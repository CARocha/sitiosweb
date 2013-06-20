from django import forms

class ContactForm(forms.Form):
	nombre = forms.CharField(max_length=200)
	correo = forms.EmailField()
	asunto = forms.CharField(max_length=200, required=False)
	mensaje = forms.CharField(required=False, widget=forms.Textarea)