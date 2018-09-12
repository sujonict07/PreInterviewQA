from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PreInterviewModelForm
# Create your views here.


class SignUp(CreateView):
    form_class = UserCreationForm
    print("this is signup")
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def preinterview_question_answer_create_view(request):
    form = PreInterviewModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PreInterviewModelForm()

    context = {
        'form': form
    }
    return render(request, "preinterviewqaapp/home.html", context)