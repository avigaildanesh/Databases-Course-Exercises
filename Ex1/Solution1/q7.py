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
    # we returned the location and monthly avg,min,max of new cases
    cursor.execute(""" 
            SELECT location, AVG(monthly_new_cases), MAX(monthly_new_cases),MIN(monthly_new_cases)
            FROM(
                SELECT location,SUM(new_cases) as monthly_new_cases, MONTH(date)
                FROM covid_deaths 
                GROUP BY location,MONTH(date)
            ) AS s 
            GROUP BY location      
                      
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))     