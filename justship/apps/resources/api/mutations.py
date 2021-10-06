import graphene
from graphql import GraphQLError

from justship.apps.resources import models


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String(required=False)

    status = graphene.Boolean()

    @staticmethod
    def mutate(root, info, name, description=None):
        """
        Add category if doesn't exists. Only staff can add categories
        :param root:
        :param info:
        :param name: category's name
        :param description: category's description. Not required
        :return: a boolean
        """
        if info.context.user.is_staff:
            # create only if doesn't exists
            category, is_created = models.Category.objects.get_or_create(name=name, description=description)
            return CreateCategory(status=is_created)
        else:
            return GraphQLError('You must be staff')


class ResourceMutations:
    add_category = CreateCategory.Field()
