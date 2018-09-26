from frontOffice.models import *
from frontOffice.forms import NewClientForm

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class FrontOffice(View):
    def get(self, request, *args, **kwargs):
        name = 'front-office'
        return render(request, 'front-office.html', {'nbar':name})
    
    

class NewClient(View):
    def get(self, request, *args, **kwargs):
        name = 'front-office'
        form = NewClientForm()
        return render(request, 'new-client.html', {'nbar':name, 'form':form})
    
#    def post(self, request, *args, *kwargs):
#        return render(request, '')


class ViewClient(View):
    def get(self, request, *args, **kwargs):
        name = 'front-office'
        img = Client.objects.all()
        return render(request, 'view-client.html', {'nbar':name, 'pic':img})



class EditClient(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'edit-client.html', context)
    

