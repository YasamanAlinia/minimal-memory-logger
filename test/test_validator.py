from memory_journal.memory_validator import text_validator
from memory_journal.custom_error import TextTooShortError
import unittest

class TestTextValidator(unittest.TestCase):
    def setUp(self):
        self.short_text = "This is a very short input that is less than 200 characters"

    def test_text_validator_raises_error_for_short_text(self):
       with self.assertRaises(TextTooShortError):
           text_validator(self.short_text)

    def tearDown(self):
        self.short_text = None