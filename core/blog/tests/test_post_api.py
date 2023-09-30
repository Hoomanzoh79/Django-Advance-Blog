import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def test_user():
    user = User.objects.create_user(email='test@test.com',
                                    password='Alishab13%',
                                    is_verified=True,)
    return user   

@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self,api_client):
        url = reverse('blog:api-v1:post-list')
        response = api_client.get(url)
        assert response.status_code == 200
    
    def test_create_post_response_401_status(self,api_client):
        url = reverse('blog:api-v1:post-list')
        data = {
            'title':'test title',
            'content':'test content',
            'status':True,
            'published_data':datetime.now(),
        }
        response = api_client.post(url,data=data)
        assert response.status_code == 401