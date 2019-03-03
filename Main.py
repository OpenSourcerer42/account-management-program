import csv
import os
import Encryption as EncryptFunction

encryptFile = input("Would you like to encrypt your .csv file (Y)es or (N)o: \n")

if encryptFile == "Y":
    EncryptFunction.Encrypt()

elif encryptFile == "N":
    print("continue to functions")

def welcome():
    print("welcome to the software")

def checkdetails():
    username = input("please enter your username: \n")
    password = input("please enter your password: \n")
    filename = input("Please enter the name of the csv file: \n")  
    DecryptAns = input("Do you need to decrypt the file before using?: \n")
    
    if DecryptAns == "Y":
        EncryptFunction.Decrypt(filename)

    #reads csv file 
    with open(filename, "r") as details_file:
        continueTo = False
        reader = csv.reader(details_file, delimiter=",")

        #reads each line which has a username and password and compares to use input
        for line in reader:
            if username == line[0] and password == line[1]:
                os.remove(filename)
                continueTo = True

        if continueTo == False:
            tryAgain = input("incorrect details, try again yes(1) or no(2)")

            if tryAgain == '1':
                checkdetails()

        elif continueTo == True:
            print("correct details")
            welcome()

checkdetails()
