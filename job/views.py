from django.shortcuts import render

# Create your views here.

def index_job(request):
    context = {}
    return render(request, 'job/index.html', context)
