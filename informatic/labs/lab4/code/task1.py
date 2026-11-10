import sys

from ml.ron import from_ron
from ml.yaml import to_yaml


def run(file_name):
    input_path = f"../data/{file_name}/{file_name}.ron"
    output_path = f"../data/{file_name}/{file_name}.yaml"

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            ron_text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл {input_path} не найден")
        return None

    obj = from_ron(ron_text)
    yaml_text = to_yaml(obj)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(yaml_text)

    return yaml_text


if __name__ == "__main__":
    file_name = sys.argv[1] if len(sys.argv) > 1 else "schedule"
    result = run(file_name)
    print(result)
