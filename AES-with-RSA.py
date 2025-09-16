from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

AES_key = get_random_bytes(16)
print("AES key:", AES_key)

# RSA (public key and private key)
# RSA encrypts a session key (AES)
RSA_key = RSA.generate(2048)
private_key = RSA_key
public_key = RSA_key.publickey()

# Encrypt the AES key with the RSA public key
encrypt_rsa = PKCS1_OAEP.new(public_key)
enc_AES_key = encrypt_rsa.encrypt(AES_key)
print("Encrypted AES key:", enc_AES_key)

# Encrypt a message with AES
cipher_encrypt = AES.new(AES_key, AES.MODE_GCM)
plain_text = b'This is my message'
cipher_text, tag = cipher_encrypt.encrypt_and_digest(plain_text)
nonce = cipher_encrypt.nonce
print("Cipher text:", cipher_text)
print("Tag:", tag)
print("Nonce:", nonce)

# Decrypt the AES key with the RSA private key
decrypt_rsa = PKCS1_OAEP.new(private_key)
dec_AES_key = decrypt_rsa.decrypt(enc_AES_key)
print("Decrypted AES key:", dec_AES_key)

# Decrypt the message with AES
cipher_decrypt = AES.new(dec_AES_key, AES.MODE_GCM, nonce=nonce)
plain_text_decrypted = cipher_decrypt.decrypt_and_verify(cipher_text, tag)
print("Decrypted message:", plain_text_decrypted)