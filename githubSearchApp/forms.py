from django import forms

#Form for getting user input (URL)
class UserInputForm(forms.Form):
    url = forms.CharField(label='URL',
            widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter a valid GitHub Repositoy URL"}))