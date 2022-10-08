from django.urls import path

from .views import SignUpVIew

urlpatterns = [
    path('signup/', SignUpVIew.as_view(), name='signup'),
]
