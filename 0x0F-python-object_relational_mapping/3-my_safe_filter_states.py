#!/usr/bin/python3
""" Safe filter values from
database using users input and
prevent sql injection
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    inp = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (inp,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
