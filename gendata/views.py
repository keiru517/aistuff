from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def generate_rsa(request):
    return render(request, 'prompt.html')

def generate_sitelink(request):
    pass