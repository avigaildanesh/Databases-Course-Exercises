import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="covid_db",
        port='3307',
    )
    cursor = mydb.cursor()

    # Retrieve distinct values from the "covid_db" column in the "location" table
    cursor.execute("""
                  SELECT DISTINCT location 
                   FROM covid_deaths 
    """)

#Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for result in results:
        print(result[0])

    # Close the cursor and database connection
    cursor.close()
    mydb.close()