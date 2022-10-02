from django.views.generic import ListView
from .models import Post
# Create your views here.

class HomepageView(ListView):
    model = Post
    template_name: str = 'chapter_4/home.html'