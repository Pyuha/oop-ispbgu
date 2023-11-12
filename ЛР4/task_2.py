import csv
import json


input_filename = "input.csv"
output_filename = "output.json"


def task() -> None:
    with open(input_filename) as input_f:
        rows = [row for row in csv.DictReader(input_f)]

    with open(output_filename, 'w') as output_f:
        json.dump(rows, output_f, indent=4)


if __name__ == '__main__':
    task()

    with open(output_filename) as output_f:
        for line in output_f:
            print(line, end="")
