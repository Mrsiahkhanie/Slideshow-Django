from django.shortcuts import render
from .models import SlideShow

# Create your views here.

def home(request):
	return render(request, 'SlideShow/home.html')
