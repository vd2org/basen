from basen import BaseN

print("""
	Converting an str to BaseN with custom alphabet	
""")

custom_alphabet = "lI"
chunk_size = 2
engine = BaseN(custom_alphabet, chunk_size)

input_string = "This is a test post, please ignore"

encoded = engine.encoder(input_string)
decoded = engine.decoder(encoded)
print(f"Input: {input_string} \n Output: {encoded}\n Converted back: {decoded}")

print("""
	Converting an image to BaseN with custom alphabet
""")

custom_alphabet = "abc"
chunk_size = 8
engine = BaseN(custom_alphabet, chunk_size)

with open("lena.jpg", "rb") as image:
	f = image.read()
	b = bytearray(f)
	encoded = engine.encoder(b)
	print(f"The image is encoded with chunk_size {chunk_size}:")
	print(encoded[:100], "......", encoded[-100:])
