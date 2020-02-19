from basen import BaseN

"""
	Converting an image to BaseN with custom alphabet
"""

chunk_size = 10
engine = BaseN("lI", chunk_size)

with open("lena.jpg", "rb") as image:
	f = image.read()
	b = bytearray(f)
	encoded = engine.encoder(b)
	print(f"The image is encoded with chunk_size {chunk_size}:")
	print(encoded[:100], "......", encoded[-100:])
