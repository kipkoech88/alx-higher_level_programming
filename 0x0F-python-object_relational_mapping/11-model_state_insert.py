#!/usr/bin/python3
""" Adds an object to the
database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = State(name='Louisiana')
    session.add(row)
    query = session.query(State).filter_by(name='Louisiana')
    res = query.first()
    print(res.id)
    session.commit()
    session.close()
