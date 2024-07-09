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
    # A query that returns the continents which average new cases is greater that
    # the average of new cases of locations where the average population is lower
    # than the global average population

    cursor.execute("""
            SELECT continent
            FROM covid_deaths
            GROUP BY continent
            HAVING AVG(new_cases)> (
                   SELECT AVG(b)
                   FROM (
                        SELECT AVG(new_cases) AS b
                        FROM covid_deaths
                        GROUP BY location
                        HAVING AVG(population)<(
                        SELECT AVG(population)
                        FROM covid_deaths
                        )
                   ) AS s
            );                                 
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))         