from django import forms

class NewClientForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget)