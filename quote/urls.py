from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.base, name='index'),
    url(r'^api/posts/', include("API.urls", namespace='posts-api')),
]