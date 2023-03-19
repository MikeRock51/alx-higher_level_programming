#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City
from model_state import Base, State


if __name__ == "__main__":
    userName = argv[1]
    passWord = argv[2]
    dbName = argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{userName}:{passWord}@localhost/{dbName}",
        pool_pre_ping=True)

    session = Session(engine)
    places = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()

    for state, city in places:
        print(f"{state.name}: ({city.id}) {city.name})")

    session.close()
