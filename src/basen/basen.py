# Copyright (C) 2017-2021 by Ivan.
# This file is part of BaseN package.
# BaseN is released under the MIT License (see LICENSE).


from typing import Union

from .int2base import int2base, base2int


class BaseN:
    def __init__(self, alphabet: str, chunk_size: int, byteorder='big', pad_byte: int = 0xFF, pad_char: str = '='):
        """\
        Creates new BaseN encoder/decoder to encode arbitrary binary data to
        string representation in a given base(length of alphabet).

        :param alphabet: alphabet to use in encoder
        :param chunk_size: encoding chunk size
        :param byteorder: int to bytes byteorder conversion
        :param pad_byte: byte to padding last chunk if needed
        :param pad_char: char to indicate padding bytes
        """

        assert isinstance(chunk_size, int), "`chunk` must be `int`!"
        assert chunk_size >= 1, "`chunk` value must be >= 1!"
        assert isinstance(alphabet, str), "`alphabet` must be `str`!"
        assert len(alphabet) > 1, "`alphabet` length must be > 1!"
        assert byteorder in ('big', 'little'), "`byteorder` value must be `big` or `little`!"

        self._alphabet = alphabet
        self._chunk_size = chunk_size
        self._byteorder = byteorder
        self._pad_byte = pad_byte
        self._pad_char = pad_char

        # calculate size of encoded block
        self._block_size = len(int2base(int.from_bytes(bytearray((0xFF,)) * chunk_size, byteorder), alphabet))

    @property
    def alphabet(self) -> str:
        """

        :return: used alphabet
        """

        return self._alphabet

    @property
    def chunk_size(self) -> int:
        """

        :return: used block size
        """

        return self._chunk_size

    @property
    def block_size(self) -> int:
        """

        :return: calculated encoding block size
        """

        return self._block_size

    @property
    def byteorder(self) -> str:
        """

        :return: used byteorder
        """

        return self._byteorder

    @property
    def pad_char(self) -> str:
        """

        :return: used padding char
        """

        return self._pad_char

    @property
    def pad_byte(self) -> int:
        """

        :return: used padding byte
        """

        return self._pad_byte

    def encode(self, inp: Union[bytearray, bytes, str]) -> str:
        """\
        Encodes bytearray, bytes or string to string.

        :param inp:
        :return:
        """

        assert isinstance(inp, (bytearray, bytes, str)), "`input` must be `bytearray`, `bytes` or `str`!"

        if type(inp) == str:
            inp = inp.encode()

        pads = len(inp) % self.chunk_size
        if pads:
            inp = inp + bytearray((self.pad_byte,)) * (self.chunk_size - pads)

        out = str()
        for i in range(0, len(inp), self.chunk_size):
            c = int.from_bytes(inp[i: i + self.chunk_size], self.byteorder)
            block = int2base(c, alphabet=self.alphabet)
            if len(block) < self.block_size:
                block = (self.alphabet[0] * (self.block_size - len(block))) + block
            out += block

        if pads:
            return out + self.pad_char * (self.chunk_size - pads)
        return out

    def decode(self, inp: str) -> bytearray:
        """\
        Decodes string to bytearray.

        :param inp: input string for decoding
        :return: decoded data
        """

        assert isinstance(inp, str), "`input` must be `str`!"

        size = len(inp)
        inp = inp.rstrip(self.pad_char)
        pads = size - len(inp)

        if len(inp) % self.block_size:
            raise ValueError('Wrong size of `input`!')

        out = bytearray()

        for i in range(0, len(inp), self.block_size):
            block = base2int(inp[i: i + self.block_size], self.alphabet)
            out += block.to_bytes(self.chunk_size, self.byteorder)

        if pads:
            return out[:-pads]
        return out
