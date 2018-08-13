import json

from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from django_countries.fields import countries


def visit_history(request, name):
#    visit = request.session.get('visit')
    if not 'saved' in request.session or not request.session['saved']:
        request.session['visit'] = [name]
        saved_visit = request.session['visit']
    else:
        saved_visit = request.session['visit']
        saved_visit.append(name)
        request.session['saved'] = saved_visit
    return saved_visit



class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})
  

    
class MainMenu(View):
    def get(self, request, *args, **kwargs):
        name = 'main'
        visit = visit_history(request, name)
        
        context = {'item':visit, 'nbar':name}
        return render(request, 'dashboard.html', context)
#        return render(request, 'main.html', context)



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
        return render(request, 'new-client.html', {})



class Error404(View):
    def get(self, request, *args, **kwargs):
        return render(request, '404.html', {})