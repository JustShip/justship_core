from graphene_django import DjangoObjectType

from ..models import Resource, Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        only_fields = (
            'id',
            'name',
            'description',
        )


class ResourceType(DjangoObjectType):
    class Meta:
        model = Resource
        only_fields = (
            'id',
            'title',
            'url',
            'category',
            'image',
            'description',
            'creator',
        )


resource_types = [
    ResourceType, CategoryType
]
