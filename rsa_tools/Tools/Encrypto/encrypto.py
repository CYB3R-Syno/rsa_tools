#!/usr/bin/python3

# RSA Encipher

import sys
import argparse

class Encipher(object):

  # Accueil

  def accueil(self):

    print ("\n")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\t\t      RSA Encipher       ")
    print ("\t\t       CYB3R_Syno        ")
    print ("\t\t    GNU GPL v3 License   ")
    print ("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~")
    print ("\n")

  def __init__(self,n,e,p):

    c = pow(p,e,n)

    print("\t[+] The ciphertext is: {}\n".format(c))
  
