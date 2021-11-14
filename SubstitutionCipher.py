#text to encrypt

plainText = 'ciao'

#substitution key

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", ",", "!", "?", " "]
def subKey (alphabet):
    for i in range(len(alphabet)):
        
        if i in range(0, 20):
            encryptedLetter = alphabet[i + 5]
            print(encryptedLetter + "0-20")
            """if alphabet[i] == '.':
                print('.')
            elif alphabet[i] == ',':
                print(',')
            elif alphabet[i] == '!':
                print('!')
            elif alphabet[i] == '?':
                print('?')
            elif alphabet[i] == ' ':
                print('space')"""
        elif i in range(19, 25):
            encryptedLetter = alphabet[i - 20]
            print(encryptedLetter + "19-25")
        elif i > 25:
            encryptedLetter = alphabet[i]
            print(alphabet[i] + "symbols")
    print("------------------------------------")

#Encrypt plaintext 
newList = []
def stringToList(plainText):
   
    for x in plainText:
        newList.append(x)
    print("newList: ")
    
    
#countML = 0
#countAlphaLetter = 0
def encMessage(newList):
    for messageLetter in newList:
        countML = 0
        for alphaLetter in alphabet:
            countAlphaLetter = 0
            if messageLetter == alphaLetter:
                
                countML =+ 1
                #countAlphaLetter =+ 1
                print("messageLetter")
                print(messageLetter)

                confirm = "counting"
                print(confirm)
                print("countML")
                print(countML)
            countAlphaLetter =+ 1
            print("countalphaLetter")
            print(countAlphaLetter)

    print("List")
    print(newList)



subKey(alphabet)
stringToList(plainText)
encMessage(newList)
encMessage(plainText)