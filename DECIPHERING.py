from string import ascii_lowercase as lowers
from string import ascii_uppercase as uppers
def rot_13(message):
    rotters_lower = lowers[13:] + lowers[:13]
    rotter_upper = uppers[13:] + uppers[:13]
    output = ''
    for c in message:      # iteration
        if c == '':
            output += ''
        else:
            pos = letters.find(c)
            output += rotters[pos]
    return output


if __name__ == '__main__':
    encrypt = rot_13("secret message")
    print("encrypted =", encrypt)
    decrypt = rot_13(encrypt)
    print("decrypted = ", decrypt)