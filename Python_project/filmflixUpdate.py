from filmconnect import *

def update():
    idfield =input("Enter the ID of the record to be updated: ")

    fieldName =input("Enter the field to be updated(Title, YearReleased, Rating, Duration, Genre): ").title() # makes all the text capital case
    print (fieldName)
    newvalue = input(f"enter the value for {fieldName}: ") #python string output

    newvalue = "'"+newvalue+"'"

    try:
        cursor.execute(f"UPDATE tblFilms SET {fieldName} = {newvalue} WHERE filmID = {idfield}")
        conn.commit()
        print(f"Record {idfield} has been updated")

    except sql.OperationalError as e: 
        conn.rollback()
        print(f"records not updated: {e}")
    
if __name__ == "__main__":
    update()    