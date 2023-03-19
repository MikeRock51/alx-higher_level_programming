#!/usr/bin/python3


"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    userName = argv[1]
    passWord = argv[2]
    dbName = argv[3]
    reqState = (argv[4],)

    db = MySQLdb.connect(user=userName, passwd=passWord, database=dbName)
    cur = db.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states ON states.id\
        = cities.state_id WHERE states.name = %s"
    params = reqState
    cur.execute(query, params)
    result = cur.fetchall()

    print(", ".join(city[0] for city in result))

    cur.close()
    db.close()
