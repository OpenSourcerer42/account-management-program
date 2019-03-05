import csv
import pyAesCrypt

def Add(filename):
    bufferSize = 64 * 1024
    ans = input("is the file being used encrypted Yes(1) or No(2) \n")
    
    if int(ans) == 1:
        password = input("enter the password for the file to decrypt it")
        pyAesCrypt.decryptFile(filename+".aes",filename, password, bufferSize)

        rowIndex = 0
        with open("details.csv", 'r') as csvFile:
            reader = csv.reader(csvFile, delimiter=",")
            for rows in reader:
               rowIndex = int(rows[0])
            rowIndex += 1
            csvFile.close()
            
        username = input("enter username")
        password = input("enter password")
        print(str(rowIndex)+username+password)
        #find a way to hide the decrypted file when adding a username and password to increase security
        csvFile = open(filename, "a")
        csvFile.write("\n"+str(rowIndex)+","+username+","+password)
        csvFile.close()

    elif int(ans) == 2:
        rowIndex = 0
        with open("details.csv", 'r') as csvFile:
            reader = csv.reader(csvFile, delimiter=",")
            for rows in reader:
               rowIndex = int(rows[0])
            rowIndex += 1
            csvFile.close()

        username = input("enter username")
        password = input("enter password")
        print(str(rowIndex)+username+password)

        csvFile = open(filename, "a")
        csvFile.write("\n"+str(rowIndex)+","+username+","+password)
        csvFile.close()

def Edit(filename):
    print(filename)

def Delete(filename):
    print(filename)
