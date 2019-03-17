import pyAesCrypt


def Encrypt(filename):
    bufferSize = 64 * 1024
    password = input("Enter the password to encrypt the file: \n")
    pyAesCrypt.encryptFile(filename, filename+".aes", password, bufferSize)
    
def Decrypt(filename):
    bufferSize = 64 * 1024
    password = input("Enter the password to decrypt the file: \n")
    pyAesCrypt.decryptFile(filename, "details.csv", password, bufferSize)
    