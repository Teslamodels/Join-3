import psycopg2
from psycopg2 import Error


def select_data():

    try:

        connection = psycopg2.connect(user = 'YOU NEED TO WRITE IT BY YOURSELF', password = 'YOU NEED TO WRITE IT BY YOURSELF', host = 'YOU NEED TO WRITE IT BY YOURSELF', port = 5432, database = 'YOU NEED TO WRITE IT BY YOURSELF')

        cursor = connection.cursor()

        cursor.execute("""SELECT Product.id, Product.Title, Product.Category_id, Category.id, Category.Title FROM Product INNER JOIN Category ON Product.Category_id = Category.id;""")
        
        info = cursor.fetchall()

        return info

    except(Exception, Error) as error:

        print("Error", error)

    finally:

        if connection:

            cursor.close()

            connection.close()
            
            print("Successfully closed!")

print(select_data())