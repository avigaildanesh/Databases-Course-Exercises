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
    # we did the sum of the 2 results, you can get the 2 results by adding row up to HAVING that is "GROUP BY location".
    cursor.execute("""
            SELECT SUM(new_cases)
            FROM covid_deaths AS a
            WHERE a.location IN (
                SELECT DISTINCT location
                FROM covid_deaths AS b, (
                   SELECT DISTINCT MAX(population) AS d, date
                   FROM covid_deaths 
                   GROUP BY date
                ) AS c
                WHERE b.date = c.date AND c.d = b.population
            ) 
            HAVING AVG(new_cases)>3;        
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))      