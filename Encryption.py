import pyAesCrypt


def Encrypt():
    bufferSize = 64 * 1024
    password = input("Enter the password to encrypt the file: \n")
    filename = input("Enter the name of the csv file you want to encrypt: \n")
    pyAesCrypt.encryptFile(filename, filename+".aes", password, bufferSize)

def Decrypt(filename):
    bufferSize = 64 * 1024
    password = input("Enter the password to decrypt the file: \n")
    pyAesCrypt.decryptFile(filename+".aes", filename, password, bufferSize)