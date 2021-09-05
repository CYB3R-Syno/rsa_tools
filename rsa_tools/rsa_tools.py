#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import getcwd

import argparse

from subprocess import call

from attacks import Attack
from tools import Tool

import readline

# Accueil

def accueil(arg):

	if arg == "first":

		call(["clear"], shell=True)
		
		print("\n")
		print("\t\t########################################################")
		print("\t\t# Options:                                             #")
		print("\t\t#                  ==== Wiener ====                    #")
		print("\t\t#                [1]: Wiener Attack                    #")
		print("\t\t#                                                      #")
		print("\t\t#                 ==== RSA Cipher ====                 #")
		print("\t\t#             [2]: RSA Ciphertext Decipher             #")
		print("\t\t#             [3]: RSA Ciphertext Encipher             #")
		print("\t\t#             [0]: Quit                                #")
		print("\t\t########################################################")
		print("\n\n")

		print("\n\t\t [*] Please select from your selections (0-3)")
		return input("\t\t > ")


	elif arg == "again":

		print("\n\t\t [*] Please enter the select from your selections (0-3)")
		return input("\t\t > ")

# Fonction de traitement et de lancement

def choose(arg):

	attack = str(accueil(arg))

	if attack == "1":

		print("\n\t\t\t ===== Wiener Attack =====")

		args = input("\n\t\t[*] Arguments ([-h] -n modulus -e exponent):\n\n\t\t\t").split()

		parser = argparse.ArgumentParser(description='This program allows to carry out a Wiener Attack')
		parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
		parser.add_argument('-e', dest='e',type=int,help='RSA public key exponent',required=True)

		params=parser.parse_args(args)

		attack_object = Attack(params)
		attack_object.wiener()


	elif attack == "2":

		print("\n\t\t\t ===== RSA Decrypto =====")

		try:

			args = input("\n\t\t[*] Argument ([-h] -n modulus -d private_exponent -c ciphertext):\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()

		parser = argparse.ArgumentParser(description='This simple program allows to decipher a message using RSA')
		parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
		parser.add_argument('-d', dest='d',type=int,help='RSA private key exponent',required=True)
		parser.add_argument('-c', dest='c',type=int,help='ciphertext',required=True)
		params=parser.parse_args(args)

		tool_object = Tool(params)
		tool_object.decipher()

	elif attack == "3":

		print("\n\t\t\t ===== RSA Encrypto =====")

		try:

			args = input("\n\t\t[*] Argument ([-h] -n modulus -e public_exponent -p plaintext):\n\n\t\t\t").split()

		except:

			print("\n\t\t\t[-] Argument Error: Please verify your inputs\n")
			exit()

		parser = argparse.ArgumentParser(description='This simple program allows to encipher a message using RSA')
		parser.add_argument('-n', dest='n',type=int,help='RSA public key modulus',required=True)
		parser.add_argument('-e', dest='e',type=int,help='RSA public key exponent',required=True)
		parser.add_argument('-p', dest='p',type=int,help='plaintext',required=True)
		params=parser.parse_args(args)

		tool_object = Tool(params)
		tool_object.encipher()

	else:

		choose("again")

# Main

if __name__ == "__main__":

	choose("first")

