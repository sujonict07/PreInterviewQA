from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PreInterviewModelForm
from .models import PreInterviewModel
# Create your views here.


class SignUp(CreateView):
    form_class = UserCreationForm
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


def employee_list_view(request):
    print(request)
    queryset = PreInterviewModel.objects.all()
    print(queryset)
    context = {
        "object_list" : queryset
    }
    return render(request, "preinterviewqaapp/details.html",context=context)