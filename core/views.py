from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html', {})

def play(request):
    return render(request, 'core/play.html', {})