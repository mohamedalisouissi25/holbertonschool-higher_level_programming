#!/usr/bin/python3
"""
a script that lists all cities in the input state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    dal = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = dal.cursor()
    cursor.execute("SELECT cities.name\
                FROM cities JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name LIKE BINARY '{}'\
                ORDER BY 'cities.id'".format(sys.argv[4]))
    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))
    cursor.close()
    dal.close()
