import psycopg2

try:
    connection = psycopg2.connect(user='postgres',
                                  password='postgres',
                                  host='localhost',
                                  port='5432',
                                  database='tcrawler')
    cursor = connection.cursor()
    cursor.execute("SELECT id,bio,rating from crawler_data where bio like '%велоси%' limit 100")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
except (Exception,psycopg2.Error) as error:
    print("Error while connections to postgresql",error)
finally:
    if(connection):
        connection.close()

