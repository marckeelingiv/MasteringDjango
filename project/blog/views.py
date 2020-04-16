from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import BlogPost
# Create your views here.
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blogpostlist.html'
    context_object_name = 'all_posts_list'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpostdetial.html'

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blogpost_create.html'
    fields = ['title','author','body']

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blogpost_update.html'
    fields = ['title','body']

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogpost_delete.html'
    success_url = reverse_lazy('blogposts')