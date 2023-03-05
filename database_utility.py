#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__ = ['ReviewDatabase']
import sqlite3

class ReviewDatabase:
    def __init__(self, name):
        self.name = name + ".db"

    def create_table(self):
        # Creating new table for logging reviews in database
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        c.execute('''CREATE TABLE if NOT EXISTS product(title TEXT, comments TEXT, url TEXT)''')

    def add_data(self, review_content):
        # For adding new entry in the reviews database
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        c.execute('''INSERT INTO product VALUES(?,?,?)''', (review_content["title"], review_content["comments"], review_content["url"]))
        conn.commit()
        conn.close()

    def select_data(self, key):
        #For displaying reviews of a product
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        c.execute('''SELECT * FROM product''')
        results = c.fetchall()
        print(results)
        conn.close()

    def get_product_titles(self):
        # For getting list of all available titles logged in the database
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        c.execute('''SELECT title FROM product''')
        results = c.fetchall()
        conn.close()
        result = (str(str(f).split("'")[1]) for f in results)
        return result


    def get_product_review(self, searched_title):
        # Get the reivews of a particular title
        conn = sqlite3.connect(self.name)
        c = conn.cursor()
        c.execute('''SELECT * FROM product WHERE title=:searched_title''', {"searched_title": searched_title})
        results = c.fetchall()
        conn.close()
        return results[0]