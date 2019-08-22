from django import forms
from .models import ServiceTemplate, Service

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

class ServiceCreateForm(forms.Form):
    template = forms.ModelChoiceField(
        queryset=None
    )
    count = forms.IntegerField()
    date = forms.CharField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'time_field'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ServiceCreateForm, self).__init__(*args, *kwargs)
        self.fields['template'].queryset = ServiceTemplate.objects.filter(church=self.user.home_church)

    class Meta:
        model = Service
