# Copyright (C) 2017-2024 by Vd.
# This file is part of BaseN package.
# BaseN is released under the MIT License (see LICENSE).


from .basen import BaseN
from .int2base import int2base, base2int

VERSION = "v1.0.2"
__version__ = VERSION


def version():
    return VERSION
