from django import forms
from captcha.fields import CaptchaField,CaptchaTextInput

CHOICES = [
    (None, '--Select Subject--'),
    ('MSSP Service Enquiry', 'MSSP Service Enquiry'),
    ('Partnership Enquiry', 'Partnership Enquiry'),
    ('Issue Complain', 'Issue Complain'),
    ('other', 'Other')
]

class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'fields/captcha_field.html'

class ContactForm(forms.Form):
    error_css_class = 'text-danger'

    name = forms.CharField( label='', max_length =100, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    email = forms.EmailField( label='', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your email', 'type': 'email'}))
    subject = forms.ChoiceField(label='', choices=CHOICES, required=True, widget = forms.Select(attrs={'class': 'form-control', 'placeholder': '---', 'type': 'select'}))
    message = forms.CharField( label='', widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': '7'}))
    captcha = CaptchaField(label="",widget=CustomCaptchaTextInput(attrs={'class': 'form-control border-left border-right px-2','placeholder':'Enter The Captcha'}))