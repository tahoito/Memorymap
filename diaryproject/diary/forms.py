from django import forms
from .models import Diary,Todo

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = {'date','title','text'}
        widget = {
            'date': forms.TextInput(attrs={'class': 'form-control col-2'}),
            'title': forms.TextInput(attrs={'class': 'form-control col-2'}),
            'text': forms.TextInput(attrs={'class': 'form-control col-2','style': 'height: 300px;'}),
            }
        
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = {'id','memo',}
