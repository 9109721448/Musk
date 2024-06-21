import sqlite3
import streamlit as st


#connection

conn = sqlite3.connect('Mydb.db')

# Create a cursor object
c=conn.cursor()


# Create a table

c.execute('steel')
c.execute('select * from cement')
data=c.fetchall()
