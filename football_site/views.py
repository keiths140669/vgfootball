from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def home(request):
	
	return render(request, 'football_site/home.html')