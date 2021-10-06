import graphene


class CreateResource(graphene.Mutation):
    class Arguments:
        pass

    @staticmethod
    def mutate(root, info, url):
        pass


class ResourceMutations:
    add_resource = CreateResource.Field()
