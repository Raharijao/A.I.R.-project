from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
