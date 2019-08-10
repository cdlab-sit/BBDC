from flask import Flask, render_template, request, jsonify
import csv, random, datetime, os

app = Flask(__name__)

filename = './csv/aaa.csv'   #　作成するcsvファイル名
taskID = 0      #　タスクに割り振られるID
TASK_NUM = 130   #　処理するタスクの総数
task_count = 0  #　ホストに伝え終わったタスクのユニット数

# csvディレクトリが存在しない場合にcsvディレクトリを作成
if not os.path.exists('csv'):
    os.mkdir('csv')

# 　キャッシュを保存させない指定
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

# ホスト側の処理中
# csvファイルを作成し、htmlファイルを返す
@app.route('/host')
def host():
    # 2週目以降のために初期化
    global filename,taskID,task_count
    taskID = 0
    task_count = 0

    # データを保存するcsvファイルを作成
    dt_now = datetime.datetime.now()
    try:
        with open(filename,'w') as csvfile:
            writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
            writer.writerow(['taskID','target','result'])
            writer.writerow(['0','0','0'])
            print('just made file')
    except:
        print("error")
    return render_template('moguchan.html')

# ホスト側の待機
# htmlファイルを返す
@app.route('/host-waiting')
def index():
    return render_template('menu.html')

# hostからrequestを受けとり、タスクのユニット進行度を返す
@app.route('/host-task')
def host_task(): 
    global task_count, filename
    task = 0
    result = 'false'
    unit = int(TASK_NUM/13)
    if(task_count*unit > TASK_NUM):
        return result
    try:
        with open(filename,'r',newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                task = int(row['taskID'])
    except:
        result = 'false'
    if((task - task_count*unit) >= unit):
        result = 'true'
        task_count = task_count+1
    # print('in /host-task :' + result)
    return result

# デバッグ用
# @app.route('/test')
# def test():
#     return render_template('test_host-task.html')

# ユーザー側の処理中
# htmlファイルを返す
@app.route('/user')
def cliant():
    return render_template('user.html')

# ユーザー側の待機
# htmlファイルを返す
@app.route('/user-waiting')
def client_waiting():
    return render_template('user-waiting.html')

# ユーザーにタスクを割り振る
# タスクをjson形式で返す
@app.route('/make-task')
def make():
    global taskID, TASK_NUM, filename
    taskID+=1
    
    # 乱数生成
    target = random.randint(50000,100000)
    #target = 50000 #test
    info = {
        "target": target,
        "taskID": taskID,
    }
    try:
        with open(filename,'r',newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # print(type(reader))
            for row in reader:
                # print("in /make-task taskID:" + row['taskID'])
                if(int(row['taskID']) >= TASK_NUM):
                    info = {
                        "target": 0,
                        "taskID": 0,
                    }   
    except:
        info = {
            "target": -1,
            "taskID": -1,
        }
    return jsonify(info)

# /user で user.js により呼び出される
# タスク終了時にcsvファイルにタスクの情報を書き込む 
@app.route('/complete-task', methods=['POST'])
def complete():
    global filename
    with open(filename,'a',newline='') as csvfile:
        # print("in /complete-task taskID:" + request.form['taskID'])
        # print("in /complete-task target:" + request.form['target'])
        # print("in /complete-task result:" + request.form['result'])
        writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
        writer.writerow([request.form['taskID'],request.form['target'],request.form['result']])
    return 'complete-task'

# flask 設定
if __name__ == "__main__":
    app.run(threaded=True, debug=True, host='0.0.0.0', port=5000)
