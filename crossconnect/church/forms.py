from django import forms

class ChurchCreateForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_field'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_field'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_field'}))

class ServiceTemplateCreateForm(forms.Form):

    DAYS_OF_WEEK = (
        (0, 'Mondays'),
        (1, 'Tuesdays'),
        (2, 'Wednesdays'),
        (3, 'Thursdays'),
        (4, 'Fridays'),
        (5, 'Saturdays'),
        (6, 'Sundays'),
    )


    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_field'}))
    day = forms.ChoiceField(label='Day', widget=forms.Select(attrs={'class' : 'select_field'}), choices=DAYS_OF_WEEK)
    time = forms.CharField(widget=forms.TextInput(attrs={'type': 'time', 'class': 'time_field'}))
