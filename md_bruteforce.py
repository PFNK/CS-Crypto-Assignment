import hashlib


f = open('/afs/inf.ed.ac.uk/group/teaching/compsec/cw2/password-cracking/rockyou-samples.md5.txt')
file_passwords = {}
cracked_passwords = {}
for l in f:
    l = l.strip()
    if l in file_passwords.keys():
        file_passwords[l] += 1
    else:
        file_passwords[l] = 1

f.close()
symbols = list('0123456789abcdefghijklmnopqrstuvwxyz')

for a in symbols:
    for b in symbols:
        for c in symbols:
            for d in symbols:
                for e in symbols:
                    password = "".join([a,b,c,d,e])
                    hashed_pass = hashlib.md5(password.encode()).hexdigest()
                    if hashed_pass in file_passwords.keys():
                         cracked_passwords[password] = file_passwords[hashed_pass]


f = open("md5_decrypted.txt", "w")

for key, val in cracked_passwords.items():
    f.write("{},{}\n".format(key,val))

f.close()
