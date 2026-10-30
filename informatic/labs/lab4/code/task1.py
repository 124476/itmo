import sys

from ml.ron import encode


def run(file_name):
    input_path = f"../data/{file_name}/{file_name}.ron"
    output_path = f"../data/{file_name}/{file_name}.bin"

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл {input_path} не найден")
        return None

    bs = encode(text)
    with open(output_path, "wb") as f:
        f.write(bs)

    return bs


if __name__ == "__main__":
    file_name = sys.argv[1] if len(sys.argv) > 1 else "schedule"
    bs = run(file_name)
    print(bs)
