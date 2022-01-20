from contextlib import redirect_stderr
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render, redirect
from django .views.generic import DetailView
from .forms import PersonForm
# Create your views here.
from .models import Person


def main_view(request):
    return render(request, 'main/main.html', {})


def main(request):
    error = ''
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin')
        else:
            error = "Щось пішло не так =("

        form = PersonForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/main.html', data)
