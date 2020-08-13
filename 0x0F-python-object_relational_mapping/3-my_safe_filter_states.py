#!/usr/bin/python3
"""
a script that displays all values in the states table1 of
hbtn_0e_0_usa where name matches the argument avoiding injection
"""

import MySQLdb
import sys

if __name__ == "__main__":
    dal = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = dal.cursor()
    cursor.execute("SELECT * FROM states\
                   WHERE name LIKE %s ORDER BY id ASC", (sys.argv[4],))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    dal.close()
