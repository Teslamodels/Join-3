import psycopg2
from psycopg2 import Error

def insert_category(Title):
    
    try:

        connection = psycopg2.connect(user = 'YOU NEED TO WRITE IT BY YOURSELF', password = 'YOU NEED TO WRITE IT BY YOURSELF', host = 'YOU NEED TO WRITE IT BY YOURSELF', port = 5432, database = 'YOU NEED TO WRITE IT BY YOURSELF')

        cursor = connection.cursor()

        cursor.execute("""INSERT INTO Category(Title)
                       VALUES(%s)""", (Title, ))
        
        connection.commit()

        print("Success")

    except(Exception, Error) as error:

        print("Error", error)

    finally:

        if connection:

            cursor.close()

            connection.close()

            print("Closed")