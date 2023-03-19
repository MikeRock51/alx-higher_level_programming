#!/usr/bin/python3
"""
A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    userName = argv[1]
    passWord = argv[2]
    dbName = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{userName}:{passWord}@localhost/{dbName}',
        pool_pre_ping=True)

    session = Session(engine)

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # new_state = session.query(State).filter(State.name == "Louisiana").all()

    # for state in new_state:
    print(new_state.id)

    session.close()
