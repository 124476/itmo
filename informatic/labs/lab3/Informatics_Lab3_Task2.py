# Author = Krahmalnikov Ilya Artemovich
# Group = P3119
# Date = 09.10.2026

import re

def func(text, group):
    reg_full = (r"[^А-ЯЁа-яё]*"
                r"([А-ЯЁ][а-яё]*(?:-[А-ЯЁ][а-яё]+)?)"
                r"\s*"
                r"([А-ЯЁ][а-яё]*)\.?"
                r".*"
                r"([А-ЯЁ][а-яё]*)\.?"
                r"[^А-ЯЁа-яё]*")
    reg_no_last_name = (r"[^А-ЯЁа-яё]*"
                        r"([А-ЯЁ][а-яё]*(?:-[А-ЯЁ][а-яё]+)?)"
                        r"\s*"
                        r"([А-ЯЁ][а-яё]*)\.?"
                        r"[^А-ЯЁа-яё]*")

    ans = []
    for line in text.split("\n"):
        if group not in line:
            ans.append(line)
            continue

        m = re.match(reg_no_last_name, line)
        if not m:
            ans.append(line)
            continue

        m_full = re.match(reg_full, line)
        if m_full:
            m = m_full

        groups = m.groups()

        if len(groups) == 2 and groups[0][0] == groups[1][0]:
            continue

        if len(groups) == 3 and groups[0][0] == groups[1][0] == groups[2][0]:
            continue

        ans.append(line)

    return "\n".join(ans)

def test_1():
    group = "P0000"
    text = """Петров П.П. P0000
Анищенко А.А. P33113
Примеров Е.В. P0000
Иванов И.И. P0000"""

    expected = "Анищенко А.А. P33113\nПримеров Е.В. P0000"
    result = func(text, group)
    assert expected == result

def test_2():
    group = "P0000"
    text = """Голованова-Иванова П. P0000
Анищенко А.А. P33113
Примеров Е.В. P0000
Иванов И.И. P0000"""

    expected = "Голованова-Иванова П. P0000\nАнищенко А.А. P33113\nПримеров Е.В. P0000"
    result = func(text, group)
    assert expected == result

def test_3():
    group = "P0000"
    text = """Голованова-Иванова Д.Д. P3119
Примеров Е.В. P0000"""

    expected = "Голованова-Иванова Д.Д. P3119\nПримеров Е.В. P0000"
    result = func(text, group)
    assert expected == result

def test_4():
    group = "P3119"
    text = """Голованова-Иванова Г.Г. P3119
Примеров Е.В. P0000"""

    expected = "Примеров Е.В. P0000"
    result = func(text, group)
    assert expected == result

def test_5():
    group = "P3119"
    text = """Примеров Петр Петрович P3119
Кузнецов Александр Б. P3119"""

    expected = "Кузнецов Александр Б. P3119"
    result = func(text, group)
    assert expected == result


def test_6():
    group = "P3119"
    text = """Примеров P3119
Кузнецов Александр Б. P3119"""

    expected = "Примеров P3119\nКузнецов Александр Б. P3119"
    result = func(text, group)
    assert expected == result


def test_7():
    group = "P3119"
    text = """Примеров П. П.
Кузнецов А. М."""

    expected = "Примеров П. П.\nКузнецов А. М."
    result = func(text, group)
    assert expected == result

def test_8():
    group = "P3119"
    text = """Иванова-Петрова Ирина P3119
Иванова-Петрова Петр P3119"""

    expected = "Иванова-Петрова Петр P3119"
    result = func(text, group)
    assert result == expected

def test_9():
    group = "P3119"
    text = """   Петров П.П. P3119   
   Иванов И.А. P3119   """

    result = func(text, group)
    assert "Петров П.П." not in result
    assert "Иванов И.А." in result

if __name__ == "__main__":
    for test in (test_1, test_2, test_3, test_4, test_5, test_6, test_7, test_8, test_9):
        try:
            test()
            print(f"{test.__name__}: OK")
        except AssertionError as e:
            print(f"{test.__name__}: FAIL")