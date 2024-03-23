from django.shortcuts import render

def homeaction(request):
    return render(request,'home.html')
