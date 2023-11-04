import psycopg2
from psycopg2 import Error

try:

    connection = psycopg2.connect(user = 'YOU NEED TO WRITE IT BY YOURSELF', password = 'YOU NEED TO WRITE IT BY YOURSELF', host = 'YOU NEED TO WRITE IT BY YOURSELF', port = 5432, database = 'YOU NEED TO WRITE IT BY YOURSELF')

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE Product(
                   ID SERIAL PRIMARY KEY,
                   Title VARCHAR(100),
                   Time_charging VARCHAR(100) NOT NULL,
                   Category_id INTEGER NOT NULL
                   );""")
    
    connection.commit()

    print("Success")

except(Exception, Error) as error:

    print("Error", error)

finally:

    if connection:

        cursor.close()

        connection.close()

        print("Closed")