def tokenize(text):
    tokens = []

    i = 0
    n = len(text)

    while i < n:
        char = text[i]

        if char.isspace():  # игнор пробельных символов
            i += 1
            continue

        if char == "/" and i + 1 < n and text[i + 1] == "/":  # игнор комментариев //
            while i < n and text[i] != '\n':
                i += 1

            continue

        if char == "/" and text[i + 1] == "*":  # игнор комментариев /*
            count_comm = 1
            i += 2

            while i + 1 < n and count_comm > 0:
                if text[i:i + 2] == "/*":
                    count_comm += 1
                    i += 1

                if text[i:i + 2] == "*/":
                    count_comm -= 1
                    i += 1

                i += 1

            continue

        if char == '"':  # чтение стринговых типов
            i += 1
            string_val = ""
            while i < n:
                if text[i] == "\\" and i + 1 < n:
                    string_val += text[i + 1]
                    i += 2
                    continue
                elif text[i] == '"':
                    break

                string_val += text[i]
                i += 1

            tokens.append(("STRING", string_val))
            i += 1
            continue

        if char.isalpha() or char == "_":  # чтение названий
            start = i
            while i < n and (text[i].isalnum() or text[i] == "_"):
                i += 1

            word = text[start:i]

            if word in ["true", "false"]:
                tokens.append(("BOOL", word == "true"))
                continue

            tokens.append(("NAME", word))
            continue

        if char.isdigit() or (char == "-" and i + 1 < n and text[i + 1].isdigit()):  # чтение чисел
            start = i
            i += 1
            while i < n and (text[i].isdigit() or text[i] == "."):
                i += 1
            num_str = text[start:i]

            if "." in num_str:
                tokens.append(("FLOAT", float(num_str)))
                continue

            tokens.append(("INT", int(num_str)))
            continue

        if char in "()[]{}:,":
            tokens.append(("SYMBOL", char))
            i += 1
            continue

        raise SyntaxError(f"Синтаксическая ошибка: неизвестный символ '{char}' на позиции {i}")

    return tokens


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]

        return None

    def consume(self, expected_type=None, expected_val=None):
        """Берет текущий токен и сдвигает указатель вперед"""
        token = self.peek()
        if not token:
            raise SyntaxError("Неожиданный конец файла")

        if expected_type and token[0] != expected_type:
            raise SyntaxError(f"Ожидался тип {expected_type}, получен {token[0]} (значение: {token[1]})")

        if expected_val and token[1] != expected_val:
            raise SyntaxError(f"Ожидался символ '{expected_val}', получен '{token[1]}'")

        self.pos += 1
        return token

    def parse(self):
        """Парсер, от него запускаем функцию для сборки типа данных"""
        token = self.peek()
        if not token:
            raise SyntaxError("Ожидалось значение, но файл закончился")

        if token[0] in ("STRING", "INT", "FLOAT", "BOOL"):
            return self.consume()[1]

        if token[1] == "[":
            return self.parse_array()

        if token[1] == "{":
            return self.parse_dict()

        if token[1] == "(":
            return self.parse_tuple()

        if token[0] == "NAME":
            # Если это слово, за которым идет скобка - значит это структура, иначе это ключ или значение
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][1] == "(":
                return self.parse_struct()

            return self.consume()[1]

        raise SyntaxError(f"Неожиданный токен: {token}")

    def parse_array(self):
        """Парсит массивы"""
        self.consume()
        arr = []
        while self.peek() and self.peek()[1] != "]":
            arr.append(self.parse())
            if self.peek() and self.peek()[1] == ",":
                self.consume()

        self.consume(expected_val="]")
        return arr

    def parse_dict(self):
        """Парсит словари"""
        self.consume()
        d = {}
        while self.peek() and self.peek()[1] != "}":
            key = self.consume(expected_type='STRING')[1]
            self.consume(expected_val=":")
            d[key] = self.parse()
            if self.peek() and self.peek()[1] == ",":
                self.consume()

        self.consume(expected_val="}")
        return d

    def parse_tuple(self):
        self.consume()

        # пустой кортеж
        if self.peek() and self.peek()[1] == ")":
            self.consume()
            return []

        # если key: value -> это структура, иначе это кортеж
        if self.peek()[0] == "NAME" and self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][1] == ":":
            d = {}
            while self.peek() and self.peek()[1] != ")":
                key = self.consume(expected_type="NAME")[1]
                self.consume(expected_val=":")
                d[key] = self.parse()
                if self.peek() and self.peek()[1] == ",":
                    self.consume()

            self.consume(expected_val=")")
            return d

        arr = []
        while self.peek() and self.peek()[1] != ")":
            arr.append(self.parse())
            if self.peek() and self.peek()[1] == ",":
                self.consume()

        self.consume(expected_val=")")
        return arr

    def parse_struct(self):
        """Парсит структуры"""
        name = self.consume(expected_type='NAME')[1]  # Читаем имя (Schedule, Class...)
        self.consume(expected_val='(')
        d = {}
        while self.peek() and self.peek()[1] != ")":
            key = self.consume(expected_type='NAME')[1]
            self.consume(expected_val=":")
            d[key] = self.parse()
            while self.peek() and self.peek()[1] == ",":
                self.consume()

        self.consume(expected_val=")")
        return {name: d}


def encode_binary(obj):
    if obj is None:
        return b'\x00'

    if isinstance(obj, bool):
        # \x01 - true, \x00 - false
        return b'\x01\x01' if obj else b'\x01\x00'

    if isinstance(obj, int):
        # 8 байта на целое число, signed - для отрицательных чисел
        # 8 байт на хранение 2^63 (максимально по модулю число)
        return b'\x02' + obj.to_bytes(8, byteorder='big', signed=True)

    if isinstance(obj, float):
        # числа с плавающей запятой
        b = str(obj).encode('utf-8')
        return b'\x03' + len(b).to_bytes(4, byteorder='big') + b

    if isinstance(obj, str):
        b = obj.encode('utf-8')
        # 4 байта на длину (2^32) + сами байты строки
        return b'\x04' + len(b).to_bytes(4, byteorder='big') + b

    if isinstance(obj, list):
        res = b'\x05' + len(obj).to_bytes(4, byteorder='big')
        for item in obj:
            res += encode_binary(item)

        return res

    if isinstance(obj, dict):
        res = b'\x06' + len(obj).to_bytes(4, byteorder='big')
        for k, v in obj.items():
            res += encode_binary(k) + encode_binary(v)

        return res

    raise TypeError(f"Неподдерживаемый тип: {type(obj)}")


def encode(text):
    tokens = tokenize(text)
    parser = Parser(tokens)
    d = parser.parse()
    bs = encode_binary(d)
    return bs
