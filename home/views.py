from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'home/homepage.html')


def contact(request):
    return render(request, 'home/contact.html')
