from django.shortcuts import render

# Create your views here.
def bag_detail(request):
    return render(request, 'bag/bag.html')
