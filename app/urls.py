from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import create_question
from .views import custom_login
from .views import get_quiz_results

urlpatterns = [
    path('', TemplateView.as_view(template_name='app/quiz.html'), name='home'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('next-page/', views.next_page_view, name='next_page'),
    #  path('next-page/quiz.html', views.next_page_quiz, name='next_page_quiz'),
     path('create/', create_question, name='create-question'),
     path('submit-quiz/', views.submit_quiz, name='submit-quiz'),
     path('quiz-completed/', TemplateView.as_view(template_name='app/quiz_completed.html'), name='quiz_completed'),
     path('accounts/login/', custom_login, name='custom_login'),
     path('get-questions/', views.get_questions, name='get_questions'),
     path('get-quiz-results/', views.get_quiz_results, name='get_quiz_results'),
 
    
   

 
]
