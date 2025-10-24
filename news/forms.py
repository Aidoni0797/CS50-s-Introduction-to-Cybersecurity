from django import forms
from .models import Feedback
from .models import Comment

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Ваш Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Тема'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Сообщение'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш комментарий...', 'rows': 4}),
        }