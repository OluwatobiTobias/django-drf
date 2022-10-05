from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("follower.urls")),
    path('four/', include('chapter_4.urls')),
    path('five/', include('chapter_5.urls')),
]
