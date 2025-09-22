key = "abcdefghijklmnopqrstuvwxyz"

def encryption(shift, plaintext):
    result = ''
    for p in plaintext:
        if p.islower():
            i = (key.index(p) + shift) % 26
            result += key[i]
        elif p.isupper():
            i = (key.index(p.lower()) + shift) % 26
            result += key[i].upper()
        else:
            result += p
    return result


def decryption(shift, encrypted_text):
    result = ""
    for p in encrypted_text:
        if p.islower():
            i = (key.index(p) - shift) % 26
            result += key[i]
        elif p.isupper():
            i = (key.index(p.lower()) - shift) % 26
            result += key[i].upper()
        else:
            result += p
    return result


msg = "Ali Sajid is man of his Qualities"
encrypted = encryption(15, msg)
print("Encrypted text:", encrypted)

decry = decryption(15, encrypted)
print("Decrypted text:", decry)
