

from filmconnect import *

def delete():
    idfield =input("Enter the ID of the film to be deleted: ")

    try:
        cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idfield}")
        conn.commit()
        print(f"Film {idfield} has been deleted")

    except sql.OperationalError as e: 
        conn.rollback()
        print(f"records not found in database: {e}")
    
if __name__ == "__main__":
    delete()  