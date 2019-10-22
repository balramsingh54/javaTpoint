from django import forms
from myApp.models import Student

class stuForm(forms.ModelForm):
    class Meta:
        model= Student
        fields = "__all__"