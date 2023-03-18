#!/usr/bin/python3
from sys import argv
import MySQLdb

"""
Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:
    Your script should take 3 arguments: mysql username,
    mysql password and database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server
    running on localhost at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported
"""

if __name__ == '__main__':
    """Allows the module to be imported without running"""

    userName = argv[1]
    passWord = argv[2]
    dbName = argv[3]

    db_conn = MySQLdb.connect(host='localhost', port=3306,
                              user=userName, passwd=passWord, db=dbName)

    db_cursor = db_conn.cursor()
    db_cursor.execute(
        "SELECT * from states WHERE SUBSTR(states.name,\
              1, 1) = 'N'")
    states = db_cursor.fetchall()

    for state in states:
        print(state)

    db_cursor.close()
    db_conn.close()
