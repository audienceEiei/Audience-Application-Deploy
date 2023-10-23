from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, get_user_model
from django.contrib import messages
from user_profile.models import UserProfile
from django.contrib.auth.backends import ModelBackend


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            gender = form.cleaned_data.get("gender")
            age = form.cleaned_data.get("age")
            country = form.cleaned_data.get("country")
            profile = UserProfile.objects.create(user=user, gender=gender, age=age, country=country)
            profile.save()
            
            # Explicitly specify the backend when calling login
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            messages.success(request, "Registration successful.")
            return redirect("audience:dashboard")
        
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, "account/register.html", {"register_form": form})
