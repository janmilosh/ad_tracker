from django import forms
from models import Newspaper


class NewspaperForm(forms.ModelForm):

    class Meta:
        model = Newspaper