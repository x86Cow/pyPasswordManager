import string
import random
import base64
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-g", default=0, help="generate password", type=int)
parser.add_argument("-o", action='store_true' , help="view passwords")
parser.parse_args()
args = parser.parse_args()

def passwordGen(i):
  randomStr =   ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(i))
  hash = base64.b64encode(randomStr.encode("utf-8"))
  hash = base64.b64decode(hash).hex()
  return(hash)

def passwordSave(hash, label):
  f = open("password.pass", 'a')
  f.write(label + ": " + hash + '\n')
  f.close()
def passwordOpen():
  f = open("password.pass", 'r')
  return(f.read())
  f.close()

label = "Hello World"
if args.g:
  passwordSave(passwordGen(args.g), label)
if args.o:
  print(passwordOpen())