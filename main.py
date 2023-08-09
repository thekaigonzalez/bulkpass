# passwrod generator in bulk amount
from zxcvbn import zxcvbn

import string
import os
import pathlib
import time

drive_letter = input("bkpass: enter drive letter: ") + ":"
password_letter_max = int(input("bkpass: password length range: "))+1
password_amount = int(input("bkpass: amount of passwords per master: "))

# third time i reused this code lol
def generate_password(len):
    """
    Generates a password

    When this algorithm is run, it will use a range with 1-9, [a-Z], and extra symbols, and create
    an array based on that string, then it will check the length, and continue adding random characters from the
    character array.
    
    """
    import random

    length = 0

    # by default it will only guess lowercase passwords
    rand = string.ascii_lowercase + string.punctuation + string.digits + string.ascii_uppercase
    rage = [ch for ch in rand]
    gen = ""

    while (length < len):
        letter = random.choice(rage)
        while letter in gen:
            letter = random.choice(rage)
        gen += letter;
        length += 1

    return gen

# if the DLETTER/passwords directory doesn't exist create it
if not pathlib.Path("{}/passwords".format(drive_letter)).exists():
    os.mkdir("{}/passwords".format(drive_letter))
    print("bpass: directory of passwords made") # log

txt = ""

for c in range(1, password_letter_max): # iterate TWENTY SIX (TWENTY FIVE) times
    if not (pathlib.Path("{}/passwords/{}".format(drive_letter, c)).exists()): # if the directory {NUMBER} does not exist, create it 
        os.mkdir("{}/passwords/{}".format(drive_letter, c)) # create it
    if (c == 15):
        print("bkpass: on the {}th password".format(c))
    for i in range(password_amount):
        pass_word = generate_password(c)
        txt += "{} | password {}\n".format(pass_word, i)

        # os.system("cls")
        # print("password " + pass_word)
        # time.sleep(0.1)

    pask = open("{}/passwords/{}/master.txt".format(drive_letter, c), "w")
    pask.write(txt);
    pask.close()
    txt = ""
print("bkpass: done!")

input("any key to exit review... ")
