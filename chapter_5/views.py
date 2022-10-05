from tarfile import BLOCKSIZE

from django.views.generic import DetailView, ListView

from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "chapter_5/home.html"

class BlogDetailView(DetailView): 
    model = Blog
    template_name = "chapter_5/about.html"
