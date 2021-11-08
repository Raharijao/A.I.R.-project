from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def render_index():
    return render_template('index.html')

@app.route("/main")
def view_main_map():
    return render_template("index.html", title="Main map")

@app.route("/plain")
def view_plain_map():
    return render_template("index.html", title="Plain map")


@app.route("/m1")
def m1():
    return render_template("index.html", title="m1")

@app.route("/m2")
def m2():
    return render_template("index.html", title="m2")


@app.route("/m3")
def m3():
    return render_template("index.html", title="m3")

@app.route("/m4")
def m4():
    return render_template("index.html", title="m4")


@app.route("/m5")
def m5():
    return render_template("index.html", title="m5")

@app.route("/m6")
def m6():
    return render_template("index.html", title="m6")

@app.route("/m7")
def m7():
    return render_template("index.html", title="m7")

@app.route("/m8")
def m8():
    return render_template("index.html", title="m8")

@app.route("/m9")
def m9():
    return render_template("index.html", title="m9")


@app.route("/m10")
def m10():
    return render_template("index.html", title="m10")

@app.route("/m11")
def m11():
    return render_template("index.html", title="m11")

@app.route("/m12")
def m12():
    return render_template("index.html", title="m12")

@app.route("/h1")
def h1():
    return render_template("index.html", title="h1")

@app.route("/h2")
def h2():
    return render_template("index.html", title="h2")

@app.route("/h3")
def h3():
    return render_template("index.html", title="h3")

@app.route("/h4")
def h4():
    return render_template("index.html", title="h4")


@app.route("/h5")
def h5():
    return render_template("index.html", title="h5")

@app.route("/h6")
def h6():
    return render_template("index.html", title="h6")

@app.route('/form')
def form():
   return render_template('form.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         fn = request.form['fn']
         ln = request.form['ln']
         email = request.form['email']
         city = request.form['city']

         with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("INSERT INTO recipients (first_name,last_name,email,city) VALUES (?,?,?,?)",(fn,ln,email,city) )

            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from recipients")

   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
    app.run(debug=True)
