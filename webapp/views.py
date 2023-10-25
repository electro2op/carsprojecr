from django.shortcuts import render,redirect
from django.http import HttpResponse
from webapp.models import Car
from .forms import CarForm



# Create your views here.
def index(request):
    cars=Car.objects.all()
    context={
        'car_list':cars
    }
    return render(request,'index.html',context)
def cardetails(request,car_id):
    carr=Car.objects.get(id=car_id)
    return render(request,"details.html",{'carr':carr})
def addcar(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        cars=Car(name=name,desc=desc,year=year,img=img)
        cars.save()

    return render(request,'add.html')

def update(request, id):
    car = Car.objects.get(id=id)
    form = CarForm(request.POST or None, request.FILES, instance=car)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'cars': car})
def delete(request, id):
    if request.method=="POST":
        car = Car.objects.get(id=id)
        car.delete()
        return redirect('/')
    return render(request,'delete.html')


