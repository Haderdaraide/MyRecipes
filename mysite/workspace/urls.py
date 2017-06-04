from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)


urlpatterns = [
    url(r'^$', views.view_workspace, name='view_workspace'),
    url(r'^my_recipes/$', views.my_recipes, name='my_recipes'),
    url(r'^add_recipe/$', views.add_recipe, name='add_recipe'),
    url(r'^view_profile/$', views.view_profile, name='view_profile')
]


