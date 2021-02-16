#!/usr/bin/env python3

###############################################################
## HASH CRACKER V1.0 ##
## MADE BY VLDG ##
## SUPORTED ALGORITHMS: MD5, SHA1, SHA-256, SHA-384, SHA-512 ##
## I WILL ADD MORE ALGORITHMS IN NEXT VERSION ##
###############################################################

###############
## ATTENTION ##
###############

######################################################################################
## THIS IS WORKING ONLY WITH UTF-8 ENCODED WORDLISTS, NO SPECIAL CHARATERS ACCEPTED ##
######################################################################################

######################################################################################################################################
## ROCKYOU WORDLIST CLEANED & ENCODED IN UTF-8 > https://drive.google.com/file/d/1WTnZL3-ptbZvmtNPfKplF0G8d46qaOnw/view?usp=sharing ##
######################################################################################################################################

##############################################
## ALSO IM BEGGINER, IM OPEN TO SUGGESTIONS ##
##############################################

#############
## MODULES ##
#############

import pyfiglet
import sys
import os
from termcolor import colored
import time
import hashlib as hl

############
## BANNER ##
############

title = 'HASH-CRACKER'
authtitle = 'by VLDG'
banner = pyfiglet.figlet_format(title, font='slant', justify='center')
author = pyfiglet.figlet_format(authtitle, font='digital', justify='center')

##############
##  SCRIPT  ##
##############

os.system('clear')
print(colored(banner, 'green'))
print(colored(author, 'green'))
print(colored('''
Select hash algorithm:
\t1 - MD5 
\t2 - SHA1
\t3 - SHA-256
\t4 - SHA-384
\t5 - SHA-512
''', 'magenta'))
algo = input(colored('>>>: ', 'magenta'))

if algo == '1':
    hashstring = input(colored("Please input your hash >>>: ", 'yellow'))
    wordfile = input(colored("Wordlist Path here >>>: ", 'yellow'))
    words = open(wordfile, "r")
    words = words.readlines()
    print(len(words), "words")
    file=open('cracked.txt', 'a')
    for word in words:
        hashc = hl.md5(word.encode('utf-8')[:-1])
        val = hashc.hexdigest()
        if hashstring == val:
            print("Password is:",word)
            print(colored("Password saved in cracked.txt", 'green'))
            file.write("\n Cracked Hashes\n\n")
            file.write("MD5\t" + hashstring+"\t>\t")
            file.write(word+"\n")
elif algo == '2':
    hashstring = input(colored("Please input your hash >>>: ", 'yellow'))
    wordfile = input(colored("Wordlist Path here >>>: ", 'yellow'))
    words = open(wordfile, "r")
    words = words.readlines()
    print(len(words), "words")
    file=open('cracked.txt', 'a')
    for word in words:
        hashc = hl.sha1(word.encode('utf-8')[:-1])
        val = hashc.hexdigest()
        if hashstring == val:
            print("Password is:",word)
            print(colored("Password saved in cracked.txt", 'green'))
            file.write("\n Cracked Hashes\n\n")
            file.write("SHA1\t" + hashstring+"\t>\t")
            file.write(word+"\n")

elif algo == '3':
    hashstring = input(colored("Please input your hash >>>: ", 'yellow'))
    wordfile = input(colored("Wordlist Path here >>>: ", 'yellow'))
    words = open(wordfile, "r")
    words = words.readlines()
    print(len(words), "words")
    file=open('cracked.txt', 'a')
    for word in words:
        hashc = hl.sha256(word.encode('utf-8')[:-1])
        val = hashc.hexdigest()
        if hashstring == val:
            print("Password is:",word)
            print(colored("Password saved in cracked.txt", 'green'))
            file.write("\n Cracked Hashes\n\n")
            file.write("SHA-265\t" + hashstring+"\t>\t")
            file.write(word+"\n")
    
elif algo == '4':
    hashstring = input(colored("Please input your hash >>>: ", 'yellow'))
    wordfile = input(colored("Wordlist Path here >>>: ", 'yellow'))
    words = open(wordfile, "r")
    words = words.readlines()
    print(len(words), "words")
    file=open('cracked.txt', 'a')
    for word in words:
        hashc = hl.sha384(word.encode('utf-8')[:-1])
        val = hashc.hexdigest()
        if hashstring == val:
            print("Password is:",word)
            print(colored("Password saved in cracked.txt", 'green'))
            file.write("\n Cracked Hashes\n\n")
            file.write("SHA-384\t" + hashstring+"\t>\t")
            file.write(word+"\n")  

elif algo == '5':
    hashstring = input(colored("Please input your hash >>>: ", 'yellow'))
    wordfile = input(colored("Wordlist Path here >>>: ", 'yellow'))
    words = open(wordfile, "r")
    words = words.readlines()
    print(len(words), "words")
    file=open('cracked.txt', 'a')
    for word in words:
        hashc = hl.sha512(word.encode('utf-8')[:-1])
        val = hashc.hexdigest()
        if hashstring == val:
            print("Password is:",word)
            print(colored("Password saved in cracked.txt", 'green'))
            file.write("\n Cracked Hashes\n\n")
            file.write("SHA-512\t" + hashstring+"\t>\t")
            file.write(word+"\n")

else:
    os.system('clear')
    print(colored(banner, 'green'))
    print(colored(author, 'green'))
    print(colored('Option not found!', 'yellow'))
    print(colored('Exiting...', 'red'))
    time.sleep(2)
    sys.exit()