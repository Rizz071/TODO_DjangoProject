from django import forms
from django.forms import Textarea

from .models import TodoList, TodoTitle


class InputForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['todo_text']
        labels = {'todo_text': ''}

        widgets = {
            "todo_text": Textarea(attrs={"rows": 1, "class": "form-control"}),
        }


class addListForm(forms.ModelForm):
    class Meta:
        model = TodoTitle
        fields = ['title']
        labels = {'title': ''}

        widgets = {
            "title": Textarea(attrs={"rows": 1, "class": "form-control"}),
        }


class delListForm(forms.Form):
    pass
