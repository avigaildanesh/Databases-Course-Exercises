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
                   SELECT date, location, new_cases 
                   FROM covid_deaths 
                   WHERE weekly_hosp_admissions = new_cases 
                   AND new_cases != 0 
                   ORDER BY new_cases DESC;
    """)

#Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for result in results:
        print(result[0], result[1],result[2])

    # Close the cursor and database connection
    cursor.close()
    mydb.close()