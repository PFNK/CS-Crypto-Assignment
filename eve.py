import sys, os, time
sys.path.append('/afs/inf.ed.ac.uk/group/teaching/compsec/cw2/mitm')
from common import *
from const import *

b_dir = Template('/tmp/$usr/').substitute(usr = getpass.getuser())
os.rename(b_dir + BUFFER_FILE_NAME, b_dir + 'buffer_original')
chat_type = sys.argv[1]
dialog = Dialog('print')

socket_to_bob, aes_to_bob = setup('alice', BUFFER_DIR, 'buffer_original')
socket_to_alice, aes_to_alice = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)

if chat_type == '--custom':
    dialog.prompt('Please input what you would like Alice to say to Bob: ')
    to_send_to_alice = input()
    encrypt_and_send(to_send_to_alice, aes_to_bob, socket_to_bob)

    dialog.prompt('Please input what you would like Bob to say to Alice: ')
    to_send_to_bob = input()
    encrypt_and_send(to_send_to_bob, aes_to_alice, socket_to_alice)


elif chat_type == '--break-heart':
    to_send_to_alice = BAD_MSG['alice']
    encrypt_and_send(to_send_to_alice, aes_to_bob, socket_to_bob)

    to_send_to_bob = BAD_MSG['bob']
    encrypt_and_send(to_send_to_bob, aes_to_alice, socket_to_alice)

else:
    to_send_to_alice = receive_and_decrypt(aes_to_alice, socket_to_alice)
    encrypt_and_send(to_send_to_alice, aes_to_bob, socket_to_bob)

    to_send_to_bob = receive_and_decrypt(aes_to_bob, socket_to_bob)
    encrypt_and_send(to_send_to_bob, aes_to_alice, socket_to_alice)

