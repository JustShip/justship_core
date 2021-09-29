"""Test Environmental settings are handled properly."""

# from unittest.mock import patch
# from django.test import TestCase
# from unittest import skip
# we have to use tools outside of django, because when it's initialized
# it's too late to change environment variables
from unittest import TestCase, main


class DebugSettingTest(TestCase):
    """Test if setting DEBUG is handled properly."""

    _variants = {
        True: ('Yes', 'YES', 'Y', 'TRUE', 'tRUE', 'true', 'On'),
        False: ('No', 'nO', 'N', 'n', 'false', 'False', 'off', 'oFF'),
    }
    env_var_debug = 'DEBUG'

    def test_debug_setting(self):
        """Check if config accepts environment variable DEBUG and sets it."""


if __name__ == '__main__':
    main()
