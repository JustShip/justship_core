import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from .types import TagType
from justship.apps.core.models import Tag


class CreateTag(graphene.Mutation):
    tag = graphene.Field(TagType)

    class Arguments():
        name = graphene.String()

    @staticmethod
    @login_required
    def mutate(root, info, name):
        try:
            tag = Tag(name=name)
            tag.save()
            return CreateTag(tag=tag)
        except:
            return GraphQLError("Tag already exists")


class CoreMutations(graphene.ObjectType):
    create_tag = CreateTag.Field()
