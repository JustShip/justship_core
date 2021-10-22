import graphene
from graphene import ObjectType

from ..accounts.api.schema import UserMutations, UserQueries, user_types
from ..billing.api.schema import BillingMutations, BillingQueries, billing_types
from ..products.api.schema import ProductMutations, ProductQueries, product_types
from ..resources.api.schema import ResourceMutations, ResourceQueries, resource_types
from ..core.api.schema import CoreMutations, CoreQueries, core_types

types = user_types + billing_types + product_types + resource_types + core_types


class Query(ObjectType, UserQueries, BillingQueries, ProductQueries, ResourceQueries, CoreQueries):
    pass


class Mutation(UserMutations, BillingMutations, ProductMutations, ResourceMutations, CoreMutations, ObjectType):
    pass


schema = graphene.Schema(
    types=types,
    query=Query,
    mutation=Mutation
)
