from django.test import TestCase
from accounts.models import User,Profile
from blog.models import Post
from datetime import datetime

class TestPostModel(TestCase):
    def test_create_post_with_valid_data(self):
        user = User.objects.create_user(email='test@test.com',password='Alishab13%')
        profile = Profile.objects.create(
            user = user,
            first_name = 'test first name',
            last_name = 'test last name',
            description = 'test description',
        )

        post = Post.objects.create(
            author=profile,
            title='test-title',
            content='test content',
            status=True,
            category=None,
            published_date=datetime.now(),
        )

        self.assertEquals(post.title,'test-title')