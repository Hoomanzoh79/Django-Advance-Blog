import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime

@pytest.mark.django_db
class TestPostApi:
    client = APIClient()

    def test_get_post_response_200_status(self):
        url = reverse('blog:api-v1:post-list')
        response = self.client.get(url)
        assert response.status_code == 200
    
    def test_create_post_response_401_status(self):
        url = reverse('blog:api-v1:post-list')
        data = {
            'title':'test title',
            'content':'test content',
            'status':True,
            'published_data':datetime.now(),
        }
        response = self.client.post(url,data=data)
        assert response.status_code == 401