from filmflixCreate import *
from filmflixDelete import *
from filmflixRead import *
from filmflixUpdate import *
from FilmReportGenre import *
from FilmReportRating import *
from FilmReportYear import *

#create a function to display the program option

def menuOptions():
    options = 0
    while options not in ["1","2","3","4","5","6"]:
        with open("Python_project/filmflixMenu.txt","r") as menu:
            choices = menu.readlines()
        for line in choices:
            print(line, end="")
        options = input("Enter a menu option: ")
        if options not in ["1","2","3","4","5","6"]:
            print(f"Sorry that choice does not exist!")
    return options        

# print(menuOptions())

def reportOptions():
    options = 0
    while options not in ["1","2","3","4","5",]:
        with open("Python_project/filmflixOptions.txt","r") as menu:
            choices = menu.readlines()
        for line in choices:
            print(line, end="")
       
        options = input("\n Enter a Report option: ")
        if options not in ["1","2","3","4","5"]:
            print(f"Sorry that choice does not exist!")
    return options    


def mainMenu():
    main = True

    while main:
        mainMenu = menuOptions()
        if mainMenu == "1":
            read()
        elif mainMenu == "2":
            insertfilm()    
        elif mainMenu == "3":
            update()
        elif mainMenu == "4":
            delete()
        elif mainMenu == "5":
            # print("reports not available") #-  create a reports menu
            report = True
            while report == True: #--------------------------- create some code to pull up a table on report issues
                print(reportOptions())
                reportMenu = reportOptions()
                if reportMenu == "1":
                    read()
                elif reportMenu == "2":
                    readGenre()
                elif reportMenu == "3":
                    readYears()
                elif reportMenu == "4":
                    readRating()      
                else:
                    report = False
            input("Press enter to exit the main menu")
            return report
        else:
            main = False    
    input("Press enter to exit the main menu")
    return main 

if __name__ == "__main__":
    mainMenu()       