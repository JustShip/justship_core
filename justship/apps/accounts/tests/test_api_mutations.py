from django.test import TestCase
from graphene.test import Client

from justship.apps.api.schema import schema


class ApiMutationTests(TestCase):
    def test_update_message(self):
        """
        Test example
        :return:
        """
        client = Client(schema=schema)
        # executed = client.execute('''{ hey }''')
        # assert executed == {
        #     'data': {
        #         'hey': 'hello!'
        #     }
        # }
        self.assertTrue(True)
