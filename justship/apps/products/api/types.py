from graphene_django import DjangoObjectType

from ..models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        only_fields = (
            'id',
            'name',
            'description',
            'link',
            'state',
            'tags',
            'socials',
            'logo_url',
            'logo_thumbnail_url'
        )


product_types = [
    ProductType
]
