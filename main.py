import string
import random
import base64
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-g", nargs='+', help="generate password")
parser.add_argument("-o", action='store_true', help="view passwords")
parser.parse_args()
args = parser.parse_args()

PASSWORD_FILE = "password.pass"
LABEL = "Hello World"

def password_gen(i):
    'Generate password'
    random_str = ''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits + string.punctuation) for _ in range(i))
    random_hash = base64.b64encode(random_str.encode("utf-8"))
    random_hash = base64.b64decode(random_hash).hex()
    return random_hash


def password_save(password_hash, label):
    'Save password to file'
    with open(PASSWORD_FILE, 'a', encoding='utf-8') as pass_file:
        pass_file.write(label + ": " + password_hash + '\n')


def password_open():
    'Get password from file'
    with open(PASSWORD_FILE, 'r', encoding='utf-8') as pass_file:
        return pass_file.read()


if args.g:
    if len(args.g) == 1:
        password_save(password_gen(8), args.g[0])
    else:
        password_save(password_gen(int(args.g[1])), args.g[0])
if args.o:
    print(password_open())