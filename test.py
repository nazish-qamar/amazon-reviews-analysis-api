import sqlite3

conn = sqlite3.connect("product_reviews.db")
cursor = conn.execute("SELECT * from product")

# delete an entry
#conn.execute("DELETE from product where comments='[]'")

for row in cursor:
    print(row)
conn.commit()
conn.close()