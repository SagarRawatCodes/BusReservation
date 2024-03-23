from django.shortcuts import HttpResponse,render

# Create your views here.
def ordersaction(request):
    return render(request, 'orders.html')
def s(request):
    return HttpResponse(request,":hi")
