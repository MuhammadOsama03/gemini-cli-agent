import unittest
from unittest.mock import patch

import tools


class CalculatorTests(unittest.TestCase):
    def test_supported_operations(self):
        self.assertEqual(tools.calculator("add", 2, 3), "5")
        self.assertEqual(tools.calculator("subtract", 7, 4), "3")
        self.assertEqual(tools.calculator("multiply", 2.5, 4), "10.0")
        self.assertEqual(tools.calculator("divide", 9, 3), "3.0")

    def test_rejects_division_by_zero_and_unknown_operation(self):
        self.assertEqual(tools.calculator("divide", 1, 0), "Error: cannot divide by zero")
        self.assertIn("unknown operation", tools.calculator("power", 2, 8))


class SearchTests(unittest.TestCase):
    @patch("tools.DDGS")
    def test_formats_search_results(self, ddgs_cls):
        ddgs_cls.return_value.text.return_value = [
            {"title": "Example", "body": "Useful result"},
            {"title": "Second", "body": "Another result"},
        ]
        output = tools.web_search("example query")
        self.assertIn("- Example: Useful result", output)
        self.assertIn("- Second: Another result", output)

    @patch("tools.DDGS")
    def test_handles_empty_results_and_provider_errors(self, ddgs_cls):
        ddgs_cls.return_value.text.return_value = []
        self.assertEqual(tools.web_search("nothing"), "No results found.")
        ddgs_cls.return_value.text.side_effect = RuntimeError("offline")
        self.assertIn("Search error: offline", tools.web_search("test"))


if __name__ == "__main__":
    unittest.main()
