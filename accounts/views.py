from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    numbers = [29, 89, 3, 32, 22, 1]
    name = "Table"
    context = {
        'name': name,
        'numbers': numbers
    }

    return render(request, 'accounts/home.html', context)
