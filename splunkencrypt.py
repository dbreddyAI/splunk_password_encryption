#Thanks to TZK for this post which gave me a great head start: http://maratto.blogspot.com/2016/03/
#rc4 code obtained from https://raw.githubusercontent.com/jbremer/rc4 #Copyright (C) 2016-2017 Jurriaan Bremer.

import base64
import sys
import os


def encrypt(plaintext,splunk_secret):
    
    rc4key = splunk_secret[0:16]
    pwd = plaintext + '\0'
    ciphertext = rc4(pwd,rc4key)
    
    return '$1$' + ciphertext.encode('base64').strip()
    
    

def decrypt(ciphertext,splunk_secret):

    rc4key = splunk_secret[0:16]
    plaintext = rc4(ciphertext[3:].decode('base64'),rc4key).strip('\0')
    
    return plaintext


def encrypt_pass4SymmKey(plaintext,splunk_secret):
    
    rc4key = splunk_secret[0:16]
    
    xorkey = 'DEFAULTSA'
    xorkey = (xorkey*(len(plaintext)/9 + 1))[0:len(plaintext)+1]
    pwd = [x[0] ^ x[1] for x in zip(unpack(plaintext),unpack(xorkey))]
    pwd.append(0)
    pwd = pack(pwd)
    
    ciphertext = rc4(pwd,rc4key)
    
    return '$1$' + ciphertext.encode('base64').strip()
    
    

def decrypt_pass4SymmKey(ciphertext,splunk_secret):

    rc4key = splunk_secret[0:16]
    
    plaintext = rc4(ciphertext[3:].decode('base64'),rc4key)
    #.strip('\0')
    
    xorkey = 'DEFAULTSA'
    xorkey = (xorkey*(len(plaintext)/9 + 1))[0:len(plaintext)-1]
    plaintext = [x[0] ^ x[1] for x in zip(unpack(plaintext),unpack(xorkey))]
    plaintext = pack(plaintext)
    
    return plaintext


def generate_splunk_secret():
    return os.urandom(255).encode("base64").strip().replace("+",".")

def unpack(text):
    return [ord(c) for c in text]
    
def pack(list):
    return ''.join([chr(i) for i in list])

def rc4(data, key):
    """RC4 encryption and decryption method."""
    S, j, out = list(range(256)), 0, []

    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    for ch in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(chr(ord(ch) ^ S[(S[i] + S[j]) % 256]))

    return "".join(out)