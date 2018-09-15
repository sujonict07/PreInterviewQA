from django.urls import path

from .views import SignUp, preinterview_question_answer_create_view, employee_list_view


app_name = 'preinterviewqaapp'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('details/',employee_list_view, name='details'),
    path('', preinterview_question_answer_create_view, name='creates'),

]