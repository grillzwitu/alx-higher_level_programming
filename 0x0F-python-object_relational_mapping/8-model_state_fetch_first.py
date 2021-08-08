#!/usr/bin/python3
"""
lists the first State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    firstState = session.query(State).order_by(State.id).first()
    if firstState is not None:
        print("{}: {}".format(firstState.id, firstState.name))
    else:
        print("Nothing")
    session.close()
