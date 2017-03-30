from django.shortcuts import render

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.forms.models import formset_factory, modelformset_factory
from django.views.generic.edit import FormView

from mainsite.models import PersonalProfile
from mainsite.models import JobInformation
from mainsite.models import RelativeInformation
from mainsite.models import ThirdPlatformAccount
from mainsite.models import Attachments

from mainsite.forms import PersonalProfileForm
from mainsite.forms import JobInformationForm
from mainsite.forms import RelativeInformationForm, RelativeInformationFormSet
from mainsite.forms import ThirdPlatformAccountForm
from mainsite.forms import AttachmentsForm


# Create your views here.
def home(request):
    context = dict()
    return render(request, "index.html", context)


class PersonalProfileView(FormView):
    '''
        According to: http://stackoverflow.com/questions/21606739/django-update-model-with-formview-and-modelform
    '''
    template_name = "personal_profile/edit.html"
    form_class = PersonalProfileForm
    success_url = 'jobinfo'

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(PersonalProfileView, cls).as_view(**initkwargs)
        return login_required(view, login_url='/user/login')

    def get_form(self, form_class):
        try:
            profile = PersonalProfile.objects.get(user=self.request.user)
            return form_class(instance=profile, **self.get_form_kwargs())
        except PersonalProfile.DoesNotExist:
            return form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(PersonalProfileView, self).form_valid(form)

class JobInformationView(FormView):
    """
    """
    template_name = "personal_profile/edit.html"
    form_class = JobInformationForm
    success_url = 'relativeinfo'

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(JobInformationView, cls).as_view(**initkwargs)
        return login_required(view, login_url='/user/login')
            
    def get_form(self, form_class):
        try:
            jobinfo = JobInformation.objects.get(user=self.request.user)  
            return form_class(instance=jobinfo, **self.get_form_kwargs())
        except JobInformation.DoesNotExist:
            return form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(JobInformationView, self).form_valid(form)


class RelativeInformationView(FormView):
    """

    """
    template_name = "personal_profile/edit.html"
    #form_class = RelativeInformationForm
    form_class = RelativeInformationFormSet

    success_url = 'attachments'

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(RelativeInformationView, cls).as_view(**initkwargs)
        return login_required(view, login_url='/user/login')
            
    def get_form(self, form_class):
        try:
            relatives = RelativeInformation.objects.filter(user=self.request.user)
            return form_class(queryset=relatives, **self.get_form_kwargs())
        except RelativeInformation.DoesNotExist:
            return form_class(**self.get_form_kwargs())

    def form_valid(self, formset):
        for form in formset:
            form.instance.user = self.request.user
        formset.save()
        return super(RelativeInformationView, self).form_valid(formset)


class ThirdPlatformAccountView(FormView):
    """
    """
    template_name = "personal_profile/edit.html"
    #form_class = ThirdPlatformAccountForm
    form_class = modelformset_factory(ThirdPlatformAccount, 
                                        form=RelativeInformationForm, 
                                        extra=2, max_num=2)
    success_url = 'attachments'

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(ThirdPlatformAccountView, cls).as_view(**initkwargs)
        return login_required(view, login_url='/user/login')
            
    def get_form(self, form_class):
        try:
            accounts = ThirdPlatformAccount.objects.filter(user=self.request.user)
            return form_class(queryset=accounts, **self.get_form_kwargs())
        except ThirdPlatformAccount.DoesNotExist:
            return form_class(**self.get_form_kwargs())

    def form_valid(self, formset):
        for form in formset:
            form.instance.user = self.request.user
        formset.save()
        return super(ThirdPlatformAccountView, self).form_valid(formset)


class AttachmentsView(FormView):
    """
    """
    template_name = "personal_profile/attachments.html"
    form_class = AttachmentsForm
    success_url = '/'

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(AttachmentsView, cls).as_view(**initkwargs)
        return login_required(view, login_url='/user/login')
            
    def get_form(self, form_class):
        try:
            attachments = Attachments.objects.get(user=self.request.user)
            return form_class(instance=attachments, **self.get_form_kwargs())
        except Attachments.DoesNotExist:
            return form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(AttachmentsView, self).form_valid(form)


# def personal_profile(request):
#   if request.method == 'POST':
#       form = PersonalProfileForm(request.POST)
#       if form.is_valid():
#           form.user = request.user
#           form.save()
#           return HttpResponse('ok!')
#   else:
#       form = PersonalProfileForm()
#   return render_to_response("personal_profile/edit.html", "")
