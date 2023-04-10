import sys
import os
import io

#import pycriptodome

from Crypto.Cipher import AES
import hashlib
from datetime import datetime

def cifrar(filename, key):
  
    clave_n = hashlib.sha256(key.encode("utf-8")).digest()
    os.system("cls")
    print("\n\nTrabajando en el cifrado\nEspera un momento...")
    try:    
        with open(filename, "rb") as file:
            orig_file = file.read()
            
        while len(orig_file) % 16 != 0:
            orig_file = orig_file + b'0'
            
        cipher = AES.new(clave_n, AES.MODE_GCM)
        encrypted_message, tag = cipher.encrypt_and_digest(orig_file)
        nonce = cipher.nonce
        root, tipo = os.path.splitext(filename)
        #print(tipo+"\n\n")
        filename = filename[:len(filename)-len(tipo)]
        with open(filename+".encrypted", "wb") as e:
            e.write(nonce)
        with open(filename+".encrypted", "ab") as e:
            e.write(tag)
        with open(filename+".encrypted", "ab") as e:
            e.write(encrypted_message)
        os.system("cls")
        print("\n\nProceso finalizado")
        return "Hecho", filename+".encrypted"
    except ValueError:
        return "Error", filename
    

def descifrar(filename, key, tipo):

    clave_n = hashlib.sha256(key.encode("utf-8")).digest()
    with open(filename, "rb") as file:
        encripted_file = file.read()
    
    nonce = encripted_file[:16]
    tag = encripted_file[16:32]
    doc_encript = encripted_file[32:]
    #print(len(encripted_file))
    #print(len(nonce))
    #print(len(tag))
    #print(encripted_file)
    fecha = datetime.today().strftime('%d-%m-%Y_%H-%M-%S')
    cipher = AES.new(clave_n, AES.MODE_GCM, nonce)
    os.system("cls")
    print("\n\nTrabajando en el descifrado\nEspera un momento...")
    try:
        decrypted_file = cipher.decrypt_and_verify(doc_encript, tag)
        with open(filename[:len(filename)-10]+fecha+tipo, "wb") as df:
            df.write(decrypted_file.rstrip(b'0'))
        os.system("cls")
        print("\n\nProceso finalizado\n")
        return "Hecho", filename[:len(filename)-10]+fecha+tipo
    except ValueError:
        return "Error", filename
    
def cifrar_grab(file, rgb):
    clave_n = hashlib.sha256(rgb.encode("utf-8")).digest()
    try:    
        with open(file, "rb") as file:
            orig_file = file.read()
            
        while len(orig_file) % 16 != 0:
            orig_file = orig_file + b'0'
            
        cipher = AES.new(clave_n, AES.MODE_GCM)
        encrypted_message, tag = cipher.encrypt_and_digest(orig_file)
        nonce = cipher.nonce
        ciphertext = nonce+tag+encrypted_message
   
        return ciphertext
    except ValueError:
        return "E"
    
def descifrar_grab(file, rgb):
    clave_n = hashlib.sha256(rgb.encode("utf-8")).digest()

    nonce = file[:16]
    tag = file[16:32]
    doc_encript = file[32:]
    #print(len(encripted_file))
    #print(len(nonce))
    #print(len(tag))
    #print(encripted_file)
    cipher = AES.new(clave_n, AES.MODE_GCM, nonce)
    try:
        decrypted_file = cipher.decrypt_and_verify(doc_encript, tag)
        return decrypted_file
    except ValueError:
        return "E"