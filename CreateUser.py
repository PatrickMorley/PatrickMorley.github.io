#Patrick Morley
#Create User

import random
import os
import sys
import crypt
import re

def createUserName(line):
    x = line.find(" ")
    line = line[0] + line[x:]
    line = line.replace(' ', '')
    line = line.replace('-', '')
    line = line.replace('\'', '')
    line = line.replace('\n', '')
    line = line.lower()
    return line

def createPassword():
    dictionary = ['bucket', 'volleyball', 'loaf', 'cycle', 'daffy', 'demonic', 'cobweb', 'carriage', 'sound', 'winter', 'button']
    firstWord = random.choice(dictionary)
    secondWord = random.choice(dictionary)
    randnum = random.randint(1000, 9999)
    password = (firstWord.lower() + str(randnum) + secondWord.upper())
    return password

with open("UserNamesLvl1", 'r') as namesfile:
    for line in namesfile:
        username = createUserName(line)
        newpassword = createPassword()
        with open("UsersLvl1", 'a') as usersfile:
            usersfile.write("username: " + username + " password: " + newpassword + "\n")
            encPass = crypt.crypt(newpassword, "22")
            os.system("useradd p " + encPass + " " + username)
            regex = (r"\b[a-z[a-z0-9]*\b")
            if re.search(regex, username):
                match = re.search(regex, username)
                print("username valid")
            else:
                print("username invalid")
                
                    
