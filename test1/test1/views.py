import json

from announcements.models import *

from django.conf import settings
from django.shortcuts import render
from django.views.generic import View


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
        
        announce = Announcement.objects.filter(post_status=True).order_by('-date_post')
        
        context = {'nbar':name, 'announce':announce}
        return render(request, 'dashboard.html', context)
#        return render(request, 'main.html', context)



class Error404(View):
    def get(self, request, *args, **kwargs):
        return render(request, '404.html', {})