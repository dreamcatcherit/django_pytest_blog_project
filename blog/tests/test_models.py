import datetime

import pytest

from django.utils import timezone

from blog.models import BlogPost


@pytest.mark.django_db
def test_blog_post_published_recently_with_future_post():
    publish_date = timezone.now() + datetime.timedelta(days=30)
    post = BlogPost.objects.create(
        title="Test blog post",
        slug="test-blog-post",
        content="Test content for blog post.",
        publish_date=publish_date
    )
    assert post.published_recently() is False


@pytest.mark.django_db
def test_blog_post_published_recently_with_old_post():
    publish_date = timezone.now() - datetime.timedelta(days=7)
    post = BlogPost.objects.create(
        title="Test blog post",
        slug="test-blog-post",
        content="Test content for blog post.",
        publish_date=publish_date
    )
    assert post.published_recently() is False


@pytest.mark.django_db
def test_blog_post_published_recently_with_recent_post():
    publish_date = timezone.now()
    post = BlogPost.objects.create(
        title="Test blog post",
        slug="test-blog-post",
        content="Test content for blog post.",
        publish_date=publish_date
    )
    assert post.published_recently() is True
