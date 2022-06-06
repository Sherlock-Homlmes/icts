from django import forms

class FormTest(forms.Form):
    name = forms.CharField(label="Name",max_length=200)
    number = forms.IntegerField(label="Number")
    check = forms.BooleanField()
