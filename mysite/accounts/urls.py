from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit', views.edit_profile, name='edit_profile')
]

# urlpatterns = [
#     url(r'^$', views.register, name='register'),
# ]

