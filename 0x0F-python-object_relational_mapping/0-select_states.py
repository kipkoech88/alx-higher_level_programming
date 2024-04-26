#!/usr/bin/python3
""" Module to ist all cities in a database
It uses MySQLdb to interact with MySQL server
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """ it connects the MySQL database using args provided
    as command line arguments, creates engine
    , create cursor where it excecutes SQL
    commands """
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    curr = db.cursor()
    curr.execute("SELECT * FROM states")
    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    db.close()
