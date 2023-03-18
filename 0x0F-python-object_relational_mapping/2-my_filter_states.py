#!/usr/bin/python3

"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.

    Your script should take 4 arguments: mysql username, mysql password,
    database name and state name searched (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running
    on localhost at port 3306
    You must use format to create the SQL query with the user input
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Allows the module to be imported without running"""

    userName = argv[1]
    passWord = argv[2]
    dbName = argv[3]
    reqState = argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=userName, passwd=passWord, database=dbName)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name = %s", (reqState,))

    result = cur.fetchall()

    for state in result:
        print(state)

    cur.close()
    db.close()
