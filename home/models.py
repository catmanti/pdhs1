from django.db import models
from wagtail.models import Page, Orderable, ParentalKey
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel


class HomePage(Page):
    """Home"""

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        InlinePanel("gallery_images", label="Carousel images"),
    ]


class CarouselItem(Orderable):
    """Add Carousel to Home page"""

    page = ParentalKey(
        HomePage, on_delete=models.CASCADE, related_name="gallery_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
    ]

    def __str__(self):
        return self.caption or f"Carousel Item #{self.pk}"
