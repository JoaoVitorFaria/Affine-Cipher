#code based on the book Cracking Codes with Python
#this is a code to crack the Affine Cipher
import pyperclip, affineCipher, detectEnglish, cryptomath

SILENT_MODE = False# it can be changed to True in order to don't show the attempts with different keys


def main():

    my_message = """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""
    hacked_message = hackAffine(my_message)

    if hacked_message != None:
        print('Copying hacked message to clipboard:')
        print(hacked_message)
        pyperclip.copy(hacked_message)
    else:
        print('Failed to hack encryption.')

def hackAffine(message):
    print("hacking...")
    print('(Press Ctrl-c or Ctrl-d to quit at any time)')
    #the operator ** is the expoent operator, equivalent to pow function in c++
    #we use the ** because we know that there are at most len(affineCipher.SYMBOLS)
    #possible integer for key_a and the same for key_b, so we multiply these values
    for key in range(len(affineCipher.SYMBOLS)**2):
        #here we get the key_a part of the key we're testing
        key_a = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(key_a, len(affineCipher.SYMBOLS))!= 1:
            continue
        decrypted_text = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print("Tried key %s... (%s)"%(key, decrypted_text[:40]))

        if detectEnglish.isEnglish(decrypted_text):
            print()
            print("Possible encryption hack")
            print("key: %s"%(key))
            print("Decrypted message : "+ decrypted_text[:200])
            print()
            print("Enter D for fone, or just press Enter to continue hacking: ")
            response = input('>')

            if response.strip().upper().startswith('D'):
                return decrypted_text
    return None

if __name__ == '__main__':
    main()
