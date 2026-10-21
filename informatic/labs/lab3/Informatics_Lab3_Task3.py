# Author = Krahmalnikov Ilya Artemovich
# Group = P3119
# Date = 09.10.2026

import re

err_len = "Your password must be at least 5 characters"
err_number = "Your password must include a number"
err_upper = "Your password must include an uppercase character"
err_special = "Your password must include a special letter"
err_sum = "Your password must add up to 25"
err_month = "Your password must include a month of the year"

def func(password):
    reg_number = r".*[0-9].*"
    reg_upper = r"[A-Z]"
    reg_special = r".*[^\w\s\d].*"
    reg_sum = r"[1-9]"
    reg_month = (r"(?i).*(january|february|march|april|may|june|july"
                 r"|august|september|october|november|december).*")

    errs = set()

    if len(password) < 5:
        errs.add(err_len)

    if not re.match(reg_number, password):
        errs.add(err_number)

    if not re.search(reg_upper, password):
        errs.add(err_upper)

    if not re.match(reg_special, password):
        errs.add(err_special)

    numbers = re.findall(reg_sum, password)
    sm = sum(map(int, numbers))
    if sm != 25:
        errs.add(err_sum)

    if not re.match(reg_month, password):
        errs.add(err_month)

    return errs

def test_1():
    expected = {err_sum}
    result = func("KL4D0VK4_P4VLU*xx!july23>13377331WxR")
    assert expected == result

def test_2():
    expected = set()
    result = func("KLD0VK4_PV2LU*xx!july23>7331WxR")
    assert expected == result

def test_3():
    expected = {err_upper}
    result = func("KLD0VK4_PV2LU*xx!july23>7331WxR".lower())
    assert expected == result

def test_4():
    expected = {err_upper, err_len, err_sum, err_month}
    result = func("kl0!")
    assert expected == result

def test_5():
    expected = {err_upper, err_sum, err_month}
    result = func("kl0!6")
    assert expected == result

def test_6():
    expected = {err_upper, err_sum, err_number, err_special, err_len}
    result = func("july")
    assert expected == result

def test_7():
    expected = {err_sum, err_number, err_special, err_len}
    result = func("juLy")
    assert expected == result

def test_8():
    expected = set()
    result = func("mAy!997")
    assert expected == result

if __name__ == "__main__":
    for test in (test_1, test_2, test_3, test_4, test_5, test_6, test_7, test_8,):
        try:
            test()
            print(f"{test.__name__}: OK")
        except AssertionError as e:
            print(f"{test.__name__}: FAIL")