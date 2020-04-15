from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import BlogPost
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='supersecretandhard'
        )

        self.post = BlogPost.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user
        )

    def test_string_representation(self):
        post = BlogPost(title='A sample title')
        self.assertEqual(str(post),post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','A good title')
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.body}','Nice body content')
    
    def test_post_list_view(self):
        resp = self.client.get(reverse('blogposts'))
        self.assertEqual(resp.status_code,200)
        self.assertContains(resp,'Nice body content')
        self.assertTemplateUsed(resp,'blogpostlist.html')

    def test_post_detail_view(self):
        resp = self.client.get('/blogposts/post/1/')
        no_resp = self.client.get('/blogposts/post/10000/')
        self.assertEqual(resp.status_code,200)
        self.assertEqual(no_resp.status_code,404)
        self.assertTemplateUsed(resp,'blogpostdetial.html')