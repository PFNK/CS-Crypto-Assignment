import sys, os, time
from common import *
from const import *

os.rename(BUFFER_DIR + '/' + BUFFER_FILE_NAME, BUFFER_DIR + '/' + 'buffer_original')
chat_type = sys.argv[1]
dialog = Dialog('print')

socket_to_bob, aes_to_bob = setup('alice', BUFFER_DIR, 'buffer_original')
socket_to_alice, aes_to_alice = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)

# to_send_to_bob = receive_and_decrypt(aes_to_bob, socket_to_bob)
# to_send_to_alice = receive_and_decrypt(aes_to_alice, socket_to_alice)

if chat_type == '--custom':
    #receive true message from alice to bob
    to_send_to_bob = receive_and_decrypt(aes_to_alice, socket_to_alice)
    #get the custom message from user
    dialog.prompt('Please input what you would like Alice to say to Bob: ')
    to_send_to_bob = input()
    #send custom message to bob
    encrypt_and_send(to_send_to_bob, aes_to_bob, socket_to_bob)

    #receive true message from bob to alice
    to_send_to_alice = receive_and_decrypt(aes_to_bob, socket_to_bob)
    #get the custom message from user
    dialog.prompt('Please input what you would like Bob to say to Alice: ')
    to_send_to_alice = input()
    #send custom message to alice
    encrypt_and_send(to_send_to_alice, aes_to_alice, socket_to_alice)


elif chat_type == '--break-heart':
    #receive true message from alice to bob
    to_send_to_bob = receive_and_decrypt(aes_to_alice, socket_to_alice)
    #get the alice's bad message
    to_send_to_bob = BAD_MSG['alice']
    #send alice's bad message to bob
    encrypt_and_send(to_send_to_bob, aes_to_bob, socket_to_bob)

    #receive true message from bob to alice
    to_send_to_alice = receive_and_decrypt(aes_to_bob, socket_to_bob)
    #get the bob's bad message
    to_send_to_alice = BAD_MSG['bob']
    #send bob's bad message to alice
    encrypt_and_send(to_send_to_alice, aes_to_alice, socket_to_alice)

else:
    #receive true message from alice to bob
    to_send_to_bob = receive_and_decrypt(aes_to_alice, socket_to_alice)
    #sent the true message from alice to bob
    encrypt_and_send(to_send_to_bob, aes_to_bob, socket_to_bob)

    #receive true message from bob to alice
    to_send_to_alice = receive_and_decrypt(aes_to_bob, socket_to_bob)
    #sent the true message from bob to alice
    encrypt_and_send(to_send_to_alice, aes_to_alice, socket_to_alice)


tear_down(socket_to_bob, BUFFER_DIR, 'buffer_original')
tear_down(socket_to_alice, BUFFER_DIR, BUFFER_FILE_NAME)
