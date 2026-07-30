"""
AI Prompt Generator
A simple utility for generating reusable prompts.
"""

class PromptGenerator:

    def code_review(self, code):
        return f"""
Review the following code.

Check for:
- Bugs
- Performance
- Security
- Best Practices

Code:
{code}
"""

    def bug_fix(self, error):
        return f"""
Analyze this error.

Explain:
1. Cause
2. Fix
3. Prevention

Error:
{error}
"""

    def documentation(self, code):
        return f"""
Generate professional documentation for:

{code}
"""

    def unit_tests(self, code):
        return f"""
Generate comprehensive unit tests for:

{code}
"""

    def refactor(self, code):
        return f"""
Refactor this code without changing functionality:

{code}
"""


if __name__ == "__main__":
    generator = PromptGenerator()

    sample = generator.code_review("print('Hello World')")
    print(sample)
