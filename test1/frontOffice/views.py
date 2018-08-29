from frontOffice.models import *

from django.conf import settings
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class FrontOffice(View):
    def get(self, request, *args, **kwargs):
        name = 'front-office'
        return render(request, 'front-office.html', {'nbar':name})
    
    

class NewClient(View):
    def get(self, request, *args, **kwargs):
#        json_data = open("{% static 'node_modules/psgc2/cities.json' %}").read()
#        data1 = json.load(json_data)
#        data2 = json.dumps(json_data)
#        json_data.close()
        name = 'front-office'
        return render(request, 'new-client.html', {'nbar':name})
    
class ViewClient(View):
    def get(self, request, *args, **kwargs):
        name = 'front-office'
        img = Client.objects.all()
        return render(request, 'view-client.html', {'nbar':name, 'pic':img})
    
    
class EditClient(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'edit-client.html', context)
    

