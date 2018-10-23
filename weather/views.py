from django.shortcuts import render
import requests
from .models import City
from .forms import Cityform
# Create your views here.
def index(request):
    url = 'http://apiopenweathermap.org/data/2.5/weather?q=()&units=imperial&appid=20b4b6a8d5e4682f5dfa55bcc62d37d0'
    city = 'Las Vegas'

    if request.method == 'POST':
        form = Cityform(request.POST)
        form.save()

    form  = Cityform()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather ={
            'city':city.name,
            'temperature':r['main']['temp'],
            'description':r['weather'][e]['description'],
            'icon':r['weather'][e]['icon'],
        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data': city_weather,'form':form}
    return render(request,'weather/weather.html',context)