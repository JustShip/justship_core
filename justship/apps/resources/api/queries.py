import graphene

from .types import CategoryType
from .. import models
from .types import ResourceType


class ResourceQueries:
    category = graphene.Field(CategoryType, category_id=graphene.Int())
    categories = graphene.List(CategoryType)
    resources = graphene.List(ResourceType)

    def resolve_resources(self, info):
        pass

    def resolve_category(self, info, category_id):
        return models.Category.objects.get(pk=category_id)

    def resolve_categories(self, info):
        return models.Category.objects.all()
