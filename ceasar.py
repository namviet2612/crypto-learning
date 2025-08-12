alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plain_text = 'THIS IS A MESSAGE'
cipher_text = ''
key = 3
vigenere_key = 'SECRET'

def ceasar_encrypt(plain_text, _key = key):
    _cipher_text = ''
    for c in plain_text:
        index = alphabet.find(c)
        index = (index + _key) % len(alphabet)
        _cipher_text = _cipher_text + alphabet[index]
    return _cipher_text

def ceasar_decrypt(cipher_text, _key = key):
    _plain_text = ''
    for c in cipher_text:
        index = alphabet.find(c)
        index = (index - _key) % len(alphabet)
        _plain_text = _plain_text + alphabet[index]
    return _plain_text

def ceasar_cracking(cipher_text):
    _plain_text = ''
    for _key in range(1, len(alphabet)):
        _plain_text = ceasar_decrypt(cipher_text, _key)
        print("key = ", _key, ", plain text = ", _plain_text)

def vigenere_encrypt(plain_text, _key = vigenere_key):
    _cipher_text = ''
    key_cnt = 0
    key_list = list(_key)
    for c in plain_text:
        index = alphabet.find(c)
        key_index = alphabet.find(key_list[key_cnt])
        index = (index + key_index) % len(alphabet)
        key_cnt = (key_cnt + 1) % len(_key)
        _cipher_text = _cipher_text + alphabet[index]
    
    print(_cipher_text)
    return _cipher_text

def vigenere_decrypt(cipher_text, _key = vigenere_key):
    _plain_text = ''
    key_cnt = 0
    key_list = list(_key)
    for c in cipher_text:
        index = alphabet.find(c)
        key_index = alphabet.find(key_list[key_cnt])
        index = (index - key_index) % len(alphabet)
        key_cnt = (key_cnt + 1) % len(_key)
        _plain_text = _plain_text + alphabet[index]
    print(_plain_text)
    return _plain_text


if __name__ == '__main__':
    #cipher_text = ceasar_encrypt(plain_text)
    #ceasar_cracking(cipher_text)

    cipher_text = vigenere_encrypt(plain_text)
    vigenere_decrypt(cipher_text)