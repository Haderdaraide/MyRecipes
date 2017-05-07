from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^apology/', views.apology, name='apology'),
    url(r'^home/', views.index, name='home'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    #url(r'^profile/$', views.view_profile, name='view_profile'),
    #url(r'^profile/edit/$', views.edit_profile, name='edit_profile')
]
