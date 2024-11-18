from django import forms

from .models import Simpson


class MoveForm(forms.ModelForm):

    class Meta:
        model = Simpson
        fields = ('lieu', )