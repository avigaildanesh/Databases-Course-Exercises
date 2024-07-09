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
    # The answer contains both the date and the total amount of new vaccinations as “daily_vaccinations”.
    cursor.execute("""
                SELECT date, SUM(new_vaccinations) AS daily_vaccinations
                FROM covid_vaccination
                WHERE continent = "Asia"
                GROUP BY date
                HAVING daily_vaccinations > 20000000;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))       
