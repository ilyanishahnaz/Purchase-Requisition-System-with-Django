"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from app import views as main_views
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime

from additem import views as additem_views
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', main_views.home, name='home'),
    re_path(r'^contact$', main_views.contact, name='contact'),
    re_path(r'^about$', main_views.about, name='about'),
    re_path(r'^login/$',
        LoginView.as_view(template_name = 'app/login.html'),
        name='login'),
    re_path(r'^logout$',
        LogoutView.as_view(template_name = 'app/index.html'),
        name='logout'),
    re_path(r'^menu$', main_views.menu, name='menu'),
    re_path(r'^additemform$', additem_views.additemform, name='additem_form'),
    re_path(r'^additemconfirmation$', additem_views.additemconfirmation, name='additem_confirmation'),
    re_path(r'^approvePR$', main_views.approvePR, name='approvePR'),
    re_path(r'^searchPR$', main_views.searchPR, name='searchPR'),
    re_path(r'^searchSelectedPR$', main_views.searchSelectedPR, name='searchSelectedPR'),
    re_path(r'^viewPR$', main_views.viewPR, name='viewPR'),
    re_path(r'^approveQuo$', main_views.approveQuo, name='approveQuo'),
    re_path(r'^viewQuo$', main_views.viewQuo, name='viewQuo'),
    re_path(r'^viewPRItem$', main_views.viewPRItem, name='viewPRItem'),
    re_path(r'^viewSelectedPR$', main_views.viewSelectedPR, name='viewSelectedPR'),
    re_path(r'^update_status$', main_views.update_status, name='update_status'),
    re_path(r'^viewPRQuo$', main_views.viewPRQuo, name='viewPRQuo'),
    re_path(r'^uploadedQuo$', main_views.uploadedQuo, name='uploadedQuo'),
    re_path(r'^status_quo$', main_views.status_quo, name='status_quo'),
    re_path(r'^searchQuoSelect$', main_views.searchQuoSelect, name='searchQuoSelect'),
    re_path(r'^viewApprovedQuo$', main_views.viewApprovedQuo, name='viewApprovedQuo'),
    re_path(r'^viewAppQuo$', main_views.viewAppQuo, name='viewAppQuo'),
    re_path(r'^searchQuo2$', main_views.searchQuo2, name='searchQuo2'),
    re_path(r'^searchPRQuo$', main_views.searchPRQuo, name='searchPRQuo'),
    re_path(r'^createQuo$', main_views.createQuo, name='createQuo'),
    re_path(r'^addQuoItem$', main_views.addQuoItem, name='addQuoItem'),
    re_path(r'^confirm$', main_views.confirm, name='confirm'),
    re_path(r'^generatepo$', main_views.generatepo, name='generatepo'),
    re_path(r'^generatepoform$', main_views.generatepoform, name='generatepoform'),
    re_path(r'^create_po$', main_views.create_po, name='create_po'),
    re_path(r'^viewpo$', main_views.viewpo, name='viewpo'),
    re_path(r'^viewselectedpo$', main_views.viewselectedpo, name='viewselectedpo'),
     re_path(r'^viewPRbyemp$', main_views.viewPRbyemp, name='viewPRbyemp'),
    re_path(r'^createPR$', main_views.createPR, name='createPR'),
    re_path(r'^confirm$', main_views.confirm, name='confirm'),
    re_path(r'^addPRItem$', main_views.addPRItem, name='addPRItem')
    
]

