# cookbook/schema.py
import graphene
from graphene_django import DjangoObjectType

from justshipto_core.accounts.models import Profile


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("id", "first_name", "last_name", "username")


class Query(graphene.ObjectType):
    all_profiles = graphene.List(ProfileType)
    profile_by_first_name = graphene.Field(ProfileType, first_name=graphene.String(required=True))

    def resolve_all_profiles(root, info):
        # We can easily optimize query count in the resolve method
        return Profile.objects.all()

    def resolve_profile_by_first_name(root, info, first_name):
        try:
            return Profile.objects.get(first_name=first_name)
        except Profile.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
