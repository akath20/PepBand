"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from PepBandWebsite import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^auth/$', views.auth_view, name='auth_view'),
    # url(r'^loggedin/$', views.loggedin, name='loggedin'),
    # url(r'^invalid/$', views.invalid, name='invalid'),
    url(r'^eboard/$', views.eboard, name='eboard'),
    url(r'^section_leaders/$', views.section_leaders, name='section_leaders'),
    url(r'^constitution/$', views.constitution, name='constitution'),
    url(r'^home/$', views.home, name='home'),
    url(r'^admin_page/$', views.admin_page, name='admin_page'),
    url(r'^new_song/$', views.new_song, name='new_song'),
]
