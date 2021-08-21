from django import forms
from django.forms import TextInput


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'nameform'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your message...','class': 'messageform'}))

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        message = cleaned_data.get('message')
        if not name and not message:
            raise forms.ValidationError('You have to write something')