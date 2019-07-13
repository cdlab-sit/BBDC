from flask import Flask, render_template, request, jsonify
import csv, random, datetime

app = Flask(__name__)

dt_now = datetime.datetime.now()
filename = dt_now.strftime('%Y_%m_%d_%H:%M:%S')
with open(filename,'w') as csv:
    print('just made file')

# python で static変数を使いたかった
# 代用案
class static:
    taskID=0
    task_num=0

@app.route('/')
def index():
    return "待機"

@app.route('/user')
def cliant():
    return render_template('user.html')

@app.route('/make-task')
def make():
    with open(filename,'r') as csvfile:
        reader = csv.DictReader(csvfile,fieldnames=['taskID,target,result'])
    
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
    with open(filename,'a',newline='') as csvfile:
        print(request.form['taskID'],file=csvfile,newline=',')
        print(request.form['target'],file=csvfile,newline=',')
        print(request.form['result'],file=csvfile)
    return 'ok from server'

# @app.route('/mogumogu', methods=[])
# def complete():
#     return 'go'

if __name__ == "__main__":
    app.run(threaded=True, debug=True, host='0.0.0.0', port=5000)
