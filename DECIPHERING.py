from string import ascii_lowercase as letters
def rot_13(message):
    rotters = letters[13:] + letters[:13]
    output = ''
    for c in message:            # iteration
        output += c
    return output


if __name__ == '__main__':
    encrypt = rot_13("secret message")
    print(encrypt)