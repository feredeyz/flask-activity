from flask import Flask, send_file, request, render_template, session
from functions.login import login as check_login
from functions.register import register as check_register
from functions.get_activity import get_activity
from functions.get_secret_key import get_secret_key
from functions.write_messages import write_messages
from functions.get_messages import get_messages

app = Flask(__name__, template_folder='templates')
app.secret_key = get_secret_key()

@app.route('/')
def root():
    return send_file('static/main.html')

@app.route('/data/msg', methods=["POST"])
def messages():
    write_messages(session["username"], request.form["msg"])
    return main()

def main():
    return render_template('home.html', msgs=get_messages(), activities=get_activity())

@app.route('/data/reg', methods=["POST"])
def registrate():
    if check_register(request.form):
        session["username"] = request.form["username"]
        return main()
    else:
        return "net"

@app.route('/data/log', methods=["POST"])
def login():
    result = check_login(request.form)
    if result == "fail":
        return "nepravilno"
    else:
        session["username"] = request.form["username"]
        return main()

if __name__ == "__main__":
    app.run(debug=True)