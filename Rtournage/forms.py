from django import forms


class Formulaire(forms.Form):
    name = forms.CharField(label='category_name', max_length=20)
