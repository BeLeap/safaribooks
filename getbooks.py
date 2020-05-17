#!/usr/bin/python3
import os
from getpass import getpass
import argparse

parser = argparse.ArgumentParser(description='Get Authentication info')
parser.add_argument('--email', help='Your email')
parser.add_argument('--password', help='Your password')
args = parser.parse_args()

email = args.email
if email is None:
    email = input("Email: ")
password = args.password
if password is None:
    password = getpass()

file = open("bookcode.txt", "r")
for code in file:
    print("[INFO]", "Downloading", code)
    os.system('python3 safaribooks.py --cred' + ' "' +
              email + ':' + password + '" ' + code)

file.close()
