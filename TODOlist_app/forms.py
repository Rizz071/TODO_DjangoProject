from django import forms

from .models import TodoList


class InputForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['todo_text']
        labels = {'todo_text': 'Add new TODO entry:'}
