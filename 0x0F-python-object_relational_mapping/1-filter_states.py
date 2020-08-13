#!/usr/bin/python3

""" lists all states that start with N from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    dal = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    csr = dal.cursor()
    csr.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = csr.fetchall()

    for row in rows:
        print(row)
    csr.close()
    dal.close()
