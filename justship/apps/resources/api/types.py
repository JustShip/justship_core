from graphene_django import DjangoObjectType

from ..models import Resource


class ResourceType(DjangoObjectType):
    class Meta:
        model = Resource
        only_fields = (
            'id',
            'url',
            'category',
            'image',
            'description',
            'creator',
        )


resource_types = [
    ResourceType
]
