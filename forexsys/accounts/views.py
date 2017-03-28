from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as account_login
from django.contrib.auth import logout as account_logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic.edit import UpdateView
from django import forms
from accounts.forms import UserForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))


def login(request):
    c = RequestContext(request)
    c.update(csrf(request))
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    next_page = request.GET.get('next', '/')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            account_login(request, user)
            return redirect(next_page)
        else:
            return HttpResponse("Your account has been disabled!", c)
    else:
        c['login_form'] = LoginForm()
        return render_to_response("accounts/login.html", c)


def logout(request):
    account_logout(request)
    return redirect('accounts.views.login')


class UserView(UpdateView):

    form_class = UserForm
    model = User
    template_name = "accounts/user_form.html"
    success_url = "accounts.views.profile"

    def get_object(self, queryset=None):
        obj = User.objects.get(username=self.request.user)
        return obj

    def form_valid(self, form):
        if form.is_valid():
            # if password1 exists, change password, otherwise
            # leave it
            if form.cleaned_data['password1']:
                self.object = form.save(commit=False)
                self.object.set_password(form.cleaned_data['password1'])
            self.object.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


profile = login_required(UserView.as_view())
