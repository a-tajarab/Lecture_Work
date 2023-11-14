from string import ascii_lowercase as letters
def rot_13(message):
    rotters = letters[13:] + letters[:13]
    output = ''
    for c in message:      # iteration
        pos = letters.find(c)
        output += rotters[pos]
    return output


if __name__ == '__main__':
    encrypt = rot_13("secret message")
    print("encrypted =", encrypt)
    decrypt = rot_13(encrypt)
    print("decrypted = ", decrypt)