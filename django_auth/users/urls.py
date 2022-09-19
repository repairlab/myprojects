from django.urls import re_path
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    re_path(r'^create/$', CreateUserAPIView.as_view()),
    re_path(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
    re_path(r'^login/$', obtain_auth_token)
    
]