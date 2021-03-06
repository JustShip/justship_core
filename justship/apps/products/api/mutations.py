import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required

from justship.apps.core.models import Tag
from justship.apps.products.models import Product
from .types import ProductType


class CreateProduct(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        name = graphene.String()
        description = graphene.String(required=False)
        link = graphene.String(required=False)
        state = graphene.String()
        tags = graphene.List(graphene.String, required=False)

    @staticmethod
    @login_required
    def mutate(root, info, name, state, description=None, link=None, tags=None):
        user = info.context.user

        try:
            new_product = Product(name=name,
                                  state=state,
                                  description=description,
                                  link=link,
                                  owner=user
                                  )
            new_product.save()
            if tags:
                tags_list = Tag.objects.filter(name__in=tags)
                new_product.tags.set(*tags_list)
                new_product.save()
            return CreateProduct(product=new_product)

        except:
            return GraphQLError("Object with same name already exists")


class DeleteProduct(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments():
        product_id = graphene.Int()

    @staticmethod
    @login_required
    def mutate(root, info, product_id):
        user = info.context.user
        try:
            product = Product.objects.get(pk=product_id)
            if user == product.owner:
                product.delete()
                return DeleteProduct(ok=True)
            else:
                return GraphQLError("You must be product's owner")
        except:
            return GraphQLError("Product doesn't exists")


class UpdateProduct(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        product_id = graphene.Int()
        name = graphene.String(required=False)
        description = graphene.String(required=False)
        link = graphene.String(required=False)
        state = graphene.String(required=False)
        tags = graphene.List(graphene.String, required=False)

    @staticmethod
    @login_required
    def mutate(root, info, product_id, name=None, description=None, link=None, state=None, tags=None):
        user = info.context.user
        try:
            product = Product.objects.get(pk=product_id)
            if user == product.owner:
                product.name = name or product.name
                product.description = description or product.description
                product.link = link or product.link
                product.state = state or product.state
                product.save()
                if tags:
                    tags_list = Tag.objects.filter(name__in=tags)
                    product.tags.set(tags_list)
                    product.save()
                return UpdateProduct(product=product)
            else:
                return GraphQLError("You must be the product's owner")
        except:
            return GraphQLError("Object doesn't exists")


class ProductMutations:
    create_product = CreateProduct.Field()
    delete_product = DeleteProduct.Field()
    update_product = UpdateProduct.Field()
