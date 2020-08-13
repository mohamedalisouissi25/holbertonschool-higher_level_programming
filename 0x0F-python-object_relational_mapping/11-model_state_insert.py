#!/usr/bin/python3
"""
a script that adds the State object Louisiana
to the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sess = Session()
    new_state = State(name='Louisiana')
    sess.add(new_state)
    st = sess.query(State).filter_by(name='Louisiana').first()
    print(str(st.id))
    sess.commit()
    sess.close()
