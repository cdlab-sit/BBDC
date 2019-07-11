from flask import Flask, render_template, request, jsonify
import csv

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
        "taskID": "1",
        "return": "-1"          # 空の場合 -1　 解が存在しない場合 0
    }

    #csvモジュールは独自の改行処理を行うため、newline='' を指定
    with open('taskID_list.csv','a',newline='') as csvfile:
        writer=csv.writer(csvfile, lineterminator='\n')
        print(info["target"],file=csvfile,end=',')
        print(info["taskID"],file=csvfile,end=',')
        print(info["return"],file=csvfile)
    return jsonify(info)

#from user.js
@app.route('/complete-task', methods=['GET', 'POST'])
def complete():
    print(request.form['taskID'])
    print(request.form['result'])
    return 'ok from server'

if __name__ == "__main__":
    app.run(threaded=True, debug=True, host='0.0.0.0', port=5000)
