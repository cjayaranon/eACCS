import json

from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from django_countries.fields import countries

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})
    
    
class MainMenu(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'dashboard.html', context)


class FrontOffice(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'front-office.html', {})
    
    
    
class NewClient(View):
    def get(self, request, *args, **kwargs):
#        json_data = open("{% static 'node_modules/psgc2/cities.json' %}").read()
#        data1 = json.load(json_data)
#        data2 = json.dumps(json_data)
#        json_data.close()
        return render(request, 'new-client.html', {})