from django.shortcuts import get_object_or_404
from rest_framework.fields import Field
from rest_framework.filters import BaseFilterBackend
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.serializers import PageSerializer
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from wagtail.images.api.v2.views import ImagesAPIViewSet


# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests

def get_page_relative_url(page):
    return page.get_url_parts()[2]


class PageRelativeUrlField(Field):
    def get_attribute(self, instance):
        return instance

    def to_representation(self, page):
        return get_page_relative_url(page)


class CustomPageSerializer(PageSerializer):
    relative_url = PageRelativeUrlField(read_only=True)


class UrlFilter(BaseFilterBackend):
    """
    Implements the ?detail_url filter which limits the set of pages to a
    particular detail_url.
    """
    def filter_queryset(self, request, queryset, view):
        if 'relative_url' in request.GET:
            queryset = queryset.filter(page__site=request.GET['relative_url'])
        return queryset


class CustomPagesAPIViewSet(PagesAPIViewSet):
    base_serializer_class = CustomPageSerializer

    meta_fields = PagesAPIViewSet.meta_fields + [
        'relative_url',
    ]

api_router.register_endpoint('pages', CustomPagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)