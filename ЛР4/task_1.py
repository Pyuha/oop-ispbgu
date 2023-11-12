import json


def task() -> float:
    file_name = 'input.json'
    with open(file_name, 'r') as input_f:
        json_data = json.load(input_f)
        sum_multiplying = sum([item.get('score') * item.get('weight') for item in json_data])
        return round(sum_multiplying, 3)

print(task())
