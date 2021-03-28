
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:13:56 2021

"""
# takes IV and generate a key stream with the length of 2^m-1
def stream_generator(m, iv):
    stream = '01010' #store keystream
    stream_len=pow(2, m)-1
    #perform bitwise operation using the recurrence relation
    #z=z0 + z3 mod 5

    while len(stream)<pow(2, m)-1:
        bit = int(iv[0]) ^ int(iv[3])
        stream+=str(bit)
        #shift iv
        iv = iv[1:]
        iv+=str(bit)
        
    return stream
    
# prepare keystream array for bitwise operation
def pad_key(msg, stream):
    # pad the keystream
    multiple = len(msg)//len(stream)
    remainder = len(msg)%len(stream)

    new_stream = ''
    for i in range(multiple):
        new_stream += stream
    
    new_stream = new_stream + stream[:27]
    return new_stream

# process the ciphertext for bitwise operation
def process_msg(msg, stream):
    ptxt_bits = ''

    for i in range(len(msg)):
        temp = int(msg[i]) ^ int(stream[i])
        ptxt_bits+=str(temp)

    return ptxt_bits

def decrypt(msg_bits):
    a_dict='abcdefghijklmnopqrstuvwxyz ?!.\'$'
    ptxt=''
    for i in range(0, len(msg_bits), 5):
        bits=msg_bits[i:i+5]
        char=int(bits, 2)
        ptxt+=a_dict[char]
    return ptxt   


if __name__ == '__main__':
    msg='011011010101101001000010110110010001000001011001011010110101010100010110110111001110100111110110111110110101010000101111'
    iv = '01010'
    m=5
    stream=stream_generator(m, iv)

    keystream = pad_key(msg, stream)
    print('Keystream: '+ keystream)

    bits=process_msg(msg, keystream)

    ptxt = decrypt(bits)
    
    print('Plaintext: ' + ptxt)