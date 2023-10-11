import json
import random

def generate_nested_json(depth=5):
    if depth == 0:
        return random.randint(0, 1000)

    key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=20))
    value = generate_nested_json(depth-1)
    
    return {key: value}

data = generate_nested_json()
print(json.dumps(data))
