from django import forms

from .models import PreInterviewModel


class PreInterviewModelForm(forms.ModelForm):
    name = forms.CharField(label="Input your name",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "your Name"
                                }
                            )
                            )
    email = forms.EmailField(help_text='A valid email address, please.')

    jointime = forms.CharField(label="When you can start working in DDS?",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Working Time"
                                }
                            )
                            )
    whyjoin = forms.CharField(required=False,
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

    currentsalary = forms.DecimalField(initial=199.90)
    salaryexpection = forms.DecimalField(initial=199.90)


    class Meta:
        model = PreInterviewModel
        fields = [
            'name',
            'email',
            'jointime',
            'currentsalary',
            'salaryexpection',
            'whyjoin'
        ]


class RawPreInterviewModelForm(forms.Form):
    name = forms.CharField(label="Input your name",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "your Name"
                                }
                            )
                            )
    email = forms.EmailField(help_text='A valid email address, please.')

    jointime = forms.CharField(label="When you can start working in DDS?",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Working Time"
                                }
                            )
                            )
    whyjoin = forms.CharField(required=False,
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

    currentsalary = forms.DecimalField(initial=199.90)
    salaryexpection = forms.DecimalField(initial=199.90)

