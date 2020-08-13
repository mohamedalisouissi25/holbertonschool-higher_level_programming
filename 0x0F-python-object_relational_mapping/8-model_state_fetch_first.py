<#!/usr/bin/python3
"""a script that prints the first State object from the database hbtn_0e_6_usa """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sess = Session()
    dal = sess.query(State).order_by(State.id).first()
    if dal is None:
        print("Nothing")
    else:
        print("{}: {}".format(dal.id, dal.name))
