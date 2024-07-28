from django import forms
from .models import *


class FormTarea(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = '__all__'
