from prompt_generator import PromptGenerator
from utils import save_prompt

generator = PromptGenerator()

print("=" * 40)
print("AI Developer Toolkit")
print("=" * 40)

while True:
    print("\nChoose an option:")
    print("1. Code Review Prompt")
    print("2. Bug Fix Prompt")
    print("3. Documentation Prompt")
    print("4. Unit Test Prompt")
    print("5. Refactor Prompt")
    print("6. Exit")

    choice = input("\nEnter choice: ")

    if choice == "6":
        print("Goodbye!")
        break

    text = input("\nPaste your code or error:\n")

    if choice == "1":
        result = generator.code_review(text)
        filename = "code_review"

    elif choice == "2":
        result = generator.bug_fix(text)
        filename = "bug_fix"

    elif choice == "3":
        result = generator.documentation(text)
        filename = "documentation"

    elif choice == "4":
        result = generator.unit_tests(text)
        filename = "unit_tests"

    elif choice == "5":
        result = generator.refactor(text)
        filename = "refactor"

    else:
        print("Invalid option.")
        continue

    print("\nGenerated Prompt:\n")
    print(result)

    save = input("\nSave this prompt? (y/n): ").lower()

    if save == "y":
        path = save_prompt(filename, result)
        print(f"Saved to {path}")
