from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

DES_key = get_random_bytes(8)
cipher_encrypt = DES.new(DES_key, DES.MODE_CBC)

plain_text = b'This is my message'
cipher_text = cipher_encrypt.encrypt(pad(plain_text, DES.block_size))

cipher_decrypt = DES.new(DES_key, DES.MODE_CBC, cipher_encrypt.iv)
plain_text_decrypted = unpad(cipher_decrypt.decrypt(cipher_text), DES.block_size)

print(plain_text)
print(plain_text_decrypted)
