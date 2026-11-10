import sys
import pyron
import yaml


def clean_data(obj):
    if isinstance(obj, tuple):
        # Если это кортеж, превращаем его в список
        return [clean_data(i) for i in obj]

    if isinstance(obj, list) and obj:
        return [clean_data(item) for item in obj]

    if isinstance(obj, dict):
        if "!__name__" in obj:
            if len(obj) == 1:
                return obj["!__name__"]

            obj = {
                obj["!__name__"]: {k: clean_data(v) for k, v in obj.items() if k != "!__name__"}
            }
            return obj

        return {k: clean_data(v) for k, v in obj.items()}

    return obj


def run(file_name):
    input_path = f"../data/{file_name}/{file_name}.ron"
    output_path = f"../data/{file_name}/{file_name}_lib.yaml"

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            ron_text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл {input_path} не найден")
        return None

    obj = pyron.loads(ron_text, preserve_class_names=True)
    obj = clean_data(obj)

    yaml_text = yaml.dump(obj, allow_unicode=True, sort_keys=False, default_flow_style=False)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(yaml_text)

    return yaml_text


if __name__ == "__main__":
    file_name = sys.argv[1] if len(sys.argv) > 1 else "schedule"
    result = run(file_name)
    print(result)
