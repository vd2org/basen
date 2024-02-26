# Copyright (C) 2017-2024 by Vd.
# This file is part of BaseN package.
# BaseN is released under the MIT License (see LICENSE).


import string
from os.path import join, dirname

from basen import BaseN

FULL_ALPHABET = string.ascii_letters + string.digits
BINARY_ALPHABET = '01'
DATA = b"This is a test post, please ignore!"

with open(join(dirname(__file__), "data/lena.jpg"), "rb") as image:
    FILE_DATA = bytearray(image.read())


def test_bytes_full():
    conv = BaseN(FULL_ALPHABET, 2)

    encoded = conv.encode(DATA)
    decoded = conv.decode(encoded)

    assert DATA == decoded


def test_bytes_binary():
    conv = BaseN(BINARY_ALPHABET, 3)

    encoded = conv.encode(DATA)
    decoded = conv.decode(encoded)

    assert DATA == decoded


def test_file_full():
    conv = BaseN(FULL_ALPHABET, 8)

    encoded = conv.encode(FILE_DATA)
    decoded = conv.decode(encoded)

    assert FILE_DATA == decoded


def test_file_binary():
    conv = BaseN(BINARY_ALPHABET, 16)

    encoded = conv.encode(FILE_DATA)
    decoded = conv.decode(encoded)

    assert FILE_DATA == decoded
