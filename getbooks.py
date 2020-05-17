#!/usr/bin/python3
import os
from getpass import getpass

email = input("Email: ")
password = getpass()

file = open("bookcode.txt", "r")
for code in file:
    print("[INFO]", "Downloading", code)
    os.system('python3 safaribooks.py --cred' + ' "' +
              email + ':' + password + '" ' + code)

file.close()
