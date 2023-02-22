from django.shortcuts import render

# Create your views here.

def index_job(request):
    return render(request, 'index.html')
