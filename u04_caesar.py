# Cäsar-Chiffre (Verschiebung im Alphabet)

# Hallo
# Cipher: 3
# Wird zu: Kdoor
# https://de.wikipedia.org/wiki/Caesar-Verschl%C3%BCsselung

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '


def encrypt(text, chiffre=3):
    crypt = ''

    for char in text:
        pos = abc.index(char)

        pos += chiffre

        if pos > len(abc) - 1:
            pos = pos - len(abc)

        new_char = abc[pos]
        crypt += new_char

    return crypt


crypt_text = encrypt('Hallo')
print(crypt_text)
