import psycopg2
from psycopg2 import Error


def insert_product(Title, Time_charging, Category_id):
    try:

        connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'Join_3')

        cursor = connection.cursor()

        cursor.execute("""INSERT INTO Product(Title, Time_charging, Category_id) 
                       VALUES(%s, %s, %s);""", (Title, Time_charging, Category_id))
        
        connection.commit()

        print("Success")

    except(Exception, Error) as error:

        print("Error", error)

    finally:

        if connection:

            cursor.close()

            connection.close()

            print("Closed")