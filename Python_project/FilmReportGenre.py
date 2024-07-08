from filmconnect import *

def readGenre():

    genre = input("Please select a genre(Action / Animation / Comedy / Crime / Fantasy / Fighting): ").title()
    
    
    try:
        row = cursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{genre}'").fetchall() # obtain all the records and they are stored in the row variable
        for arecord in row:
            print(arecord)
    except sql.OperationalError as e:
        print(f"records not found: {e}")

if __name__ == "__main__":
    readGenre()

    #('%' +genre_str+ '%',)