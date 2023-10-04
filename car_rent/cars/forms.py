from django import forms
from captcha.fields import CaptchaField
from .models import Car, CarPost


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email', max_length=255)
    content = forms.CharField(label='Complaint', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()


class CarPostForm(forms.ModelForm):
    class Meta:
        model = CarPost
        fields = ['title', 'description', 'slug', 'daily_rent_cost', 'is_published', 'properties', 'category']
