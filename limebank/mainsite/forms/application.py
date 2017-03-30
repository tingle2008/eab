# -*- coding: utf-8 -*-
from collections import OrderedDict

from django import forms

from mainsite.forms import PersonalProfileForm
from mainsite.forms import JobInformationForm
from mainsite.forms import RelativeInformationFormSet

class MixinLoanApplicationForm(forms.Form):
    pass