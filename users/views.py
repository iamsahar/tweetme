from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import ProfileForm, UpdateForm, SignUpForm, LoginForm
from django.views.generic import RedirectView, CreateView, UpdateView
from django.views.generic.edit import FormView 
from django.urls import reverse, reverse_lazy


# def register(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'{username} your Account has been created! You are now able to login.')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, "users/register.html", {"form": form})

class SignUpView(CreateView):
    """
    Provides the ability to signup
    """
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'


class LoginView(FormView):
    """
    Provides the ability to login as a user with username and password
    """
    form_class = LoginForm
    template_name = 'users/login.html'
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        # Check here if the user is an admin
        if user is not None and user.is_active:
            login(self.request, user)
            return HttpResponseRedirect('/')
        else:
            return self.form_invalid(form)


# @login_required
class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/login/'
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST,
                                 request.FILES,
                                 instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated.')
            return redirect('profile')
    else:
        u_form = UpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)
