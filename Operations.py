import csv
import os
import pyAesCrypt
import pandas as pd
import Encryption as EncryptionFunction

def DoAgain():
    filename = "details.csv"
    ans = input("Would you like to perform any other operation such as Add(1), Edit(2), Delete(3)?, if not just press enter \n")
        
    if ans == "1":
        Add(filename)
    elif ans == "2":
        Edit(filename)
    elif ans == "3":
        Delete(filename)
    else:
            print("Thank you for using the software!")

def Add(filename):
    #decrypts the csv file so the user can delete an account
    bufferSize = 64 * 1024
    password = input("Enter the password for the file to decrypt it: \n")
    pyAesCrypt.decryptFile(filename+".aes",filename, password, bufferSize)
    os.remove(filename+".aes")
    #prompts user to enter the username and password they want to add to the csv file
    username = input("Enter username you want to add: \n")
    password = input("Enter password you want to add: \n")
    csvFile = open(filename, "a")
    #appends the username and password with a delimter to the end of the csv file
    csvFile.write(username+","+password)
    csvFile.close()
    #re-encrypts the csv file
    EncryptionFunction.Encrypt("details.csv")
    os.remove(filename)

    DoAgain()
    
def Edit(filename):
    #decrypts the csv file so the user can delete an account
    bufferSize = 64 * 1024
    password = input("Enter the password for the file to decrypt it: \n")
    pyAesCrypt.decryptFile(filename+".aes",filename, password, bufferSize)
    os.remove(filename+".aes")
    #prompts user to choose what they would like to edit
    passOrUser = input("Would you like to edit a username(1), password(2) or both(3)")
    #reads csv file data into a pandas data frame
    df = pd.read_csv(filename)
    print(df)

    if int(passOrUser) == 1:
        editUsername = input("Enter the username you want to edit: \n")
        newUsername = input("Enter the new username: \n")
        #stores the index of the current username
        index = df.loc[df['username'] == editUsername].index[0]
        #stores current password
        password = df.loc[index, 'password']
        #creates a new row with index, new username and current password
        newRow = df.loc[index]= [newUsername, password]
        #adds the row to the dataframe at a specific index
        df.append(newRow)
        #stores dataframe in the csv file
        df.to_csv(filename, index=False)

        #code is the same for each condition but structured slightly differently for a different purpose
    elif int(passOrUser) == 2:
        editPassword = input("Enter the password you want to edit: \n")
        newPassword = input("Enter the new password: \n")
        
        index = df.loc[df['password'] == editPassword].index[0]
        username = df.loc[index, 'username']
        newRow = df.loc[index] = [username, newPassword]

        df.append(newRow)

        df.to_csv(filename, index=False)

    elif int(passOrUser) == 3:
        editUsername = input("Enter the username you want to edit: \n")
        newUsername = input("Enter the new username: \n")
        
        newPassword = input("Enter the new password: \n")
        index = df.loc[df['username'] == editUsername].index[0]
        newRow = df.loc[index] = [newUsername, newPassword]

        df.append(newRow)

        df.to_csv(filename, index=False)
    
    #re-encrypts the csv file
    EncryptionFunction.Encrypt("details.csv")
    os.remove(filename)

    DoAgain()

def Delete(filename):
    #decrypts the csv file so the user can delete an account
    bufferSize = 64 * 1024
    password = input("Enter the password for the file to decrypt it: \n")
    pyAesCrypt.decryptFile(filename+".aes",filename, password, bufferSize)
    os.remove(filename+".aes")
    
    delUserName = input("Enter the username of the account you want to delete: \n")
    #reads the csv file into a pandas data frame
    df = pd.read_csv(filename)
    #checks whether the column "username" contains the username provided by the user
    #if it contains it, it removes that line then dumps the dataframe back into the csv file  
    df = df[~df["username"].str.contains(delUserName, na=False)].to_csv('details.csv', index = False)
    # calls encryption function to re-encrypt the csv file
    EncryptionFunction.Encrypt("details.csv")
    os.remove(filename)

    DoAgain()

    
