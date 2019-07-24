from django.shortcuts import render
import requests

from django.conf import settings
# Create your views here.


def home(request):

    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '182.73.41.154')
    params = {'access_key': 'fa684793aa8367722a5c1f7b95ae2881'}
    response = requests.get('http://api.ipstack.com/%s' % ip_address, params=params)
    geodata = response.json()
    return render(request, 'mysite/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'AIzaSyCk8y34EOxoJ1XZxtXZItmqCX-gg15C6bg'  # Don't do this! This is just an example. Secure your keys properly.



    })
