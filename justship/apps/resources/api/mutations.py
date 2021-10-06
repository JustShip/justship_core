import graphene
from graphql import GraphQLError

from justship.apps.resources import models
from . import types


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String(required=False)

    status = graphene.Boolean()
    category = graphene.Field(types.CategoryType)

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
            return CreateCategory(status=is_created, category=category)
        else:
            return GraphQLError('You must be staff')


class UpdateCategory(graphene.Mutation):
    class Arguments:
        category_id = graphene.Int()
        name = graphene.String(required=False)
        description = graphene.String(required=False)

    category = graphene.Field(types.CategoryType)

    @staticmethod
    def mutate(root, info, category_id, name=None, description=None):
        """
        Update the category and returns it. Only staff can add categories
        :param root:
        :param info:
        :param category_id: category's id
        :param name: new category's name
        :param description: new category's description
        :return: the updated category
        """
        user = info.context.user
        if user.is_staff:
            category = models.Category.objects.filter(id=category_id).first()
            if category:
                category.name = name or category.name
                category.description = description or category.description
                category.save()
                return UpdateCategory(category=category)
            else:
                return UpdateCategory(category=None)
        else:
            return GraphQLError('You must be staff')


class DeleteCategory(graphene.Mutation):
    class Arguments:
        category_id = graphene.Int()

    status = graphene.Boolean()

    @staticmethod
    def mutate(root, info, category_id):
        if info.context.user.is_staff:
            category = models.Category.objects.filter(id=category_id).first()
            if category:
                category.delete()
                return DeleteCategory(status=True)
            else:
                return DeleteCategory(status=False)
        else:
            return GraphQLError('You must be staff')


class CreateResource(graphene.Mutation):
    class Arguments:
        url = graphene.String()
        category = graphene.List(graphene.Int, required=False)

    resource = graphene.Field(types.ResourceType)

    @staticmethod
    def mutate(root, info, url, category=None):
        """
        Create a resource. Only for logged users
        :param root:
        :param info:
        :param url: resource's url
        :param category: resource's categories
        :return: a new resource
        """
        user = info.context.user
        if user.is_authenticated:
            resource = models.Resource(url=url, creator=user)
            resource.save()
            categories = models.Category.objects.filter(pk__in=category)
            resource.category.add(*categories)
            return CreateResource(resource=resource)
        else:
            return GraphQLError('You must be authenticated')


class ResourceMutations:
    add_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()
    add_resource = CreateResource.Field()
