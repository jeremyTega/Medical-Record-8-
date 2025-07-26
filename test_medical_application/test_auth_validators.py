import unittest
from validators.auth_validator import *


class MyTestCase(unittest.TestCase):
    def test_validate_non_empty_with_valid_input(self):
        try:
            validate_non_empty("Name", "Jeremy")
        except ValueError:
            self.fail("validate_non_empty() raised ValueError unexpectedly!")

    def test_validate_non_empty_with_none(self):
        with self.assertRaises(ValueError) as context:
            validate_non_empty("Username", None)
        self.assertIn("Username cannot be empty", str(context.exception))

    def test_validate_non_empty_with_blank_string(self):
        with self.assertRaises(ValueError) as context:
            validate_non_empty("Field", "   ")
        self.assertIn("Field cannot be empty", str(context.exception))


    def test_validate_email_format_with_valid_email(self):
        try:
            validate_email_format("tega@example.com")
        except ValueError:
            self.fail("validate_email_format() raised ValueError unexpectedly!")

    def test_validate_email_format_with_invalid_email(self):
        with self.assertRaises(ValueError) as context:
            validate_email_format("invalid-email")
        self.assertIn("Invalid email format", str(context.exception))


    def test_validate_password_strength_with_strong_password(self):
        try:
            validate_password_strength("strongPass123")
        except ValueError:
            self.fail("validate_password_strength() raised ValueError unexpectedly!")

    def test_validate_password_strength_with_short_password(self):
        with self.assertRaises(ValueError) as context:
            validate_password_strength("123")
        self.assertIn("Password must be at least 6 characters long", str(context.exception))



if __name__ == '__main__':
    unittest.main()
