# from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Person

# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obt = Person.objects.all()
    return render(request, "index.html", {'result': obj,'final':obt})

# def flow(request):
#     obt=Person.objects.all()
    # return render(request,"index.html",{'final':obt})

# def demo(request):
#         name="Hanana"
#         return  render(request,"home.html",{'obj':name})

# def addition(request):
#         x=int(request.GET['num1'])
#         y=int(request.GET['num2'])
#         res=x+y
#         return render(request,"about.html",{'result':res})

# def about(request):
#         return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("I am contact")
