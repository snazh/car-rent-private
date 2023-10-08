from django import forms
from captcha.fields import CaptchaField
from .models import CarPost


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email', max_length=255)
    content = forms.CharField(label='Complaint', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()


class CarPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['category'].empty_label = "Category not selected"

    class Meta:
        model = CarPost
        fields = ['title', 'description', 'status', 'daily_rent_cost', 'photo',
                  'category', 'model', 'vendor', 'year']
