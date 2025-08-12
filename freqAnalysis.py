import matplotlib.pyplot as plt

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def ceasar_decrypt(cipher_text, _key):
    _plain_text = ''
    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - _key) % len(ALPHABET)
        _plain_text = _plain_text + ALPHABET[index]
    return _plain_text

def freqAnalysis(text):
    text = text.upper()

    letter_freq = {}

    for letter in ALPHABET:
        letter_freq[letter] = 0

    for letter in text:
        if letter in ALPHABET:
            letter_freq[letter] += 1

    return letter_freq

if __name__ == '__main__':
    cipher_text  = 'UGVIUMQAJITIHAPWTKHMZQIUNZWUJCLIXMABPCVOIZGQIUYCITQNQMLIAIXPGAQKQABIBBPMUWUMVBQIUEWZSQVOIAIAQUCTIBQWVMVOQVMMZIBIUCTBQVIBQWVITKWUXIVGQPIDMJMMVQVBMZMABMLQVITOWZQBPUAIVLLIBIABZCKBCZMAIVLQBAQUXTMUMVBIBQWVAMAXMKQITTGQVRIDIAQVKMCVQDMZAQBGTIBMZWVQOWBIKYCIQVBMLEQBPUIKPQVMTMIZVQVOBMKPVQYCMAIZBQNQKQITQVBMTTQOMVKMVCUMZQKITUMBPWLAIVLZMKQXMAACKPIAAWTDQVOLQNNMZMVBQITMYCIBQWVATQVMIZITOMJZIQVBMZXWTIBQWVIVLMFBZIXWTIBQWVBPMAMBPQVOAUIGXZWDMBWJMDMZGDMZGQUXWZBIVBQVAMDMZITNQMTLAAWNBEIZMMVOQVMMZQVOZMAMIZKPIVLLMDMTWXUMVBWZQVDMABUMVBJIVSQVOQPIDMIAXMKQITILLQKBQWVBWYCIVBQBIBQDMUWLMTAACKPIABPMJTIKSAKPWTMAUWLMTWZBPMUMZBWVUWLMT'
    letter_freq = freqAnalysis(cipher_text)
    letter_freq = sorted(letter_freq.items(), key = lambda item:item[1], reverse=True)
    posible_key = ALPHABET.find(letter_freq[0][0]) - ALPHABET.find('E')
    print('Possible key: ', posible_key)
    print(ceasar_decrypt(cipher_text, posible_key))
