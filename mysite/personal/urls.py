from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^apology/', views.apology, name='apology'),
    url(r'^home/', views.index, name='home'),
    url(r'^logout/$', views.logout, name='logout'),
]
