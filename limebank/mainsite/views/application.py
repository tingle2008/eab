# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.forms.formsets import BaseFormSet
from formtools.wizard.views import SessionWizardView

from mainsite.models import RelativeInformation
from mainsite.forms import PersonalProfileForm
from mainsite.forms import JobInformationForm
from mainsite.forms import RelativeInformationFormSet

FORMS = [PersonalProfileForm, JobInformationForm, RelativeInformationFormSet]

class ApplicationWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'application.html'
    def done(self, form_list, **kwargs):
        for form in form_list:
            if issubclass(type(form), BaseFormSet):
                for subform in form:
                    subform.instance.user = self.request.user
            else:
                form.instance.user = self.request.user
            form.save()
        return HttpResponseRedirect('/')