import random

s = "ABCDEFGHIJKL\MNOPQRSTUVWXYZ1234\567890abcdefghijklm\nopqrstuvwxyz!@#$%^&*\()_-+[]{};:'/',."
passwordlen = 8
password = "".join(random.sample(s,passwordlen))
print (password)

""" PASSWORD GENERATOR BY DIVYESH PERLA """
