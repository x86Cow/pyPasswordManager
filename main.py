import string
import random
import base64

def passwordGen(i):
  randomStr =   ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(i))
  hash = base64.b64encode(randomStr.encode("utf-8"))
  hash = base64.b64decode(hash).hex()
  return(hash)

def passwordSave(hash):
  f = open("password.pass", 'a')
  f.write(hash + '\n')
  f.close()
def passwordOpen():
  f = open("password.pass", 'r')
  return(f.read())
  f.close()

encryptedPass = passwordGen(20)
passwordSave(encryptedPass)
print(passwordOpen())