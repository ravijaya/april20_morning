import sqlite3


conn = sqlite3.connect('apr20_1.sqlite')
cur = conn.cursor()

query = 'select sqlite_version()'
cur.execute(query)

print(cur.fetchone())

cur.close()
conn.close()

"""
ravi.goglobium@gmail.com

97909 16181 
"""