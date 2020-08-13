#!/usr/bin/python3

""" a script that lists all states from the database hbtn_0e_0_usa with
a given name """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    dal = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    dal.close()
