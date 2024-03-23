from django.shortcuts import render

# Create your views here.
def feedaction(request):
 return render(request, 'feedback.html')
