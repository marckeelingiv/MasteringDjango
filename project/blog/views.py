from django.views.generic import ListView, DetailView
from .models import BlogPost
# Create your views here.
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blogpostlist.html'
    context_object_name = 'all_posts_list'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpostdetial.html'