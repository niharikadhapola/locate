from django.shortcuts import render
import requests

from django.conf import settings
# Create your views here.


def home(request):

    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    params = {'access_key': 'your accesskey'}
    response = requests.get('http://api.ipstack.com/%s' % ip_address, params=params)
    geodata = response.json()
    return render(request, 'mysite/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'yourkey'  



    })
