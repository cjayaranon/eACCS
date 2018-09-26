"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import announcements.views as an
import frontOffice.views as fo
import test1.views as te

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import (handler404)
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', te.Login.as_view(), name="login"),
#    path('main/', an.Dashboard.as_view(), name="home"),
    
    path('main/', an.AnnouncementListView.as_view(), name="home"),
    
    path('main/front-office', fo.FrontOffice.as_view(), name="front-office"),
    path('main/front-office/new-client', fo.NewClient.as_view(), name = "new-client"),
    path('main/front-office/view-client', fo.ViewClient.as_view(), name = "view-client"),
    path('main/front-office/view-client/edit-client', fo.EditClient.as_view(), name = "edit-client"),
    path('main/more/announcements-menu', an.AnnouncementMenu.as_view(), name = "announcement-menu"),
    path('main/more/announcements-menu/new-announcement', an.NewAnnouncement.as_view(), name = "announcement-new"),
    
    path('404', te.Error404.as_view(), name="error"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
