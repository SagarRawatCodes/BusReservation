from django.shortcuts import render

# Create your views here.
def findbusaction(request):
    return render(request, 'findbus.html')