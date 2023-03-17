#!/usr/bin/python3

import MySQLdb
from sys import argv

"""A script that lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    """Connects and fetches data from the database hbtn_0e_0_usa"""

    userName = argv[1]
    passWord = argv[2]
    dbName = argv[3]

    db_conn = MySQLdb.connect(host='localhost', port=3306,
                         user=userName, passwd=passWord, db=dbName)
    db_cursor = db_conn.cursor()
    db_cursor.execute("SELECT * from states")
    states = db_cursor.fetchall()

    for state in states:
        print(state)

    db_cursor.close()
    db_conn.close()
