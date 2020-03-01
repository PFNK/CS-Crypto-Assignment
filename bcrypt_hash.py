import bcrypt


f = open('/afs/inf.ed.ac.uk/group/teaching/compsec/cw2/password-cracking/rockyou-samples.bcrypt.txt')

cracked_passwords = []
i = 1

for l in f:
    if len(cracked_passwords) == 5:
        break
    l = l.strip()
    line = l.split('$') # ['', '2b','12', salt + hash] - salt first 22 chars
    # password = line[3][22:].strip()
    # salt = line[3][:22].strip()
    # p = "123456"
    # hashed = bcrypt.hashpw(p.encode('utf-8'),salt.encode('utf-8'))
    hashed = l.encode('utf-8')
    if bcrypt.checkpw("123456".encode('utf-8'), hashed):
        cracked_passwords.append(i)

    i += 1

f.close()
print(cracked_passwords)
f = open("bcrypt-cracked.txt", "w")

for num in cracked_passwords:
    f.write("{}\n".format(num))

f.close()
