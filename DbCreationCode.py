import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute('CREATE TABLE StudentPerformanceDB (name TEXT not null,gender INTEGER not null,age INTEGER not null,Pstatus INTEGER not null,studytime INTEGER not null,schoolsup INTEGER not null,famsup INTEGER not null,failures INTEGER not null,activities INTEGER not null,nursery INTEGER not null,higher INTEGER not null,internet INTEGER not null,absences INTEGER not null,G1 INTEGER not null,G2 INTEGER not null,G3 INTEGER DEFAULT 99)')
print("Table created successfully");
conn.close()