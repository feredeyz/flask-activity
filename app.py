from flask import Flask, send_file, request, render_template
from functions.login import login as check_login
from functions.register import register as check_register
from functions.get_activity import get_activity


app = Flask(__name__, template_folder='templates')

@app.route('/')
def root():
    return send_file('static/main.html')

def main():
    return render_template('home.html', activities=get_activity())

@app.route('/data/reg', methods=["POST"])
def registrate():
    if check_register(request.form):
        return main()
    else:
        return "net"
    
@app.route('/data/log', methods=["POST"])
def login():
    result = check_login(request.form)
    if result == "fail":
        return "nepravilno"
    else:
        return main()