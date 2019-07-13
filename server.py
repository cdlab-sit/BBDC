from flask import Flask, render_template, request, jsonify
import csv, random, datetime

app = Flask(__name__)

# python で static変数を使いたかった
# 代用案
class static:
    taskID=1
    task_num=0

filename = ''

@app.route('/host')
def host():
    dt_now = datetime.datetime.now()
    filename = dt_now.strftime('%Y_%m_%d_%H:%M:%S')
    with open(filename,'w') as csv:
        print('just made file')
    return 'go'

@app.route('/host-waiting')
def index():
    return "待機"

@app.route('/user-waiting')
def client_waiting():
    return render_template('user-waiting.html')

@app.route('/user')
def cliant():
    return render_template('user.html')

@app.route('/make-task')
def make():
    # with open(filename,'r') as csvfile:
    #     reader = csv.DictReader(csvfile,fieldnames=['taskID,target,result'])
    
    # 乱数生成
    target = random.randint(50000,100000)
    target = 50000 #test
    info = {
        "target": target,
        "taskID": static.taskID,
    }
    return jsonify(info)

# /user で user.js により呼び出される 
@app.route('/complete-task', methods=['POST'])
def complete():
    # with open(filename,'w',newline='') as csvfile:
    print(request.form['taskID'])
    # print(request.form['target'])
    print(request.form['result'])
    #     print(request.form['taskID'],file=csvfile,newline=',')
    #     print(request.form['target'],file=csvfile,newline=',')
    #     print(request.form['result'],file=csvfile)
    return 'ok from server'

if __name__ == "__main__":
    app.run(threaded=True, debug=True, host='0.0.0.0', port=5000)