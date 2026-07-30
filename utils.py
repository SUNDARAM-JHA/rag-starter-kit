import os
import json
from datetime import datetime


def save_prompt(name, prompt):
    os.makedirs("saved_prompts", exist_ok=True)

    filename = f"saved_prompts/{name}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(prompt)

    return filename


def load_prompt(name):
    filename = f"saved_prompts/{name}.txt"

    if not os.path.exists(filename):
        return None

    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_json(filename):
    if not os.path.exists(filename):
        return {}

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    print("Current Time:", timestamp())
