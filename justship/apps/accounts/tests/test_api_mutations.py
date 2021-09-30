import json
from graphene_django.utils.testing import GraphQLTestCase
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer


class ApiMutationTests(GraphQLTestCase):
    def setUp(self) -> None:
        self.user1 = mixer.blend(get_user_model())

    def test_update_username_with_anonymous_user(self) -> None:
        """
        Anonymous user try to update the username
        :return: None
        """
        response = self.query(
            '''
            mutation updateUsername($username: String) {
                updateUsername(username: $username) {
                    ok
                }
            }
            ''',
            op_name='updateUsername',
            variables={'username': 'ragnarok'}
        )
        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)
        self.assertEqual(content['data']['updateUsername']['ok'], False)
