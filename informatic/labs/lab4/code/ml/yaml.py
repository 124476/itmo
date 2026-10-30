class BinaryDecoder:
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def decode(self):
        return self.read_obj()

    def read_obj(self):
        type_tag = self.data[self.pos]
        self.pos += 1

        if type_tag == 0x00:
            return None

        if type_tag == 0x01:
            val = bool(self.data[self.pos])
            self.pos += 1
            return val

        if type_tag == 0x02:
            val = int.from_bytes(self.data[self.pos:self.pos + 8], byteorder="big", signed=True)
            self.pos += 8
            return val

        if type_tag == 0x03:
            length = int.from_bytes(self.data[self.pos:self.pos + 4], byteorder="big")
            self.pos += 4
            val = float(self.data[self.pos:self.pos + length].decode("utf-8"))
            self.pos += length
            return val

        if type_tag == 0x04:
            length = int.from_bytes(self.data[self.pos:self.pos + 4], byteorder="big")
            self.pos += 4
            val = self.data[self.pos:self.pos + length].decode("utf-8")
            self.pos += length
            return val

        if type_tag == 0x05:
            length = int.from_bytes(self.data[self.pos:self.pos + 4], byteorder="big")
            self.pos += 4
            return [self.read_obj() for _ in range(length)]

        if type_tag == 0x06:
            length = int.from_bytes(self.data[self.pos:self.pos + 4], byteorder="big")
            self.pos += 4
            return {self.read_obj(): self.read_obj() for _ in range(length)}

        raise ValueError(f"Неизвестный маркер типа: {type_tag}")


def to_yaml(obj, indent=0):
    spacing = " " * indent

    if isinstance(obj, dict):
        if not obj:
            return "{}"

        lines = []
        for k, v in obj.items():
            if isinstance(v, (dict, list)) and v:
                lines.append(f"{spacing}{k}:")
                lines.append(to_yaml(v, indent + 2))
            else:
                lines.append(f"{spacing}{k}: {yaml_val(v)}")

        return "\n".join(lines)

    elif isinstance(obj, list):
        if not obj:
            return "[]"

        lines = []
        for item in obj:
            if isinstance(item, (dict, list)) and item:
                item_str = to_yaml(item, indent + 2)
                lines.append(f"{spacing}- {item_str[indent + 2:]}")
            else:
                lines.append(f"{spacing}- {yaml_val(item)}")

        return "\n".join(lines)

    return yaml_val(obj)


def yaml_val(v):
    if isinstance(v, str):
        safe_v = v.replace('"', '\\"')
        return f'"{safe_v}"'

    if isinstance(v, bool):
        return "true" if v else "false"

    return str(v)