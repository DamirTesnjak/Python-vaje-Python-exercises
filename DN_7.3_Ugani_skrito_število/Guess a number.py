#!/usr/bin/env python
# -*- coding: UTF-8 -*-


''' Ugani število
    Author: Damir Tešnjak'''

import random

print("\n----Uganite število----")

# Naključno iskno število
secret = random.randint(1, 50)

# Input
guess = int( raw_input( "\nVaše ugibajoče število (1-50): " ) )

# Pogoji in izpis
if secret == guess and guess >= 1 and guess <= 50:
    print "\nZmagali ste! Uganili ste število " + str( secret )

elif secret != guess and guess >= 1 and guess <= 50:
    print "\nIzgunbili ste! Uganiti ste morali število " + str( secret )

else:
    print "\nNapaka! Vnesli ste število izven intervala"
