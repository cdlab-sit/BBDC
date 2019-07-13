from flask import Flask, render_template, request, jsonify
import csv, random, datetime

app = Flask(__name__)

filename = ''

@app.route('/host')
def host():
    global filename
    dt_now = datetime.datetime.now()
    filename = 'csv/' + dt_now.strftime('%Y_%m_%d_%H:%M:%S')
    with open(filename,'w') as csvfile:
        writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
        writer.writerow(['taskID','target','result'])
        writer.writerow(['0','0','0'])
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
    with open(filename,'r',newline='') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            taskID=int(row['taskID'])
    taskID+=1
    
    # 乱数生成
    target = random.randint(50000,100000)
    #target = 50000 #test
    info = {
        "target": target,
        "taskID": taskID,
    }
    with open(filename,'r',newline='') as csvfile:
        if(len(csvfile.readlines())>=22):
            info = {
                "target": 0,
                "taskID": 0,
            }    
            
    return jsonify(info)

# /user で user.js により呼び出される 
@app.route('/complete-task', methods=['POST'])
def complete():
    with open(filename,'a',newline='') as csvfile:
        print(request.form['taskID'])
        print(request.form['target'])
        print(request.form['result'])
        writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
        writer.writerow([request.form['taskID'],request.form['target'],request.form['result']])
    return 'complete-task'

if __name__ == "__main__":
    app.run(threaded=True, debug=True, host='0.0.0.0', port=5000)