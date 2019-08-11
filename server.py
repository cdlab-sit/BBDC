from flask import Flask, render_template, request, jsonify
import csv, random, datetime, os

app = Flask(__name__)

filename = "csv/moguchanDB.csv"
TASK_NUM = 39   #　処理するタスクの総数 13以上を指定

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

    # データを保存するcsvファイルを作成
    try:
        with open(filename,'w') as csvfile:
            writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
            writer.writerow(['taskID','target','result','flag'])
            writer.writerow(['0','0','0','0'])
            # print('just made file')
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
    info = {}
    count = 0
    task_yet = 0
    result = 'false'
    unit = int(TASK_NUM/13)

    # 未確認のタスクを確認
    try:
        with open(filename, 'r') as f:
            csv_data = csv.reader(f)
            list = [e for e in csv_data]
    
        for i in range(len(list)):
            if(list[i][3] == '0'):
                task_yet = task_yet + 1     
    except:
        result = 'false'

    # 未確認タスクが一定数以上溜まった場合は"ture"を返す
    if(task_yet >= unit):       
        result = 'true'
        for i in range(len(list)):
            if(list[i][3] == '0'):
                list[i][3] = 1
                count = count + 1
            if(count >= unit):
                break
        # タスクのリストを確認済みにする
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f,delimiter=',',lineterminator='\n')
            writer.writerows(list)

    with open(filename, 'r') as f:
        csv_data = csv.reader(f)
        count = 0
        for e in csv_data:
            count = count + 1
            if(count>2):
                info["tasks"] = {"taskID":e[0], "task":e[1], "result":e[2]}

    info["result"] = result
    return jsonify(info)

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
    count = 0
    dt_now = datetime.datetime.now()
    # %fはミリ秒で[:-3]で3桁まで出力の指定
    taskID = dt_now.strftime('%d%H%M%S%f')[:-3]

    print(taskID)
    
    # 乱数生成
    target = random.randint(50000,100000)
    #target = 50000 #test
    info = {
        "target": target,
        "taskID": taskID,
    }
    try:
        with open(filename,'r') as f:
            csv_data = csv.reader(f)
            list = [e for e in csv_data]
            for row in list:
                if(row[3] == '1'):
                    count = count + 1
    except:
        info = {
            "target": -1,
            "taskID": -1,
        }
    if(count >= TASK_NUM):
        info = {
            "target": 0,
            "taskID": 0,
        }
    return jsonify(info)

# /user で user.js により呼び出される
# タスク終了時にcsvファイルにタスクの情報を書き込む 
@app.route('/complete-task', methods=['POST'])
def complete():
    with open(filename,'a',newline='') as csvfile:
        writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
        writer.writerow([request.form['taskID'],request.form['target'],request.form['result'],0])
    return 'complete-task'

# flask 設定
if __name__ == "__main__":
    app.run(threaded=True, debug=True, host='0.0.0.0', port=5000)