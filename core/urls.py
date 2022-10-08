from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('follower/', include("follower.urls")),
    path('four/', include('chapter_4.urls')),
    path('', include('chapter_5.urls')),
    path('seven/', include('django.contrib.auth.urls')),
    path('seven/', include('chapter_7.urls')),

]
