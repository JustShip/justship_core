from graphene_django import DjangoObjectType

from ..models import Resource, Category, Vote


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
            'categories',
            'image',
            'description',
            'creator',
            'vote_amount'
        )


class VoteType(DjangoObjectType):
    class Meta:
        model = Vote
        only_fields = (
            'resource',
            'voted_by'
        )


resource_types = [
    ResourceType, CategoryType, VoteType
]
