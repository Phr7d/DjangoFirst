from django import forms
from Fred.models import Contact,NewsLetter

class ContactForm(forms.ModelForm):
    class Meta : 
        model = Contact
        fields = "__all__"
    # subject = forms.CharField(required=False)   

class NewsLetterFrom(forms.ModelForm):
    class Meta : 
        model = NewsLetter
        fields = "__all__"