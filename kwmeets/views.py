from django.shortcuts import render

# Create your views here.
def show_feeds(request):
    return render(request, 'index.html')