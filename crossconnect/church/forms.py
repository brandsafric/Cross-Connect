from django import forms

class ChurchCreateForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_field'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_field'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_field'}))
