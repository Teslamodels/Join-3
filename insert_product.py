import psycopg2
from psycopg2 import Error


def insert_product(Title, Time_charging, Category_id):
    try:

        connection = psycopg2.connect(user = 'YOU NEED TO WRITE IT BY YOURSELF', password = 'YOU NEED TO WRITE IT BY YOURSELF', host = 'YOU NEED TO WRITE IT BY YOURSELF', port = 5432, database = 'YOU NEED TO WRITE IT BY YOURSELF')

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