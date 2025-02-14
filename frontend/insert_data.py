import mysql.connector 
from datetime import datetime 

def insert_data(product_name, price, quantity):
    try:
        mydb = mysql.connector.connect(
            host='genesis-stage-rds.cddjztebudhs.eu-central-1.rds.amazonaws.com',
            #user='',
            #password='',
            database='genesis-stage-rds'
        )

        cursor = mydb.cursor()

        insert_query = "INSERT INTO ProductInventory (product_name, price, quantity, created_at) VALUES (%s, %s, %s, %s)"
        values = (product_name, price, quantity, datetime.now())

        cursor.execute(insert_query, values)
        mydb.commit()

        print("Data inserted successfully!")

    except mysql.connector.Error as error:
        print("Failed to insert data:", error)

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'mydb' in locals() and mydb is not None:
            mydb.close()

if __name__ == "__main__":
    insert_data("ProductA", 50, 100)