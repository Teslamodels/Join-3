import psycopg2
from psycopg2 import Error

def insert_category(Title):
    
    try:

        connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'Join_3')

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