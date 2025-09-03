from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

AES_key = get_random_bytes(16)
cipher_encrypt = AES.new(AES_key, AES.MODE_CBC)

plain_text = b'This is my message'
cipher_text = cipher_encrypt.encrypt(pad(plain_text, AES.block_size))

cipher_decrypt = AES.new(AES_key, AES.MODE_CBC, cipher_encrypt.iv)
plain_text_decrypted = unpad(cipher_decrypt.decrypt(cipher_text), AES.block_size)

print(plain_text)
print(plain_text_decrypted)
