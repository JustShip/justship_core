import graphene
import graphql_jwt
from graphene import ObjectType

from ..accounts.api.schema import UserMutations, UserQueries, user_types
from ..products.api.schema import ProductMutations, ProductQueries, product_types
from ..resources.api.schema import ResourceMutations, ResourceQueries, resource_types

types = user_types + product_types + resource_types


class Query(ObjectType, UserQueries, ProductQueries, ResourceQueries):
    pass


class Mutation(UserMutations, ProductMutations, ResourceMutations, ObjectType):
    # authenticate the User with its username and password to obtain the JSON Web token.
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()

    # confirm that the token is valid, passing it as an argument.
    verify_token = graphql_jwt.Verify.Field()

    # obtain a new token within the renewed expiration time for non-expired tokens, if they are enabled to expire.
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(
    types=types,
    # query=Query,
    mutation=Mutation
)
