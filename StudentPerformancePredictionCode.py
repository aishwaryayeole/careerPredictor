from flask import Flask, render_template, request
import sqlite3 as sql
from StudentPerRF import dynamic_prediction, main


app = Flask(__name__)
global con
@app.route('/')
def home():
    return render_template('StudentPerformanceHome.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            print("try")

            name = request.form['name']
            gender = request.form['gender']
            age = request.form['age']
            Pstatus = request.form['Pstatus']
            studytime = request.form['studytime']
            schoolsup = request.form['schoolsup']
            famsup = request.form['famsup']
            failures = request.form['failures']
            activities = request.form['activities']
            nursery = request.form['nursery']
            higher = request.form['higher']
            internet = request.form['internet']
            absences = request.form['absences']
            gradeOne = request.form['gone']

            g1=int(gradeOne)
            if g1 >=0 and g1 <10:
                g1=0
            else:
                g1=1

            gradeTwo = request.form['gtwo']
            g2=int(gradeTwo)
            if g2 >=0 and g2 <10:
                g2=0
            else:
                g2=1

            with sql.connect("database.db") as con:
                print("name con ", con)

                cur = con.cursor()

                cur.execute('INSERT INTO StudentPerformanceDB (name,gender,age,Pstatus,studytime,schoolsup,famsup,failures,activities,nursery,higher,internet,absences,G1,G2)\
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(name,gender,age,Pstatus,studytime,schoolsup,famsup,failures,activities,nursery,higher,internet,absences,g1,g2))

                con.commit()
                con = sql.connect("database.db")
                cur = con.cursor()
                c = cur.execute(
                    "select Pstatus,studytime,schoolsup,famsup,failures,activities,nursery,higher,internet,absences,G1,G2 from StudentPerformanceDB")
                l = c.fetchall()
                print(l)
                lastEntry=l[len(l)-1];
                print("length ",lastEntry)
                Opmessage=dynamic_prediction(lastEntry,name)

                return render_template("StudentPerformanceHome.html", message=str(Opmessage))
        except:
            con.rollback()
            return "<h3>error in insert operation</h3>"
        finally:
            con.close()
@app.route('/trainsystemPage', methods=['POST', 'GET'])
def trainSystemPage():
    return render_template("TrainSystem.html");

@app.route('/trainsystem')
def trainSystem():
    main()
    Opmessage="System trained successfully!"
    return render_template("TrainSystem.html", message=Opmessage)

if __name__ == "__main__":
    app.run(debug=True)