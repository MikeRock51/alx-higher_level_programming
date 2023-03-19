#!/usr/bin/python3
"""
A script that changes the name of a State object
from the database hbtn_0e_6_usa
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
        f"mysql+mysqldb://{userName}:{passWord}@localhost/{dbName}",
        pool_pre_ping=True)

    session = Session(engine)
    state2Update = session.query(State).filter_by(id=2)

    for state in state2Update:
        state.name = "New Mexico"

    session.commit()
    session.close()
