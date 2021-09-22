from django.test import TestCase
from django.urls import reverse


class ErrorViewTests(TestCase):
    def test_get(self):
        """Try to display error page"""
        with self.assertRaises(Exception):
            self.client.get(reverse('core:error'))
        with self.assertRaisesMessage(Exception, 'Error view'):
            self.client.get(reverse('core:error'))
