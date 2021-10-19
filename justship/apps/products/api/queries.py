import graphene
from django.db.models import Q
from graphql import GraphQLError

from .types import ProductType
from .. import models


class ProductQueries:
    product = graphene.Field(ProductType, product_id=graphene.Int(), product_name=graphene.String())
    search_products = graphene.List(ProductType, product_name=graphene.String())

    def resolve_search_products(self, info, product_name):
        try:
            search_results = models.Product.objects.filter(name__icontains=product_name)
            if not search_results:
                raise GraphQLError("Empty search")
            return search_results
        except:
            return GraphQLError('Object does not exists')

    def resolve_product(self, info, product_id=None, product_name=None):
        try:
            if product_id or product_name:
                product = models.Product.objects.get(Q(pk=product_id) | Q(name__iexact=product_name))
                return product
        except:
            return GraphQLError('Object does not exists')
