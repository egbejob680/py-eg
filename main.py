def Prompt():
    display = { "0","1","2","3","4"}
    print("====================")
    print(" 0 is to quit\n 1 is to add mail\n 2 is to show mail \n 3 is to update mail\n 4 is to delete ")
    print("====================")
    output = input("enter a value from 0 - 4: ")
    if output == "0": 
        quit()
    elif output == "1":
        addMail()
    elif output == "2":
        showMail()
    elif output == "3":
        updateMail()
    elif output == "4":
        deleteMail()
    else:
        print("please enter correct value")

def addMail(name,email):
    "modify"
def showMail():
    "modify"
def updateMail():
    "modify"

def deleteMail():
    "modify"
def quit():
    "modify"
Prompt()