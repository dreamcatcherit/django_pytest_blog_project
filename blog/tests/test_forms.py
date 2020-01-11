import pytest

from django.utils import timezone

from blog.forms import BlogPostForm
from blog.models import BlogPost


@pytest.mark.django_db
def test_blog_post_form_valid():
    publish_date = timezone.now()
    form_data = {
        "title": "Test blog post",
        "slug": "test-blog-post",
        "content": "Test content for blog post.",
        "publish_date": publish_date,
    }
    form = BlogPostForm(data=form_data)
    assert form.is_valid() is True


@pytest.mark.django_db
def test_blog_post_form_invalid():
    publish_date = timezone.now()
    BlogPost.objects.create(
        title="Test blog post",
        slug="test-blog-post",
        content="Test content for blog post.",
        publish_date=publish_date
    )
    form_data = {
        "title": "Test blog post",
        "slug": "test-blog-post",
        "content": "Test content for blog post.",
    }
    form = BlogPostForm(data=form_data)
    assert form.is_valid() is False
    assert "This title has already been used. Please try again." == form.errors["title"][0]
