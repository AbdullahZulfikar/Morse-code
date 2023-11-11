# in this we will design the morse code the user will give us the string and we will make it work
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


# now we will make to encrypt function
def encrypt(data):
    cipher = ''
    for letter in data:
        if data != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher


def decrypt(message):
    global i
    message += ' '

    citext = ''
    cypher = ''
    # if no space then
    for words in message:
        if words != ' ':
            i = 0
            citext += words
        else:
            i += 1
            if i == 2:
                cypher += ''
            else:
                try:
                    cypher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                                .values()).index(citext)]
                except ValueError:
                    pass
                citext = ''
    return cypher


def main():
    message = input("Enter your message to encrypt").upper()
    encrypted = encrypt(message)
    print(f"this is your encoded message {encrypted}")

    enter = input("Enter word")
    decrypted = decrypt(enter)
    print(f"this is your encoded message {decrypted}")


if __name__ == '__main__':
    main()
