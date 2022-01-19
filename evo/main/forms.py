from dataclasses import field
from .models import Person
from django.forms import ModelForm, TextInput


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ["name", ]

        widgets = {
            "title": TextInput(attrs={
                'placeholder': "Як тебе можна звати?"
            })
        }
