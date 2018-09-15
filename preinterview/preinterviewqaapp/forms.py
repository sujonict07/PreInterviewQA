from django import forms

from .models import PreInterviewModel
from .models import JOB_CHOICES


class PreInterviewModelForm(forms.ModelForm):
    name = forms.CharField(label="Input your name",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "your Name"
                                }
                            )
                            )
    email = forms.EmailField(help_text='A valid email address, please.')

    join_time = forms.CharField(label="When you can start working in DDS?",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Working Time"
                                }
                            )
                            )
    why_join = forms.CharField(required=False,
                    widget=forms.Textarea(
                        attrs={
                            "class": "new-class-name",
                            "placeholder": "your description",
                            "id": "my-id-for-textarea",
                            "row": 12,
                            "cols": 12
                        }
                    )
                )

    current_salary = forms.DecimalField(initial=199.90)
    salary_expection = forms.DecimalField(initial=199.90)
    interested_job = forms.ChoiceField(choices=JOB_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = PreInterviewModel
        fields = [
            'name',
            'email',
            'join_time',
            'current_salary',
            'salary_expection',
            'why_join',
            'week_day',
            'interview_time',
            'interested_job',
        ]