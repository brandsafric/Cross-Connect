from django import forms

class ContactCreateForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_field'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_field'}))
