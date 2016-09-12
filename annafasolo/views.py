from django.shortcuts import render

def home(request):
    return render(request, "annafasolo/index.html", {})

def home_files(request, filename):
	return render(request, filename, {}, content_type="text/plain")
