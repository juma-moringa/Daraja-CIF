from django import forms
from django.forms import ModelForm

from darajacifapp.models import Contact
# Create your forms here.

# class ContactForm(forms.ModelForm):
# 	first_name = forms.CharField(max_length = 50)
# 	last_name = forms.CharField(max_length = 50)
# 	email_address = forms.EmailField(max_length = 150)
# 	message = forms.CharField(widget = forms.Textarea, max_length = 1000)

class ContactForm(ModelForm):	
	class Meta:
		model = Contact
		fields = "__all__"