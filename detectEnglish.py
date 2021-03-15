#code based on the book Cracking Codes with Python
#this is a code which we can use to find a english word in a encrypted/decrypted message through a dictionary file
#there must be a dictionary.txt in the same directory
#to use: import detectEnglish
#detectEnglish.isEnglish(string)
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#the letters_and_space variable contain all the uppercase and lowercase letters. It too thas space, tab and newline character.
letters_and_space = upper_letters + upper_letters.lower()+' \t\n'


#this function copies the words from the dictionary.txt to a dictionary data type
def loadDictionary():
    dictionary_file = open('dictionary.txt')
    english_words ={}
    #i'm using this parameter in split because there is one word per line in my dictionary.txt
    for word in dictionary_file.read().split('\n'):
        english_words[word] = None
    dictionary_file.close()
    return english_words

ENGLISH_WORDS = loadDictionary()

#this function return a float value indicating the ratio as a value between 0.0(None words in english) and 1.0(all the words in english)
def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possible_words = message.split()

    if possible_words == []:
        return 0.0

    matches = 0
    #if i find this word in my dictionary, so it's a english word.
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches+=1
    return float(matches)/len(possible_words)

#this function removes the non-letters characters on my encrypted/decrypted message
def removeNonLetters(message):
    letters_only =[]
    for symbol in message:
        if symbol in letters_and_space:
            letters_only.append(symbol)
    return ''.join(letters_only)


def isEnglish(message, word_percentage=20, letters_percentage=85):
    words_match = getEnglishCount(message)*100 >= word_percentage
    num_letters = len(removeNonLetters(message))
    message_letters_percentage = float(num_letters) / len(message)*100
    letters_match = message_letters_percentage >= letters_percentage
    return words_match and letters_match
