# Copyright (C) 2017-2024 by Vd.
# This file is part of BaseN package.
# BaseN is released under the MIT License (see LICENSE).


import string

from basen import int2base, base2int

FULL_ALPHABET = string.ascii_letters + string.digits
BINARY_ALPHABET = '01'


def test_usually():
    for i in range(10000):
        c = int2base(i, FULL_ALPHABET)
        r = base2int(c, FULL_ALPHABET)

        assert isinstance(c, str)
        assert isinstance(r, int)

        print(i, c, r, type(r))

        assert r == i


def test_digits():
    for i in range(10000):
        c = int2base(i, string.digits)
        r = base2int(c, string.digits)

        assert isinstance(c, str)
        assert isinstance(r, int)

        print(i, c, r, type(r))

        assert i == int(c) == r


def test_binary():
    for i in range(10000):
        c = int2base(i, BINARY_ALPHABET)
        r = base2int(c, BINARY_ALPHABET)

        assert isinstance(c, str)
        assert isinstance(r, int)
        assert r == i

        assert f"0b{c}" == bin(r)
