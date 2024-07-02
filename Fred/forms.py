from django import forms
from Fred.models import Contact

class ContactForm(forms.ModelForm):
    class Meta : 
        model = Contact
        fields = "__all__"