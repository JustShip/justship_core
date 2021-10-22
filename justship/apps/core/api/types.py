from graphene_django import DjangoObjectType
from justship.apps.core.models import Tag


class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        only_fields = (
            'name',
        )


core_types = [
    TagType
]
