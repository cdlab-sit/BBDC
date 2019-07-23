from flask import Flask, render_template, request, jsonify
import csv, random, datetime, os

app = Flask(__name__)

filename = ''
taskID = 0
TASK_NUM = 13

if not os.path.exists('csv'):
    os.mkdir('csv')

@app.route('/host')
def host():
    # return 'host'
    return render_template('moguchan.html')

@app.route('/host-waiting')
def index():
    global filename
    dt_now = datetime.datetime.now()
    filename = 'csv/' + dt_now.strftime('%Y_%m_%d_%H:%M:%S')
    with open(filename,'w') as csvfile:
        writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
        writer.writerow(['taskID','target','result'])
        writer.writerow(['0','0','0'])
        print('just made file')
    # return 'host-waiting'
    return render_template('menu.html')

# userからrequestを受けとり、タスクの進行度を返す
@app.route('/host-task')
def host_task():
    with open(filename,'r',newline='') as csvfile:
        tasks = (len(csvfile.readlines())-2)/13 
    return int(tasks)

@app.route('/user')
def cliant():
    return render_template('user.html')

@app.route('/user-waiting')
def client_waiting():
    return render_template('user-waiting.html')

@app.route('/make-task')
def make():
    global taskID, TASK_NUM
    taskID+=1
    
    # 乱数生成
    target = random.randint(50000,100000)
    #target = 50000 #test
    info = {
        "target": target,
        "taskID": taskID,
    }
    with open(filename,'r',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print(type(reader))
        for row in reader:
            # print("in /make-task taskID:" + row['taskID'])
            if(int(row['taskID']) == TASK_NUM):
                print("39 yeah")
                info = {
                    "target": 0,
                    "taskID": 0,
                }    
    return jsonify(info)

# /user で user.js により呼び出される 
@app.route('/complete-task', methods=['POST'])
def complete():
    global filename
    with open(filename,'a',newline='') as csvfile:
        print("in /complete-task taskID:" + request.form['taskID'])
        print("in /complete-task target:" + request.form['target'])
        print("in /complete-task result:" + request.form['result'])
        writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
        writer.writerow([request.form['taskID'],request.form['target'],request.form['result']])
    return 'complete-task'

if __name__ == "__main__":
    app.run(threaded=True, debug=True, host='0.0.0.0', port=5000)