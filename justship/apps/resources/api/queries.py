import graphene

from .types import CategoryType
from .. import models


class ResourceQueries:
    category = graphene.Field(CategoryType, category_id=graphene.Int())
    categories = graphene.List(CategoryType)

    def resolve_category(self, info, category_id):
        return models.Category.objects.get(pk=category_id)

    def resolve_categories(self, info):
        return models.Category.objects.all()
