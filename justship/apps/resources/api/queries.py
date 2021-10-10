import graphene

from .types import CategoryType
from .. import models
from .types import ResourceType, VoteType


class ResourceQueries:
    category = graphene.Field(CategoryType, category_id=graphene.Int())
    categories = graphene.List(CategoryType)
    resource = graphene.Field(ResourceType, resource_id=graphene.Int())
    all_resources = graphene.List(ResourceType)
    vote = graphene.Field(VoteType, vote_url=graphene.String())

    def resolve_vote(self, info, vote_url):  # TO-DO: Change search argument or keep it
        return models.Vote.objects.get(resource=models.Resource.objects.get(url=vote_url))

    def resolve_resource(self, info, resource_id):
        return models.Resource.objects.get(pk=resource_id)

    def resolve_all_resources(self, info):
        return models.Resource.objects.all()

    def resolve_category(self, info, category_id):
        return models.Category.objects.get(pk=category_id)

    def resolve_categories(self, info):
        return models.Category.objects.all()
