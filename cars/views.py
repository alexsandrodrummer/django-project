from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View

# Create your views here.

class CarsView(View):
    def get(self, request):  
      cars = Car.objects.all().order_by('model')
      search = request.GET.get('search')

      if search:
        cars = cars.filter(model__icontains=search)
    
      return render(
        request,
          'cars.html', 
          {'cars': cars}
        )
        

class NewCarView(View):
   
   def get(self, request):  
      new_car_form = CarModelForm()
      return render(request, 'new_car.html',{ 'new_car_form':new_car_form })
    
   def post(self, request):
      new_car_form = CarModelForm()
      if new_car_form.is_valid():
         new_car_form.save()
         return redirect('car_list')
      return render(request, 'new_car.html',{ 'new_car_form':new_car_form })
