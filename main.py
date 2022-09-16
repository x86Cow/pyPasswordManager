import string
import random

def passwordGen(i):
  randomStr =   ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(i))
  print(randomStr)
passwordGen(20)