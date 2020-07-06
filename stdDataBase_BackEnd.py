import sqlite3


def studentData():
    con = sqlite3.connect('student.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, stdId text, firstName text, surname text, \
     dob text, age text, gender text, address text, mobile text)")
    con.commit()
    con.close()


def addStdRec(stdId, firstName, surname, dob, age, gender, address, mobile):
    con = sqlite3.connect('student.db')
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?)", (stdId, firstName, surname, dob, age, gender,
                                                                       address, mobile))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect('student.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows


def deleteRec(id):
    con = sqlite3.connect('student.db')
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()


def searchData(stdId="", firstName="", surname="", dob="", age="", gender="", address="", mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student where stdId=? OR firstName=? OR surname=? OR dob=? OR age=? OR gender=? OR \
     address=? OR mobile=? ", (stdId, firstName, surname, dob, age, gender, address, mobile))
    rows = cur.fetchall()
    con.close()
    return rows


def dataUpdate(id, stdId="", firstName="", surname="", dob="", age="", gender="", address="", mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET stdId=?, firstName=,?, surname=?, dob=?, age=?, gender=?, \
         address=?, mobile=?, WHERE id=? ", (stdId, firstName, surname, dob, age, gender, address, mobile, id))
    con.commit()
    con.close()


studentData()
