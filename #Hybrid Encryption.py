#Hybrid Encryption
#public key + symmetric key

import random, math
import secrets
from Crypto.Cipher import AES


#generate prime numbers
def generatePrime(keysize):
    while True:
        num = random.randrange(2**(keysize -1), 2**(keysize))
        if isPrime(num):
            return num

def isPrime(num):
    a=2
    while a<=math.sqrt(num):
        if num%a<1:
            return False
        a=a+1
    return num>1

#euclid's alg
def gcd(a,b):
    while b != 0:
        temp =  a % b
        a = b
        b = temp
    return a


#Euclid's extended alg
def multiplicativeInverse(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a
    ob = b
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa
    return lx 
    
def KeyGen(size=8):
    #generate prime numbers p,q with same size
    p=generatePrime(size)
    q=generatePrime(size)

    if p == q:
        raise ValueError('p, q cannot be ==')

#calculate n = pq & phi = (p-1)(q-1)
    n = p * q
    phi = (p - 1) * (q - 1)


#select random integer 1<e<phi ==>gcd(e,phi)=1
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        g = gcd(e, phi)

#compute unique integer d
# 1<d<phi
    d = multiplicativeInverse(e, phi)

#public key (e, n)
#private key (d, n)
    return ((n, e), (d, n))


#encrypt
def encrypt(ku, plaintext):
    n, e = ku
#c = m^e(mod n)
    c = [(ord(character) ** e) % n for character in plaintext]
    print(c)

#decrypt
def decrypt(kr, ciphertext):
    d, n = kr
#m=c^d(mod n)
    m = [chr((character ** d) % n) for character in ciphertext]
    return m


def encryptAES(cipherAESe, plaintext):
    return cipherAESe.encrypt(plaintext.encode("utf-8"))

def decryptAES(cipherAESd, ciphertext):
    dec = cipherAESd.decrypt(ciphertext).decode('utf-8')
    return dec 



def main():
    
    print("encrypt and decrypt with AES and RSA")
    print("******************************************************************")
   
    #Generate key
   
    print("Generating RSA public and Privite keys")
    pub,pri=KeyGen()

    #2.	Generates symmetric key for data encapsulation scheme.
    print("Generating AES symmetric key")
    key = secrets.token_hex(16)
    print("AES Symmetric Key: ")
    print(key)
    KeyAES=key.encode('utf-8')

    #3.	Encrypts m  with data encapsulation scheme, using symmetric key just generated.
    plainText = input("Enter the message: ")
    cipherAESe = AES.new(KeyAES,AES.MODE_GCM)
    nonce = cipherAESe.nonce
    print("Encrypting the message with AES......")
    cipherText=encryptAES(cipherAESe,plainText)
    print("AES cypher text: ")
    print(cipherText)


    #4.	Encrypt symmetric key with key encapsulation scheme
    cipherKey=encrypt(pub,key)
    print("Encrypting the AES symmetric key with RSA......")
    print("Encryted AES symmetric key")
    print(cipherKey)
    
    
    #To decrypt 

    #1.	Uses her private key to decrypt the symmetric key contained in the key encapsulation segment.
    decriptedKey=''.join(decrypt(pri,cipherKey))
    print("Decrypting the AES Symmetric Key...")
    print("AES Symmetric Key:")
    print(decriptedKey)

    #2.	Uses this symmetric key to decrypt the message contained in the data encapsulation segment.
    decriptedKey=decriptedKey.encode('utf-8')
    cipherAESd = AES.new(decriptedKey, AES.MODE_GCM, nonce=nonce)
    decrypted=decryptAES(cipherAESd,cipherText)
    print("Decrypting the message using the AES symmetric key.....")
    print("decrypted message: ")
    print(decrypted)
    
    
    input('Press ENTER to exit')

    

if __name__ == "__main__":
    main()
