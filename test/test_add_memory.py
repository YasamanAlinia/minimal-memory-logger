from memory_journal.main import add_memory
from unittest.mock import patch
from io import StringIO
import unittest


class TestAddMemory(unittest.TestCase):
    def setUp(self):
        self.mock_input = patch('builtins.input', return_value="""This is a sample text that is intentionally written to 
                                contain more than 200 characters,
                                in order to demonstrate or test character limits in forms, 
                                applications, or validation systems where
                                 a minimum length requirement is needed for submission.""").start()
        self.mock_save = patch("memory_journal.main.save_memory").start()
        self.mock_stdout = patch("sys.stdout", new_callable=StringIO).start()

    def test_add_memory_action(self):
        add_memory()

        self.mock_input.assert_called_once()

        args, kwargs = self.mock_save.call_args
        memory_dict = args[0]
        self.assertIn('text', memory_dict)
        self.assertIn('date', memory_dict)
        self.assertTrue(len(memory_dict['text']) >= 200)
        
        output = self.mock_stdout.getvalue().strip()
        self.assertIn("--memory made successfully!--", output)
        
    def tearDown(self):
        patch.stopall()

    