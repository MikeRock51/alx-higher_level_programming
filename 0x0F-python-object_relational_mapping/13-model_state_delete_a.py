#!/usr/bin/python3
"""A script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base


if __name__ == "__main__":
    userName = argv[1]
    passWord = argv[2]
    dbName = argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{userName}:{passWord}@localhost/{dbName}",
        pool_pre_ping=True)

    session = Session(engine)
    states2Delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in states2Delete:
        session.delete(state)

    session.commit()
    session.close()
