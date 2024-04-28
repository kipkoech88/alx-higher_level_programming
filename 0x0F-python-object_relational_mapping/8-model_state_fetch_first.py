#!/usr/bin/python3
""" Returns the first state in the
database """
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.id == 1)
    row = query.first()
    if row is None:
        print('Nothing')
    else:
        print(row.id, row.name, sep=': ')
