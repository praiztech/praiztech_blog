from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    ListBlock,
)

from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


class HeadingBlock(StructBlock):
    heading_text = CharBlock(required=True)
    heading_size = ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h2", "H2"),
            ("h3", "H3"),
        ],
        blank=True,
        required=False,
    )

class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    alt = CharBlock(required=False)
    caption = CharBlock(required=False)

class ContentBlock(StreamBlock):
    heading = HeadingBlock()
    paragraph = RichTextBlock(blank=True)
    image = ImageBlock()
    listing = ListBlock(CharBlock(label="list_item"))

class StandardPage(Page):
    body = StreamField(
        ContentBlock(), 
        verbose_name="Page content", 
        blank=True, 
        use_json_field=True
    )
    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

class Logo(models.Model):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Site logo",
    )
    alt = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Alt text for the site logo",
    )

    panels = [
        FieldPanel("image"),
        FieldPanel("alt"),
    ]

    def __str__(self):
        return self.alt

@register_setting
class SiteSettings(BaseSiteSetting):
    title_suffix = models.CharField(
        verbose_name="Title suffix",
        max_length=255,
        help_text="The suffix for the title meta tag e.g. ' | PraizTech Blog'",
        default="PraizTech Blog",
    )

    panels = [
        FieldPanel("title_suffix"),
    ]