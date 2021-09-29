import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from justshipto_core.accounts.api.schema import UserMutations, UserQueries, user_types
from justshipto_core.products.api.schema import ProductMutations, ProductQueries, product_types
from justshipto_core.resources.api.schema import ResourceMutations, ResourceQueries, resource_types


types = user_types + product_types + resource_types

class Query(ObjectType, UserQueries, ProductQueries, ResourceQueries):
    pass

class Mutation(ObjectType, UserMutations, ProductMutations, ResourceMutations):
    pass

schema = graphene.Schema(
    types=types,
    # query=Query,
    # mutation=Mutation
)
