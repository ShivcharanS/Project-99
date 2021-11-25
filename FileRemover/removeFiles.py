import os 
import shutil
print("Welcome to file remover, Enter your file details asked and make sure your file days is 30 or more than that")

path = input("Enter Your Path :- ")
s = os.path.exists(path)

if (s == True):
    os.walk(path)
    days = int(input("Enter Your Days :- "))

    if( days >= 30):
        os.remove(path)
        print("Your File Has Been Deleted!!")

    if(days < 30):
        print("Sorry!! Your File Or Folder Is No Older Than 30 Days")

if (s == False):
    print("Sorry!! Your Path Doesnt Exists")


