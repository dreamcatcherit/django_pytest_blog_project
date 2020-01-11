from django import forms

from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "slug", "content", "publish_date"]

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(id=instance.id)
        if qs.exists():
            raise forms.ValidationError("This title has already been used. Please try again.")
        return title
