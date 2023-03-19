#!/usr/bin/python3
"""
A script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    userName = argv[1]
    passWord = argv[2]
    dbName = argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{userName}:{passWord}@localhost:3306/{dbName}",
        pool_pre_ping=True)

    session = Session(engine)

    places = session.query(State).order_by(State.id).all()

    for place in places:
        print(f"{place.id}: {place.name}")
        for city in place.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()
