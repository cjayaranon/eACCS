from .models import *

from datetime import datetime
from django.conf import settings
from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class Dashboard(View):
    def get(self, request, *args, **kwargs):
        announcements = Announcement.objects.filter(post_status=True).order_by('-date_posted')
        
        context = {'announce':announcements, 'date_today':datetime.now().date}
        
        return render(request, 'dashboard.html', context)
    

class AnnouncementMenu(View):
    def get(self, request, *args, **kwargs):
        announcements = Announcement.objects.all()
        context = {'announce':announcements}
        return render(request, 'announcement-menu.html', context)
    
class NewAnnouncement(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'announcement-new.html', context)