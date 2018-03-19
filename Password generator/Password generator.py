#!/usr/bin/env python
# -*- coding: UTF-8 -*-

''' Password generator
    Author: Damir Tešnjak'''

import random

print "----Password generator----"

pass_length = int(raw_input("Length of password (min 5 characters). Type number. "))
num_of_password = int(raw_input("Number of passwords to generate. "))

password = ""

if pass_length < 5:
    print "Password length must be over 5 characthers!"
else:
    for x in range(num_of_password):
        for y in range(pass_length):
            randC = random.randint(0, 1)
            if randC == 0:
                password += chr(random.randint(65, 90)).lower()
            else:
                password += chr(random.randint(65, 90)).upper()
        print "Password: " + password
        password = ""