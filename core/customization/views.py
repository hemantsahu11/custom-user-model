from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserProfileForm, UserForm
from django.db import transaction
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return HttpResponse("home page customization")


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect("user:profile")
    else:
        user_form = UserForm(instance=request.user)   # render the form for the user who have logged in that's why request.user which stands for current user
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, "customization/profile.html", {'user_form':user_form, 'user_profile_form':user_profile_form})
