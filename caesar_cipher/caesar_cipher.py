import nltk
nltk.download('words', quiet=True)
from nltk.corpus import words

lower = ["a", "b", "c", "d", "d", "e", "f", "g", "h", "i", "j", "k", "l", 'm', "n", "o", "p", "q", "r", "S", "t", "u", "v", "w", "x", "y", "z"]

upper = []

for word in lower:
    upper.append(word.upper())

list_word = words.words()


def encrypt(plain, key):
    text_encrypt = ''

    for char in plain:

        if char in lower:
           temp = lower.index(char)
           temp1 = (temp + key) % 26
           text_encrypt += lower[temp1]
       
        elif char in upper:
            temp = upper.index(char)
            temp1 = (temp + key) % 26
            text_encrypt += upper[temp1]

        else:
             text_encrypt += char

    return text_encrypt

def decrypt(encoded, key):
    decrypted_text = encrypt(encoded, -key)
    return decrypted_text


def crack(cracked):
    cracked_message = []
    for key in range(len(lower)):





if __name__=="__main__":
  print(encrypt("abc", 1))
#   print(decrypt("dgh", 1))
