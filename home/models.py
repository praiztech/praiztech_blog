from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel


class HomePage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="The heading for the homepage",
    )
    intro = models.TextField(
        null=True,
        blank=True,
        help_text="Write an introduction for the blog",
    )
    cta_text = models.CharField(
        verbose_name="Homepage CTA",
        max_length=255,
        null=True,
        blank=True,
        help_text="Text to display for Homepage Call to Action",
    )
    cta_link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Homepage CTA link",
        help_text="Choose a page to link to for the Homepage Call to Action",
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("heading"),
        FieldPanel("intro"),
        FieldPanel("cta_text"),
        PageChooserPanel("cta_link_page"),
    ]
