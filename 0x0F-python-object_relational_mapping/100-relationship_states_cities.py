#!/usr/bin/python3
"""
creates the State California with the City San Francisco from the database
"""

from relationship_state import Base, State
from relationship_city import City
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

    addState = State(name="California")
    addState.cities = [City(name="San Francisco")]
    session.add(addState)
    session.commit()
    session.close()
