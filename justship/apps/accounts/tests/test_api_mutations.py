import json
from graphene_django.utils.testing import GraphQLTestCase
from graphql_jwt.testcases import JSONWebTokenTestCase
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer


class ApiMutationTests(JSONWebTokenTestCase):
    def setUp(self) -> None:
        self.user1 = mixer.blend(get_user_model())
        self.user2 = mixer.blend(get_user_model())

    def test_update_username_with_authenticated_user(self) -> None:
        """
        Authenticated user try to update his/her username
        :return: None
        """
        self.client.authenticate(self.user2)
        query = '''
            mutation updateUsername($username: String) {
                updateUsername(username: $username) {
                    ok
                }
            }
            '''
        variables = {
            "username": 'ragnarok',
        }
        response = self.client.execute(query, variables)
        self.assertTrue(response.data.get('updateUsername').get('ok'))

    def test_update_username_with_anonymous_user(self) -> None:
        """
        Anonymous user try to update the username
        :return: None
        """
        query = '''
            mutation updateUsername($username: String) {
                updateUsername(username: $username) {
                    ok
                }
            }
            '''
        variables = {'username': 'ragnarok'}
        response = self.client.execute(query, variables)
        errors = response.errors

        # This validates the status code and if you get errors
        self.assertIsNotNone(response.errors)
        self.assertEqual('You do not have permission to perform this action', errors[0].message)
        # self.assertResponseHasErrors(response)
        self.assertIsNone(response.data['updateUsername'])
