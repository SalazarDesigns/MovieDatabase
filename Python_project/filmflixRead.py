from filmconnect import *

def read():
    try:
        cursor.execute("SELECT * FROM tblFilms") #selects all the recors from the films table
        row = cursor.fetchall()# obtain all the records and they are stored in the row variable
        for arecord in row:
            print(arecord)
    except sql.OperationalError as e:
        print(f"records not found: {e}")

if __name__ == "__main__":
    read()
        