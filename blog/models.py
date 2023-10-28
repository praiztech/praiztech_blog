from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from base.models import ContentBlock


class BlogPage(Page):
    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Teaser image for a blog post",
    )
    date_published = models.DateField("Publish date")
    body = StreamField(
        ContentBlock(), 
        verbose_name="Post content", 
        blank=True, 
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("feed_image"),
        FieldPanel("date_published"),
        FieldPanel("body"),
    ]

    parent_page_types = ["BlogIndexPage"]
    subpage_types = []


class BlogIndexPage(Page):
    intro = models.TextField(
        help_text="Text to introduce the blog index page", 
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    
    subpage_types = ["BlogPage"]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        context['blog_entries'] = BlogPage.objects.child_of(self).live().order_by('-first_published_at')
        return context
