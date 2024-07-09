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
    # we limit 1000 like the question
    cursor.execute("""
                SELECT  a.date,a.new_cases,a.location, b.location
                FROM   (
                        SELECT *
                        FROM   covid_deaths
                        WHERE  new_cases > 1000
                        LIMIT  1000) AS a,
                        (SELECT *
                        FROM   covid_deaths
                        WHERE  new_cases > 1000
                        LIMIT  1000) AS b
                WHERE  a.date = b.date AND a.location < b.location AND a.new_cases = b.new_cases;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))    