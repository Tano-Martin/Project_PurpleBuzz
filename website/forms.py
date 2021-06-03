from django import forms
from django.forms.forms import Form
from .models import Contact, Newsletter
from django import forms 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'company', 'subject', 'message']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email"]



