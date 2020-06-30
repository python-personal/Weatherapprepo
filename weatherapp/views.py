import requests
from django.shortcuts import render,redirect
from .models import Data
from .forms import CityForm
from django.contrib import messages


def weatherview(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8527f550de53779189ed5cc0d0d09031'
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city=form.cleaned_data['name'].capitalize()

            if not Data.objects.filter(name=new_city):
                r = requests.get(url.format(new_city)).json()
                print(r['cod'])
                if r['cod']==200:
                    form.save()
                    messages.success(request,'City added successfully!')
                    return redirect('/')
                else:
                    messages.error(request,'Invalid City Name!!')
            else:
                messages.error(request,'Weather for this data is already displayed, Plz scroll below!!')
                return redirect('/')
    form = CityForm()
    cities = Data.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city.name)).json()
        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    return render(request, 'weatherapp/index.html',{'weather_data':weather_data,'form':form})


def deleteview(request,name):
    city=Data.objects.get(name=name)
    print(city)
    city.delete()
    return redirect('/')
