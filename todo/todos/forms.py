from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title","description"]
    title = forms.CharField(max_length=255, required=True)
    description = forms.CharField(max_length=8000, required=True)
