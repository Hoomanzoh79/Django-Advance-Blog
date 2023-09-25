from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from .views import IndexView


class TestUrl(TestCase):
    def test_blog_index_url_resolve(self):
        url = reverse('blog:index')
        self.assertEquals(resolve(url).func.view_class,IndexView)
