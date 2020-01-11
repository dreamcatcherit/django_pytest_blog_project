import pytest

from django.urls import reverse
from django.utils import timezone

from blog.models import BlogPost
from blog.views import index


@pytest.mark.django_db
def test_index_view(client):
    publish_date = timezone.now()
    BlogPost.objects.create(
        title="Test blog post 1",
        slug="test-blog-post-1",
        content="Test content for blog post 1.",
        publish_date=publish_date
    )
    BlogPost.objects.create(
        title="Test blog post 2",
        slug="test-blog-post-2",
        content="Test content for blog post 2.",
        publish_date=publish_date
    )

    url = reverse("blog:home")
    request = client.get(url)
    response = index(request)
    content = response.content.decode(response.charset)
    assert response.status_code == 200
    assert "Test blog post 1" in content
    assert "Test blog post 2" in content
