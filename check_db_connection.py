import pymysql.cursors


# DB API 2.0
connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
try:
    # Point to the data stored in the database
    cursor = connection.cursor()
    # Query the data from the DB and print row by row
    cursor.execute("select * from address_in_groups")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()