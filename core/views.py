from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html', {})

def play(request):
    if request.method == "POST":
        username = request.POST.get('username')
        request.session["username"] = username
        return render(request, 'core/play.html', {
            'error_message': "You're logged in as " + username
        })
    return render(request, 'core/play.html', {})