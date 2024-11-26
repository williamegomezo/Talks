from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.core.models import Page, Orderable, ParentalKey
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel


from core.models.serializers import ResponsiveImageSerializer


class HomePage(Page):
    parent_page_types = ['wagtailcore.Page']

    main_header = models.TextField()
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('main_header'),
        ImageChooserPanel('hero_image')
    ]

    api_fields = [
        APIField('main_header'),
        APIField('hero_image', serializer=ResponsiveImageSerializer()),
    ]