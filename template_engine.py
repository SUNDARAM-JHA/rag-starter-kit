import re


class PromptTemplate:
    """
    Simple template engine for replacing variables like:
    {{CODE}}
    {{ERROR}}
    {{LANGUAGE}}
    """

    def __init__(self, template):
        self.template = template

    def render(self, **kwargs):
        output = self.template

        for key, value in kwargs.items():
            output = output.replace(f"{{{{{key}}}}}", str(value))

        return output

    def variables(self):
        return sorted(set(re.findall(r"\{\{(.*?)\}\}", self.template)))


if __name__ == "__main__":
    template = """
Review the following {{LANGUAGE}} code.

Code:
{{CODE}}
"""

    engine = PromptTemplate(template)

    print("Variables:", engine.variables())

    print(
        engine.render(
            LANGUAGE="Python",
            CODE="print('Hello World')"
        )
    )
