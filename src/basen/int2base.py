# Copyright (C) 2017-2021 by Ivan.
# This file is part of BaseN package.
# BaseN is released under the MIT License (see LICENSE).


def int2base(inp: int, alphabet: str) -> str:
    """\
    Convert an integer to its string representation in a given base(length of alphabet).

    :param inp: input integer to conversion
    :param alphabet: alphabet to conversion
    :return:
    """

    assert isinstance(inp, int), "`input` must be `int`!"
    assert isinstance(alphabet, str), "`alphabet` must be `str`!"
    assert len(alphabet) > 1, "`alphabet` length must be > 1!"

    if inp == 0:
        return alphabet[0]
    if inp < 0:
        raise ValueError("`input` must be positive integer.")
    out = str()
    b = len(alphabet)
    while inp > 0:
        inp, idx = divmod(inp, b)
        out = alphabet[idx] + out
    return out


def base2int(inp: str, alphabet: str) -> int:
    """\
    Convert an string representation to its integer in a given base(length of alphabet)

    :param inp: input string to conversion
    :param alphabet: alphabet to conversion
    :return:
    """

    assert isinstance(inp, str), "`input` must be `str`!"
    assert isinstance(alphabet, str), "`alphabet` must be `str`!"
    assert len(alphabet) > 1, "`alphabet` length must be > 1!"

    pwr = len(inp) - 1
    out = 0
    b = len(alphabet)
    for c in inp:
        if c not in alphabet:
            raise ValueError("`input` out of alphabet")
        out += b ** pwr * alphabet.index(c)
        pwr -= 1
    return out
