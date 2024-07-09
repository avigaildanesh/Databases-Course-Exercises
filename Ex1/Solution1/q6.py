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
    # we removed the locations that start in A and not the continents that start with A
    cursor.execute("""
            SELECT continent
            FROM covid_deaths
            WHERE location NOT LIKE 'A%'
            GROUP BY continent
            HAVING SUM(new_cases) > (
                SELECT AVG(new_cases)
                FROM covid_deaths
                ); 
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))     