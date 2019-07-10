from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "route"

@app.route('/user')
def cliant():
    return render_template('user.html')

@app.route('/make-task')
def make():
    info = {
        "target": "100000",
        "taskID": "1"
    }
    return jsonify(info)

@app.route('/complete-task', methods=['GET', 'POST'])
def complete():
    print(request.form['taskID'])
    print(request.form['result'])
    return 'ok from server'

if __name__ == "__main__":
    app.run(threaded=True, debug=True)
