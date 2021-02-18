from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField( label='', max_length =100, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    email = forms.EmailField( label='', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your email', 'type': 'email'}))
    subject = forms.CharField( label='', max_length =200,widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField( label='', widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': '7'}))