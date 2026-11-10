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

        if char == "/" and i + 1 < n and text[i + 1] == "*":  # игнор комментариев /*
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
            num = float(num_str) if "." in num_str else int(num_str)

            tokens.append(("NUMBER", num))
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

    def consume(self, *expected_types, expected_val=None):
        """Берет текущий токен и сдвигает указатель вперед"""
        token = self.peek()
        if not token:
            raise SyntaxError("Неожиданный конец файла")

        if expected_types and token[0] not in expected_types:
            raise SyntaxError(f"Ожидался тип {' или '.join(expected_types)}, получен {token[0]} (значение: {token[1]})")

        if expected_val and token[1] != expected_val:
            raise SyntaxError(f"Ожидался символ '{expected_val}', получен '{token[1]}'")

        self.pos += 1
        return token

    def parse(self):
        """Парсер, от него запускаем функцию для сборки типа данных"""
        token = self.peek()
        if not token:
            raise SyntaxError("Ожидалось значение, но файл закончился")

        if token[0] in ("STRING", "NUMBER", "BOOL"):
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

    def parse_array_values(self, symbol):
        """Вспомогательная функция для парсинга объектов типа массивов"""
        arr = []
        while self.peek() and self.peek()[1] != symbol:
            arr.append(self.parse())
            if self.peek() and self.peek()[1] == ",":
                self.consume()

        self.consume(expected_val=symbol)
        return arr

    def parse_key_values(self, symbol, *types):
        """Вспомогательная функция для парсинга объектов типа словарей"""
        d = {}
        while self.peek() and self.peek()[1] != symbol:
            key = self.consume(*types)[1]
            self.consume(expected_val=":")
            d[key] = self.parse()
            if self.peek() and self.peek()[1] == ",":
                self.consume()

        self.consume(expected_val=symbol)
        return d

    def parse_array(self):
        self.consume()
        return self.parse_array_values("]")

    def parse_dict(self):
        self.consume()
        return self.parse_key_values("}", "NAME", "STRING")

    def parse_tuple(self):
        self.consume()

        # пустой кортеж
        if self.peek() and self.peek()[1] == ")":
            self.consume()
            return []

        # если key: value -> это структура, иначе это кортеж
        if self.peek()[0] == "NAME" and self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][1] == ":":
            return self.parse_key_values(")", "NAME")

        return self.parse_array_values(")")

    def parse_struct(self):
        name = self.consume()[1]
        self.consume()
        d = self.parse_key_values(")", "NAME")
        return {name: d}


def from_ron(text):
    tokens = tokenize(text)
    parser = Parser(tokens)
    return parser.parse()
