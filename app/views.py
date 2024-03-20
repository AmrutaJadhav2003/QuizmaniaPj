from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Result
from .forms import QuestionForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import JsonResponse






def quiz_view(request):
    return render(request, 'app/quiz.html')

def next_page_view(request):
   return render(request, 'next_page.html')
def next_page_quiz(request):
   return render(request, 'quiz.html')  # Render the quiz.html template



def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question-list')  # Redirect to a page showing all questions
    else:
        form = QuestionForm()
    return render(request, 'create_question.html', {'form': form})

# def calculate_score(quiz_submission_data):
#     # Example logic to calculate score based on quiz_submission_data
#     score = 0
#     for question_id, answer in quiz_submission_data.items():
#         # Assuming each question ID is associated with the correct answer in your database
#         question = Question.objects.get(id=question_id)
#         if answer == question.correct:
#             score += 1
#     return score



# @login_required
# def submit_quiz(request):
#     if request.method == 'POST':
#         # Initialize the score
#         score = 0
        
#         # Iterate over the form data to calculate the score
#         for key, value in request.POST.items():
#             # Check if the key corresponds to a question ID
#             if key.startswith('question'):
#                 # Extract the question ID from the key
#                 question_id = key.replace('question', '')
                
#                 # Retrieve the question object from the database
#                 try:
#                     question = Question.objects.get(id=int(question_id))
#                 except Question.DoesNotExist:
#                     # Handle the case where the question does not exist
#                     # You may want to log an error or handle it differently
#                     continue
                
#                 # Compare the submitted answer with the correct answer
#                 if value == question.correct:
#                     score += 1
        
#         # Create a Result object for the current user with the calculated score
#         Result.objects.create(user=request.user, score=score)
        
#         # Redirect the user to the quiz completed page
#         return redirect('quiz_completed')  
#     else:
#         # If the request method is not POST, redirect to the next page
#         return redirect('next_page')




# def quiz_view(request):
#     questions = Question.objects.all()
#     return render(request, 'next_page.html', {'questions': questions})



def  next_page_view(request):
    # Retrieve all questions from the database
    questions = Question.objects.all()
    
    # Pass the questions to the template context
    context = {'questions': questions}
    
    # Render the template with the provided context
    return render(request, 'next_page.html', context)




def custom_login(request, **kwargs):
    if request.user.is_authenticated:
        return redirect('quiz_completed')
    else:
        return LoginView.as_view()(request, **kwargs)
    
@login_required
def quiz_completed_view(request):
    latest_result = None
    try:
        latest_result = Result.objects.filter(user=request.user).order_by('-id').first()
        quiz_result_message = f"Thank you for completing the quiz! Your score is {latest_result.score}." if latest_result else "No quiz results found for this user."
    except Result.DoesNotExist:
        quiz_result_message = "No quiz results found for this user."

    print("Quiz Result Message:", quiz_result_message)  # For debugging

    return render(request, 'app/quiz_completed.html', {'quiz_result_message': quiz_result_message})



def quiz_view(request):
    questions = Question.objects.all()
    return render(request, 'quiz.html', {'questions': questions})

def calculate_score(quiz_submission_data):
    score = 0
    for key, value in quiz_submission_data.items():
        if key.startswith('answer'):  # Check if the key is for an answer
            question_id = key.replace('answer', '')  # Extract the question ID from the key
            # Assuming each question ID is associated with the correct answer in your database
            question = Question.objects.get(id=question_id)
            if value == question.correct:
                score += 1
    return score



def submit_quiz(request):
    if request.method == 'POST':
        # Process the submitted quiz data
        # For example, calculate the score
        score = calculate_score(request.POST)

        # Save the quiz result
        result = Result(user=request.user, score=score)
        result.save()

        return JsonResponse({'message': 'Quiz submitted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)



def get_questions(request):
    questions = Question.objects.all()
    data = [{
        'question': question.question,
        'option_a': question.option_a,
        'option_b': question.option_b,
        'option_c': question.option_c,
        'option_d': question.option_d,
    } for question in questions]
    return JsonResponse(data, safe=False)

def get_quiz_results(request):
    if request.user.is_authenticated:
        try:
            # Retrieve the latest quiz result for the current user
            latest_result = Result.objects.filter(user=request.user).latest('id')
            # Prepare the data to be sent as JSON response
            data = {
                'score': latest_result.score,
                'correctPredictions': latest_result.score  # Each correct answer is awarded 1 mark
            }
            return JsonResponse(data)
        except Result.DoesNotExist:
            # If no quiz result found for the user, return an empty response with status code 404
            return JsonResponse({}, status=404)
    else:
        # If the user is not authenticated, return an error response with status code 401 (Unauthorized)
        return JsonResponse({'error': 'User is not authenticated'}, status=401)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def your_view_function(request):
    # Your existing view logic
    return render(request, 'your_template.html', {'user': request.user})  