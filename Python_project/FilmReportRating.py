from filmconnect import *

def readRating():

    agerating = input("Please select an Age Rating(G / PG / R ): ").upper()
    
    try:
        row = cursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{agerating}'").fetchall() #selects all the recors from the films table
        # obtain all the records and they are stored in the row variable
        for arecord in row:
            print(arecord)
    except sql.OperationalError as e:
        print(f"records not found: {e}")

if __name__ == "__main__":
    readRating()