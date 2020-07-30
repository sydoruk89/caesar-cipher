import re
try:
    def read_file(path):
        """ The function takes data from text file and return a stripped string.

        Args:
            path (txt): txt file
        """
        with open(path, 'r') as words_read:
            text = words_read.read()
            return text
except FileNotFoundError as error:
    print(error)

stored_words = read_file('assets/words.txt')

def encrypt(plain_text, key):
    """
    The function takes a text and a key which is a numeric shift.
    ('abc', 1) --> 'bcd'
    """

    encrypted_text = ''
    for char in plain_text:
        if re.match('[^a-zA-Z]', char):
            encrypted_text += char
        elif char.isupper():
            encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
        else:
            encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
    return encrypted_text

def decrypt(encoded, key):
    return encrypt(encoded, -key)

def decrypt_without_key(encoded):
    list_var = []
    text = ''
    for i in range(26):
        decrypted_text = ''
        for char in encoded:
            if re.match('[^a-zA-Z]', char):
                decrypted_text += char
            elif char.isupper():
                decrypted_text += chr((ord(char) + i - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) + i - 97) % 26 + 97)
        list_var.append(decrypted_text)
        decrypted_text = ''
    for el in list_var:
        words = el.split()
        count = 0
        for word in words:
            if word.lower() in stored_words:
                count += 1
        if count / len(words) > 0.8:
            print(count / len(words))
            for el in words:
                text += f' {el}'
            return text

if __name__ == "__main__":
    m = encrypt('It was the best of times, it was the worst of times.', 34)
    print(decrypt_without_key(m))