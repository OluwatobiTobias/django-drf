from django.urls import path

from .views import BlogDetailView, BlogListView

app_name = 'chapter_5'

urlpatterns = [
    path('', BlogListView.as_view(), name='home5'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='about5'),
]
