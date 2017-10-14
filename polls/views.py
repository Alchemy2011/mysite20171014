from django.shortcuts import render


# Create your views here.
def index(request):
    hello = "Hello, world. You're at the polls index."
    return render(request, 'polls/index.html', {'hello': hello})
