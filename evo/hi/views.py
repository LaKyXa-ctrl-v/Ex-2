from django.shortcuts import render
from django .views.generic import DetailView

# Create your views here.


def main_view(request):
    return render(request, 'main.html', {})
