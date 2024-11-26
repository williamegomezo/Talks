from rest_framework.fields import Field
from collections import OrderedDict
from wagtail.images.models import SourceImageIOError


class ResponsiveImageSerializer(Field):
    @staticmethod
    def get_image_representation(image):
        return OrderedDict(
            [
                ("url", image.url),
                ("width", image.width),
                ("height", image.height),
                ("alt", image.alt),
            ]
        )

    def to_representation(self, image):
        try:
            xs = image.get_rendition('width-375')
            sm = image.get_rendition('width-768')
            md = image.get_rendition('width-1024')
            lg = image.get_rendition('width-1440')
            return OrderedDict(
                [
                    ("xs", ResponsiveImageSerializer.get_image_representation(xs)),
                    ("sm", ResponsiveImageSerializer.get_image_representation(sm)),
                    ("md", ResponsiveImageSerializer.get_image_representation(md)),
                    ("lg", ResponsiveImageSerializer.get_image_representation(lg)),
                ]
            )
        except SourceImageIOError:
            return OrderedDict(
                [
                    ("error", "SourceImageIOError"),
                ]
            )