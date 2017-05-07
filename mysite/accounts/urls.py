from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.view_profile, name='view_profile'),
    url(r'register/', views.register, name='register'),
    url(r'edit/$', views.edit_profile, name='edit_profile')
]


