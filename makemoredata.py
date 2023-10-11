import json
import random

WORDS = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yellowfruit", "zucchini"]

def generate_random_text():
    lines = random.randint(1, 5)
    return '\n'.join(''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=40)) for _ in range(lines))

def generate_nested_json(depth=10):
    if depth == 0:
        if random.choice([True, False]):
            return generate_random_text()
        return random.randint(0, 1000)

    structure_type = random.choice(['dict', 'list'])

    if structure_type == 'dict':
        key = random.choice(WORDS)
        value = generate_nested_json(depth-1)
        return {key: value}
    else:
        length = random.randint(1, 5)
        return [generate_nested_json(depth-1) for _ in range(length)]

data = generate_nested_json()
print(json.dumps(data))
