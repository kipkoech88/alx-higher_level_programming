#!/usr/bin/python3
import sys
import MySQLdb
""" This module displays values in
the `states` table of hbtn_0e_0_usa
where name matches the argument
"""

if __name__ == "__main__":
    """ Takes 4 command line arguments ie username
    password, db name and name to be searched for
    """
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name 
                LIKE BINARY '{}' ORDER BY states.id ASC""".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
