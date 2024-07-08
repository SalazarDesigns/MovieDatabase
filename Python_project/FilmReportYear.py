from filmconnect import *

def readYears():

    year = input("Please select a Year (1979 / 2014 / 2015 / 2016 / 2021): ")
    
    try:
        row = cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = '{year}'").fetchall()# obtain all the records and they are stored in the row variable
        for arecord in row:
            print(arecord)
    except sql.OperationalError as e:
        print(f"records not found: {e}")

if __name__ == "__main__":
    readYears()