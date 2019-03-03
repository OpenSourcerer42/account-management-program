import csv


def welcome():
    print("welcome to the software")

def checkdetails():
    username = raw_input("please enter your username: \n")
    password = raw_input("please enter your password: \n")

    #reads csv file 
    with open("details.csv", "r") as details_file:
        continueTo = False
        reader = csv.reader(details_file, delimiter=",")
        #reads each line which has a username and password and compares to use input
        for line in reader:
            if username == line[0] and password == line[1]:
                continueTo = True

        if continueTo == False:
            tryAgain = input("incorrect details, try again yes(1) or no(2)")

            if tryAgain == 1:
                checkdetails()

        elif continueTo == True:
            print("correct details")
            welcome()



checkdetails()
