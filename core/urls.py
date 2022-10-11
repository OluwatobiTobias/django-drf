from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    #path('follower/', include("follower.urls")),
    #path('', include('chapter_4.urls')),
    #path('', include('chapter_5.urls')),
    #path('seven/', include('django.contrib.auth.urls')),
    #path('seven/', include('chapter_7.urls')),
    path('acount/', include('django.contrib.auth.urls')),
    path('eight/', include('chapter_8.urls')),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),

]
