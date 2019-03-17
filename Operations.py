import csv
import os
import pyAesCrypt
import pandas as pd
import Encryption as EncryptionFunction

def Add(filename, Encryptpassword):
    #decrypts the csv file so the user can delete an account
    bufferSize = 64 * 1024
    password = input("enter the password for the file to decrypt it: \n")
    pyAesCrypt.decryptFile(filename+".aes",filename, password, bufferSize)
    os.remove(filename+".aes")
    #prompts user to enter the username and password they want to add to the csv file
    username = input("enter username you want to add: \n")
    password = input("enter password you want to add: \n")
    csvFile = open(filename, "a")
    #appends the username and password with a delimter to the end of the csv file
    csvFile.write(username+","+password)
    csvFile.close()
    #re-encrypts the csv file
    EncryptionFunction.Encrypt()
    os.remove(filename)
    
def Edit(filename):
    print(filename)

def Delete(filename):
    #decrypts the csv file so the user can delete an account
    bufferSize = 64 * 1024
    password = input("enter the password for the file to decrypt it: \n")
    pyAesCrypt.decryptFile(filename+".aes",filename, password, bufferSize)
    os.remove(filename+".aes")

    delUserName = input("enter the username of the account you want to delete")
    #reads the csv file into a pandas data frame
    df = pd.read_csv(filename)
    #checks whether the column "username" contains the username provided by the user
    #if it contains it, it removes that line then dumps the dataframe back into the csv file  
    df = df[~df["username"].str.contains(delUserName, na=False)].to_csv('details.csv', index = False)
    # calls encryption function to re-encrypt the csv file
    EncryptionFunction.Encrypt()
    os.remove(filename)
    