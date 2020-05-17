#!/bin/python3
import os
from getpass import getpass

arr = [9781492051718,
       9780135560396,
       9781492057680,
       9781491903063,
       9781788472906,
       9781491922996]

email = input("Enter email: ")
password = getpass()

for elem in arr:
    print(elem)
    os.system('python3 safaribooks.py --cred' + ' "' +
              email + ':' + password + '" ' + str(elem))
