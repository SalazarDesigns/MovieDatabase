from filmconnect import *

def insertfilm():
    #Create an empty list
    films=[]

    title = input("Enter film Title: ")
    release = input("Enter film release Year: ")
    agerating = input("Enter film age Rating: ")
    duration = input("Enter film Duration: ")
    genre = input("Enter film genre: ")

    #append data into the list "songs"
    films.append(title)
    films.append(release)
    films.append(agerating)
    films.append(duration)
    films.append(genre)

    # songs = songs + [title, artist, genre] - both are valid ways to append data items

    try:
        cursor.execute("INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)", films)
        conn.commit()  
        print(f"{title} has been added to the database")
    
    except sql.OperationalError as e :
        conn.rollback()
        print(f"Record not added {e}")

if __name__ == "__main__":
    insertfilm()