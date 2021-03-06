import socket
import os
import random

socketServerName = "localhost"
socketServerPN = 7002
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = (socketServerName, socketServerPN)
print('client started')

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def generate_n_qn():
    
    p  = 941
    q = 7907
    output2 = 1653
    output3 = 89917
    output1 = p * q
    return output1, output2, output3


def encryption(input, key, n):
    Cipher = ''
    integer_conv = [ord(i) for i in input]
    for i in integer_conv:
        CipherExp = str((pow(i, key)) % n).zfill(8)
        Cipher +=  CipherExp
    return Cipher
	
def decryption(input, key, n):
    reply = ''
    Parsed_Cipher = [input[i:i+8] for i in range(0, len(input), 8)]
    for i in Parsed_Cipher:
        plain_exp = chr((pow(int(i), key)) % n)
        reply += plain_exp
    return reply
	


while 1:
    message = raw_input("Enter the message: ")
    len_key = 1024
    n, e, d = generate_n_qn()
    for i in message:
    	encryption_data  = encryption(message, e, n)
    socketClient.sendto(encryption_data, addr)                   #send the packet to server if the above 'if' condition is not satisfied
    print ('client sending message to server')
    response, addr = socketClient.recvfrom(1024)                # using the recvfrom function the data and the address is stored in the Imagedata and addr variables                          
    print ('message received from server')
    decryption_data = decryption(response, d, n)
    print "message is:",decryption_data

    	
socketClient.close()






