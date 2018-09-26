from .models import *

from datetime import datetime
from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView

# Create your views here.


class Dashboard(View):
    template_name = 'dashboard.html'
    def get(self, request, *args, **kwargs):
        announcements = Announcement.objects.filter(post_status=True).order_by('-date_pub')
        
        context = {'announce':announcements, 'date_today':datetime.now().date}
        
        return render(request, self.template_name, context)

class AnnouncementListView(ListView):
    model = Announcement
    object_list = Announcement.objects.all()
    date_today = datetime.now().date
    

class AnnouncementMenu(View):
    date_today = datetime.now().date()
    def get(self, request, *args, **kwargs):
        announcements = Announcement.objects.all()
        
        context = {'announce':announcements, 'date_today':date_today}
        return render(request, 'announcement-menu.html', context)
    
class NewAnnouncement(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'announcement-new.html', context)
    