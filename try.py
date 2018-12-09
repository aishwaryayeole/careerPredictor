from flask import Flask, render_template, request
import sqlite3 as sql
import numpy as np
from scipy.sparse import csr_matrix



app = Flask(__name__)


@app.route('/')
def home():
    return "<h1> Hello Home </h1>"


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute('INSERT INTO students (name,addr,city,pin)\
                VALUES(?, ?, ?, ?)',(nm,addr,city,pin) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html",msg = msg)
            con.close()


con = sql.connect("database.db")
cur = con.cursor()
c=cur.execute("select * from students")
l=c.fetchall()
print(l)
out = open('test.csv', 'w')
for row in l:
    for column in row:
        out.write('%s;' % column)
    out.write('\n')
out.close()
if __name__ == "__main__":
    app.run(debug=True)