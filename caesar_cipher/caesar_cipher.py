import nltk
nltk.download('words', quiet=True)
from nltk.corpus import words

lower = ["a", "b", "c", "d",  "e", "f", "g", "h", "i", "j", "k", "l", 'm', "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

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
        to_add = ""
        count = 0
    
    
        for char in cracked:
            if char in upper:
                x = upper.index(char)
                x = (x - key) % 26
                to_add += upper[x]
            elif char in lower:
                x = lower.index(char)
                x = (x - key) % 26
                to_add += lower[x]
            
            else:
                to_add+= char
        
        words = to_add.split()
        for i in words:
            if i in list_word:
                count += 1

        c = [to_add, count]
        cracked_message.append(c)

    value = cracked_message[0][1]
    counter = 0
    for i in range(len(cracked_message)):
        if value < cracked_message[i][1]:
            counter = i
            value = cracked_message[i][1]

    return cracked_message[counter][0]




# print(encrypt("abc", 1))
# print(decrypt('bcd', 1))
test = encrypt("It was the best of times, it was the worst of times.", 2)
print(crack(test))
