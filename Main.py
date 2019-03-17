import csv
import os
import Encryption as EncryptFunction
import Operations as ops

def checkdetails():
    username = input("please enter your username: \n")
    password = input("please enter your password: \n")
    filename = "details.csv"
    os.system("clear")
    EncryptFunction.Decrypt(filename+".aes")

    #reads csv file 
    with open(filename, "r") as details_file:
        continueTo = False
        reader = csv.reader(details_file, delimiter=",")
        #reads each line which has a username and password and compares to use input
        for line in reader:
            if username == line[0] and password == line[1]:
                continueTo = True
                os.remove("details.csv")
        if continueTo == False:
            tryAgain = input("incorrect details, try again yes(1) or no(2) \n")
            if tryAgain == '1':
                checkdetails()
            else:
                EncryptFunction.Encrypt(filename)
                os.remove(filename)
        elif continueTo == True:
            if "admin" in username:
                os.system("clear")
                AdminPanel(username, filename)
            else:
                os.system("clear")
                UserPanel(username)

def AdminPanel(usrName, filename):
    print("Welcome to the software: " + usrName)
    operationAns = input("What action would you like to perform on the csv file: \n\n1.Add an account \n2.Delete an account \n3.Edit an account\n")

    if operationAns == '1':
        ops.Add(filename)
    elif operationAns == '2':
        ops.Delete(filename)
    elif operationAns == '3':
        ops.Edit(filename)
    else:
        print("Error: incorrect input, please enter with 1, 2 or 3 \n")
        AdminPanel(usrName, filename)

def UserPanel(usrName):
    print("welcome to the software: " + usrName)
    


checkdetails()
