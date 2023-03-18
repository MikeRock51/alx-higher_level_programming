#!/usr/bin/python3


"""
A script that lists all cities from the database hbtn_0e_4_usa

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    userName = argv[1]
    passWord = argv[2]
    dbName = argv[3]

    db = MySQLdb.connect(user=userName, passwd=passWord, database=dbName)
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states ON state_id=states.id ORDER BY cities.id ASC")
    result = cur.fetchall()

    for city in result:
        print(city)

    cur.close()
    db.close()
