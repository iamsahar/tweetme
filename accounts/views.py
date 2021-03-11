from django.contrib.auth import login, get_user_model, logout
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .forms import UserCreationForm, UserLoginForm
from .models import ActivationProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UpdateForm


User = get_user_model()


def home(request):
    if request.user.is_authenticated:
        print("request.user.profile.city")
    return render(request, 'base.html', {})


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("accounts:login")
    return render(request, "accounts/register.html", {"form": form})


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return redirect("home")
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("accounts:login")


def activate_user_view(request, code=None, *args, **kwargs):
    if code:
        act_profile_qs = ActivationProfile.objects.filter(key=code)
        if act_profile_qs.exists() and act_profile_qs.count() == 1:
            act_obj = act_profile_qs.first()
            if not act_obj.expired:
                user_obj = act_obj.user
                user_obj.is_active = True
                user_obj.save()
                act_obj.expired = True
                act_obj.save()
                return redirect("accounts:login")
    # invalid code
    return redirect("accounts:login")


@login_required
def user_profile(request):
    if request.method == "POST":
        u_form = UpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST,
                                 request.FILES,
                                 instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated.')
            return redirect('accounts:profile')
    else:
        u_form = UpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'accounts/profile.html', context)