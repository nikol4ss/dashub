from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

@never_cache
@login_required
def home(request):
    return render(request, "dashboard/dashboard.html")
