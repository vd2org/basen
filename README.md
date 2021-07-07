# BaseN

Custom encoder that encodes any binary data to given alphabet.

### Requirements

Python 3.6 and above. No additional dependencies.

### Installation

`pip install basen-converter`

## Usage

### Numbers

Convert a number to the string and back

```python
import string

import basen

ALPHABET = string.ascii_letters + string.digits

for i in range(1000, 2000, 9):
    encoded = basen.int2base(i, ALPHABET)
    decoded = basen.base2int(encoded, ALPHABET)

    print(i, encoded, decoded)
```
#### Output:

```text
1000 qi 1000
1009 qr 1009
1018 qA 1018
1027 qJ 1027
...
```

### Huge numbers

Even huge numbers can be converted as well.

```python
import string

import basen

ALPHABET = string.ascii_letters + string.digits

NUM = 10**100

encoded = basen.int2base(i, ALPHABET)
decoded = basen.base2int(encoded, ALPHABET)

print(NUM)
print(encoded)
print(decoded)
```

#### Output:

```text
10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
Am851IcwtXApqVErDmkjfH9ikry1v4YsyaP4zUrrmM8H8j83wfxbV02K
10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

### Convert a binary

Convert a binary data to printable text like base64 but with an arbitrary alphabet.

```python
import string

import basen

ALPHABET = string.ascii_letters
DATA = "Some binary data..."

encoder = basen.BaseN(string.ascii_letters, 3)
encoded = encoder.encode(DATA)
decoded = encoder.decode(encoded)

print(DATA)
print(encoded)
print(decoded)
```

#### Output:

```text
Some binary data...
aMUkfaVgYAaXhpLbbsxuaUOUCaTprkavVgx==
bytearray(b'Some binary data...')
```
