from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. You can log in now.")
            return redirect("accounts:login")
    else:
        form = UserRegistrationForm()

    return render(request, "accounts/register.html", {"form": form})

@login_required
def profile(request):
    return render(request,"accounts/profile.html")

@login_required
def profile(request):
    return render(request, "accounts/profile.html", {"profile": request.user.profile})


@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated.")
            return redirect("accounts:profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, "accounts/profile_edit.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })