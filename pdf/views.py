from django.shortcuts import render
from .models import Profile


# Create your views here.
def profile(request):
    return render(request, 'pdf/accept.html', )