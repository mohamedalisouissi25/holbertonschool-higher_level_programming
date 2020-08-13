#!/usr/bin/python3
"""
a script prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sess = Session()
    for sta, cty in sess.query(State, City).\
            filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(sta.name, cty.id, cty.name))
