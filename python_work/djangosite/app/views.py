from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os
from app.forms import MomentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


def moments_input(request):
    if request.method == 'post':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse("app.views.welcome"))
    else:
        form = MomentForm()
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    return render(request,os.path.join(PROJECT_ROOT, 'app/templates'
                  'monents_input.html'),{'form': form})


def welcome(request):
    return HttpResponse("<h1>Welcome to my tiny twitter</h1>")
