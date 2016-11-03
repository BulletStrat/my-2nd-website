from django.conf.urls import url


from API.views import (
    PostListAPIView,
    PostCreateAPIView

)



urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),


]