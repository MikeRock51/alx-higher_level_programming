#!/usr/bin/python3
"""
A script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    userName = argv[1]
    passWord = argv[2]
    dbName = argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{userName}:{passWord}@localhost:3306/{dbName}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    city2add = City(name='California')
    state2add = State(name='San Francisco')
    state2add.cities.append(city2add)
    session.add(state2add)

    session.commit()
    session.close()
