import unittest

from prompt_generator import PromptGenerator


class TestPromptGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = PromptGenerator()

    def test_code_review(self):
        result = self.generator.code_review("print('Hello')")
        self.assertIn("Review the following code", result)
        self.assertIn("print('Hello')", result)

    def test_bug_fix(self):
        result = self.generator.bug_fix("NameError")
        self.assertIn("NameError", result)

    def test_documentation(self):
        result = self.generator.documentation("def hello(): pass")
        self.assertIn("Generate professional documentation", result)

    def test_unit_tests(self):
        result = self.generator.unit_tests("def add(a, b): return a + b")
        self.assertIn("Generate comprehensive unit tests", result)

    def test_refactor(self):
        result = self.generator.refactor("x=1")
        self.assertIn("Refactor this code", result)


if __name__ == "__main__":
    unittest.main()
