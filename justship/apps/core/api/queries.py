import graphene

from justship.apps.core.models import Tag
from .types import TagType


class CoreQueries:
    tags = graphene.List(TagType)

    def resolve_tags(self, info):
        return Tag.objects.all()
