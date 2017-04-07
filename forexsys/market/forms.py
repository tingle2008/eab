import operator
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.forms.models import BaseModelFormSet
from django.forms.models import inlineformset_factory

from models import TempTableModel


class TempTableForm(ModelForm):
    class Meta:
        model  = TempTableModel
        fields = ('dt','sym','o','h','l','c','v',)
