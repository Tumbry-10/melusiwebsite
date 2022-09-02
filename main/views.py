from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	return render(request, 'main/index.html')

def services(request):
	return render(request, 'main/services.html')

def about(request):
	return render(request, 'main/about.html')