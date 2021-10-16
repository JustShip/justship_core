import graphene
from .types import ProductType
from .. import models


class ProductQueries:
    product = graphene.Field(ProductType, product_id=graphene.Int())

    def resolve_product(self, info, product_id):
        return models.Product.objects.get(pk=product_id)
