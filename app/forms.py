from django import forms
from django.db import models
from django.forms import fields
from .models import Etudiant

class EtudiantForm(forms.Form):

    class Meta:
        model = Etudiant
        fields = '__all__'