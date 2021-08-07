#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa where
name matches the argument and is safe from MySQL injections
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
