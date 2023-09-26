from django.test import TestCase
from accounts.models import User,Profile
from blog.models import Post
from datetime import datetime

class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com',password='Alishab13%')
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'test first name',
            last_name = 'test last name',
            description = 'test description',
        )

    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author=self.profile,
            title='test-title',
            content='test content',
            status=True,
            category=None,
            published_date=datetime.now(),
        )

        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEquals(post.title,'test-title')
        self.assertEquals(Post.objects.count(),1)