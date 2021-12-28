from django import forms
from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name*'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email*'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message*'}),
            'subject': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Subject*'}),
            'phone': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Phone*'})
        }
