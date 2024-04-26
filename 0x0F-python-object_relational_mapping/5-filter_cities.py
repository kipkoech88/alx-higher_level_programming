#!/usr/bin/python3
""" This module is for listing
all cities in the database of
a state provided by user"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
                INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4], ))
    res = cur.fetchall()
    li = list(i[0] for i in res)
    print(*li, sep=', ')
    cur.close()
    db.close()
