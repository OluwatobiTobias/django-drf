
from typing import Optional

from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "chapter_5/home.html"

class BlogDetailView(DetailView): 
    model = Blog
    template_name = "chapter_5/about.html"

class BlogCreateView(CreateView):
    model = Blog
    template_name: str = "chapter_5/create_new.html"
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Blog
    template_name: str = "chapter_5/update_blog.html"
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Blog
    template_name: str = "chapter_5/delete_blog.html"
    success_url: Optional[str] = reverse_lazy("chapter_5:home5")
