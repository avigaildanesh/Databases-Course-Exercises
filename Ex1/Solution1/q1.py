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
    # We assume that the question is referring to the clomun "new_cases" and not the sum of total_cases because total cases is. 
    cursor.execute("""
                SELECT 
                    (SELECT SUM(new_cases) FROM covid_deaths WHERE MONTH(date) = 2) -
                    (SELECT SUM(new_cases) FROM covid_deaths WHERE MONTH(date) = 3);    
                FROM 
                    covid_deaths;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))