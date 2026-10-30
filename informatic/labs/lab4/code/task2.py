import sys

from ml.ron import encode
from ml.yaml import BinaryDecoder, to_yaml


def run(file_name):
    input_path = f"../data/{file_name}/{file_name}.ron"
    bin_path = f"../data/{file_name}/{file_name}.bin"
    yaml_path = f"../data/{file_name}/{file_name}.yaml"

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            ron_text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл {input_path} не найден")
        return None

    bs = encode(ron_text)
    with open(bin_path, "wb") as f:
        f.write(bs)

    with open(bin_path, "rb") as f:
        read_bs = f.read()

    decoder = BinaryDecoder(read_bs)
    data = decoder.decode()
    yaml_text = to_yaml(data)

    with open(yaml_path, "w", encoding="utf-8") as f:
        f.write(yaml_text)

    return yaml_text


if __name__ == "__main__":
    file_name = sys.argv[1] if len(sys.argv) > 1 else "schedule"
    result = run(file_name)
    print(result)
