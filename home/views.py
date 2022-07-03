from django.conf import settings
from django.shortcuts import render
from django.views import View
import requests
import os
import pandas as pd
from datetime import datetime
from home.models import ExcelFile


if settings.DEBUG:
    END_POINT = 'http://127.0.0.1:8000/get_data/'
else:
    END_POINT = 'https://get-brazilian-docs.herokuapp.com/get_data/'


class Home(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        # Get text from form
        text = request.POST.get('text')
        
        # Fetch data from API
        session = requests.session()
        resp = session.post(END_POINT, data={'text': text})
        data = resp.json()

        # Save content in .xlsx file
        df = pd.DataFrame.from_dict(data, orient='index')
        df = df.transpose()
        file_path = os.path.join(settings.MEDIA_ROOT, datetime.now().isoformat() + '.xlsx')
        new_file = df.to_excel(file_path, index=False)

        # Create a model instance to get an url to download file
        excel_file = ExcelFile(new_file)
        data.update({'excel_file_url': os.path.join('..', 'media', os.path.basename(file_path))})

        return render(request, 'home.html', context=data)


class ExportExcel(View):
    pass