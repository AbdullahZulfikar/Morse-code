# Morse-code
Morse Code Encryption and Decryption
This Python script provides a simple Morse code encryption and decryption tool. Users can input a message, and the script will encode it into Morse code or decode a Morse code message back into plaintext.

Morse Code Dictionary
The script uses the following Morse code dictionary for encryption and decryption:

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    # ... (other Morse code mappings)
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    # ... (other special characters)
}
Usage
Encrypting a Message (Encoding):

To encrypt a message, run the script and enter a message when prompted. The script will then provide the Morse code equivalent of the input.

bash
Copy code
Enter your message to encrypt: Hello World
Output:

bash
Copy code
This is your encoded message: .... . .-.. .-.. ---   .-- --- .-. .-.. -..
Decrypting a Message (Decoding):

To decrypt a Morse code message, run the script and enter the Morse code when prompted. The script will then provide the plaintext equivalent.

Output:

bash
Copy code
This is your decoded message: HELLO WORLD
How to Run
Ensure you have Python installed on your system. Run the script by executing the following command in your terminal:

bash
Copy code
python morse_code.py
Notes
Make sure to separate words with spaces when entering messages or Morse code.
The script is case-insensitive, so you can enter messages in uppercase or lowercase.
