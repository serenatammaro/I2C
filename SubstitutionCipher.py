#text to encrypt

plainText = 'ciaouz'

#substitution key

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", ",", "!", "?", " "]
"""
def subKey (alphabet):
    for i in range(len(alphabet)):
        
        if i in range(0, 20):
            encryptedLetter = alphabet[i + 5]
            print(encryptedLetter + "0-20")
            if alphabet[i] == '.':
                print('.')
            elif alphabet[i] == ',':
                print(',')
            elif alphabet[i] == '!':
                print('!')
            elif alphabet[i] == '?':
                print('?')
            elif alphabet[i] == ' ':
                print('space')
        elif i in range(19, 25):
            encryptedLetter = alphabet[i - 20]
            
        elif i > 25:
            encryptedLetter = alphabet[i]
            
    print("------------------------------------")
"""""

#Encrypt plaintext 
newList = []
def stringToList(plainText):
   
    for x in plainText:
        newList.append(x)
    print("newList: ")
    
    
encdMessage = []
newIndex = ""

def encMessage(newList):
    for messageLetter in newList:
        
        
        for alphaLetter in alphabet:
            
            if messageLetter == alphaLetter:
                indexAlphabet = alphabet.index(alphaLetter)

                if indexAlphabet in range(0, 20):
                    newIndex = indexAlphabet + 5
                    encryptedLetter = alphabet[indexAlphabet + 5]
                    print(encryptedLetter + "0-20")
                elif alphaLetter == '.':
                    print('.')
                elif alphaLetter == ',':
                    print(',')
                elif alphaLetter == '!':
                    print('!')
                elif alphaLetter == '?':
                    print('?')
                elif alphaLetter == ' ':
                    print('space')
                elif indexAlphabet in range(19, 25):
                    newIndex = indexAlphabet - 20
            
                elif indexAlphabet > 25:
                    newIndex = alphabet[indexAlphabet]
            
   # print("------------------------------------")

                #newIndex = indexAlphabet + 5
                encdLetter = alphabet[newIndex]
                encdMessage.append(encdLetter)

                

                
    print("encdMessage")
    print(encdMessage)
            

    print("List")
    print(newList)



#SubKey(alphabet)
stringToList(plainText)
encMessage(newList)
