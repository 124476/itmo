import sys

from ml.yaml import BinaryDecoder
from ml.xml import to_xml


def run(file_name):
    input_path = f"../data/{file_name}/{file_name}.bin"
    output_path = f"../data/{file_name}/{file_name}.xml"

    try:
        with open(input_path, "rb") as f:
            bs = f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл {input_path} не найден")
        return None

    decoder = BinaryDecoder(bs)
    obj = decoder.decode()
    xml_text = to_xml(obj)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(xml_text)

    return xml_text


if __name__ == "__main__":
    file_name = sys.argv[1] if len(sys.argv) > 1 else "schedule"
    result = run(file_name)
    print(result)
