from django.urls import path

from .views import (BlogCreateView, BlogDeleteView, BlogDetailView,
                    BlogListView, BlogUpdateView)

app_name = 'chapter_5'

urlpatterns = [
    path('', BlogListView.as_view(), name='home5'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='about5'),
    path('blog/new_post/', BlogCreateView.as_view(), name='create5'),
    path('blog/update/<int:pk>/edit/', BlogUpdateView.as_view(), name='update5'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete5'),

]
