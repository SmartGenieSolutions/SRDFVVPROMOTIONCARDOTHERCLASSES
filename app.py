from flask import Flask, render_template, request, flash
import sqlite3

app = Flask(__name__, static_url_path='/static')
app.secret_key = "Smart"


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def home_page():
    flash("")
    return render_template('index.html')


@app.route('/marks_page', methods=["POST"])
def marks_page():
    if request.method == 'POST':
        user_admn_number = request.form['admission_number_input']
        print(user_admn_number)
        result_admn = search(request.form['admission_number_input'])
        # print(result_admn[3])

    if result_admn is None:
        flash("Please contact school Office")
        return render_template('index.html')
    else:
        return render_template('marks.html', result=result_admn)


def search(admn_number):
    conn = sqlite3.connect("srdfvvpromotion.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * from student_data WHERE admn_number=? ", (admn_number,))
    rows = cursor.fetchone()
    conn.close()
    return rows


if __name__ == '__main__':
    app.debug = True
    app.run()
