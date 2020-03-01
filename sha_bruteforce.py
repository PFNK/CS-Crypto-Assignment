import hashlib


f = open('/afs/inf.ed.ac.uk/group/teaching/compsec/cw2/password-cracking/rockyou-samples.sha1-salt.txt')
file_passwords = {}
cracked_passwords = {}
for l in f:
    l = l.strip()
    sha_line = l.split('$') #ll = ['', 'SHA1p', salt, hash]
    if sha_line[3] not in file_passwords.keys():
        file_passwords[sha_line[3]] = sha_line[2]


f.close()

l = ['123456','12345','123456789','password','iloveyou','princess','1234567','rockyou','12345678','abc123','nicole','daniel','babygirl','monkey','lovely','jessica','654321','michael','ashley','qwerty','111111','iloveu','000000','michelle','tigger']

for password in l:
    for salt in file_passwords.values():
        salt_password = salt + password
        hashed_pass = hashlib.sha1(salt_password.encode()).hexdigest()
        if hashed_pass in file_passwords.keys():
            if password in cracked_passwords.keys():
                cracked_passwords[password] += 1
            else:
                cracked_passwords[password] = 1


f = open("sha1_decrypted.txt", "w")

for key, val in cracked_passwords.items():
    f.write("{},{}\n".format(key,val))

f.close()
