
from os import urandom
from binascii import hexlify
from cryptography .hazmat. primitives .ciphers import Cipher , algorithms , modes
key = urandom (16)
iv = urandom (16)
cipher = Cipher( algorithms .AES(key), modes.ECB ())
encryptor = cipher. encryptor ()
# What happens i f you don ' t p a s s 16−b y t e i n p u t ?
ct = encryptor .update(b"attack at dawn!!") + encryptor .finalize ()
print(hexlify(key ))
cphFile = open("ciphertext.bin", "wb")
cphFile.write(ct)
cphFile.close ()
