from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from blog.views import IndexView,PostListView,PostDetailView


class TestUrl(TestCase):
    def test_blog_index_url_resolve(self):
        url = reverse('blog:index')
        self.assertEquals(resolve(url).func.view_class,IndexView)
    
    def test_blog_post_list_resolve(self):
        url = reverse('blog:post-list')
        self.assertEquals(resolve(url).func.view_class,PostListView)
    
    def test_blog_post_detail_resolve(self):
        url = reverse('blog:post-detail',kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class,PostDetailView)
    

