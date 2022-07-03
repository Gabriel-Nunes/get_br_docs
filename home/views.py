from django.conf import settings
from django.shortcuts import render
from django.views import View
import requests

if settings.DEBUG:
    END_POINT = 'http://127.0.0.1:8000/get_data/'
else:
    END_POINT = 'https://get-brazilian-docs.herokuapp.com/get_data/'

class Home(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        text = request.POST.get('text')
        session = requests.session()
        resp = session.post(END_POINT, data={'text': text})
        data = resp.json()
        print(data.get('cpfs_found'))

        return render(request, 'home.html', context={'cpfs': data.get('cpfs_found')})