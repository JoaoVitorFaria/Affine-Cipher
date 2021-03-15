#code based on the book Cracking Codes with Python
#this is an affine cipher algorithm
#The affine cipher uses multiplication and addition with two integers keys to encrypt
#the cyptomath module has the gcd() and findModInverse() functions, which are necessary to do the decryption
import sys, pyperclip, cryptomath, random


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def main():
    #my_message = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    my_message = """""5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""
    my_key = 2894#it's  possible to change this to 'my_key = getRandomKey()" in order to get a 'random' key
    my_mode = 'decrypt'# you can change this to 'decrypt'

    if my_mode == 'encrypt':
        translated = encryptMessage(my_key, my_message)
    elif my_mode == 'decrypt':
        translated = decryptMessage(my_key, my_message)

    print('Key: %s' %(my_key))
    #this line tells the user wether the output message is encrypted or decrypted
    print('%sed text:'%(my_mode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard.'%(my_mode))

#this function splits a single integer key into two integers keys
#for example, let's suppose : 
def getKeyParts(key): # key = 2894
    key_a = key // len(SYMBOLS) #key_a = 2894 // 66 = 43
    key_b = key % len(SYMBOLS) #key_b = 2894 % 66 = 56
    #to combine the keys back into a single key: (key_a * symbol_set_size)+key_b
    return (key_a, key_b)

#this function verifies if one(or both) key isn't strong enough
def checkKeys(key_a, key_b, mode):
    if key_a == 1 and mode == 'encrypt':
        sys.exit("Cipher is weak if key A is 1. Choose a different key.")

    if key_b == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if key B is 0. Choose a different key.')
    if key_a < 0 or key_b < 0 or key_b > len(SYMBOLS)-1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
    #this statement verifies one of the conditions to affine cipher.
    #key_a must be relatively prime to the symbol set size
    #to verify, it's used the gcd function. In this case, the GCD of key_a em len(SYMBOLS) must be equal to 1.
    if cryptomath.gcd(key_a, len(SYMBOLS))!= 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (key_a, len(SYMBOLS)))        

def encryptMessage(key, message):
    key_a, key_b = getKeyParts(key)
    checkKeys(key_a, key_b, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            #if the character exist in our symbolset, we save his index to do the calculation
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * key_a + key_b) % len(SYMBOLS)]
        else :
            ciphertext += symbol
    return ciphertext

def decryptMessage(key, message):
    key_a, key_b = getKeyParts(key)
    checkKeys(key_a, key_b, 'decrypt')
    plaintext = ''
    #instead of multiplying by key_a, the decryption process multiplies by the modular inverse of key_a
    modInverseOfKeyA = cryptomath.findModInverse(key_a, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS [(symbolIndex - key_b) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol
    return plaintext

def getRandomKey():
    while True:
        #firstly we ensure that there's no key equal to the invalid values 0 or 1
        key_a= random.randint(2, len(SYMBOLS))
        key_b= random.randint(2, len(SYMBOLS))
        #then we garantee that key_a is a relatively prime with the symbol set size
        if cryptomath.gcd(key_a, len(SYMBOLS)) == 1:
            return key_a * len(SYMBOLS) + key_b

if __name__ == '__main__':
    main()
    













            
