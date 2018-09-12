from django.urls import path

from .views import SignUp, preinterview_question_answer_create_view


app_name = 'preinterviewqaapp'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('create/', preinterview_question_answer_create_view, name='creates'),
]