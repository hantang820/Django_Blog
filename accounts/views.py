from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView

def signup_success(request):
    return render(request, 'accounts/signup_success.html')

signup = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'accounts/signup.html',
    success_url = '/accounts/signup_success/',
)

login = LoginView.as_view(
    template_name = 'accounts/login.html',
    next_page = '/'
)

logout = LogoutView.as_view(
    next_page = '/'
)
