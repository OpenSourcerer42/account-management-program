import csv
import os
import pyAesCrypt
import Encryption as EncryptionFunction

def Add(filename, Encryptpassword):
    bufferSize = 64 * 1024
    password = input("enter the password for the file to decrypt it: \n")
    pyAesCrypt.decryptFile(filename+".aes",filename, password, bufferSize)
    os.remove(filename+".aes")
    #delete the old encrypted file, hide the decrypted file and once you add something to it, encrypt the new csv file
    rowIndex = 0
    with open(filename, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=",")
        for rows in reader:
            rowIndex = int(rows[0])
            rowIndex += 1
        csvFile.close()
            
    username = input("enter username you want to add: \n")
    password = input("enter password you want to add: \n")
    print(str(rowIndex)+username+password)
    csvFile = open(filename, "a")
    csvFile.write("\n"+str(rowIndex)+","+username+","+password)
    csvFile.close()
    EncryptionFunction.Encrypt()
    os.remove(filename)
    
def Edit(filename):
    print(filename)

def Delete(filename):
    bufferSize = 64 * 1024
    password = input("enter the password for the file to decrypt it: \n")
    pyAesCrypt.decryptFile(filename+".aes",filename, password, bufferSize)
    os.remove(filename+".aes")

    delUserName = input("enter the username of the account you want to delete")
    
    with open(filename, 'r+') as csvFile:
        reader = csv.reader(csvFile, delimiter=",")
        writer = csv.writer(csvFile, delimiter=",")
        for rows in reader:
            if rows[1] == delUserName:
                writer.writerow("")
    #find a way to delete just a line from the csv file and not the entire file itself
    EncryptionFunction.Encrypt()
    os.remove(filename)
    