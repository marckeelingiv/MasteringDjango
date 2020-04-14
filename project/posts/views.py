from django.views.generic import ListView
from .models import Post

# Create your views here.
class PostPageView(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'all_posts_list'