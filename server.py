import psycopg2
from flask import Flask, render_template, request, jsonify
import csv, random, datetime, os

app = Flask(__name__)


count = 0
filename = 'moguchan'
TASK_NUM = 130   #　処理するタスクの総数
unit = 0
if(TASK_NUM >= 13):
    unit = int(TASK_NUM/13)
    print(unit)
else:
    print('error')

HOST="ec2-107-22-211-248.compute-1.amazonaws.com"
PORT="5432"
DATABASE="d38ht7676qu5i4"
USER="adhglqupkywiuh"
PASSWORD="de69ca1512a8ec40476ab8a61a1f73962046fc12b7d3923e760f9ac8f44aaa45"

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
    conn = psycopg2.connect(host=HOST, port=PORT, database=DATABASE, user=USER, password=PASSWORD)
    cur = conn.cursor()
    # 2週目以降のために初期化
    global filename
    check_table=0 
    cur.execute("SELECT relname FROM pg_stat_user_tables;")
    tables=cur.fetchall()
    
    print("in host :")
    print(tables)

    if(tables != None):
        for i in tables:
            if(filename == i[0]):
                check_table=1
            else:
                print("nono")

    if(check_table==0):
        cur.execute("CREATE TABLE %s(taskID serial ,task integer ,result varchar(30) ,flag integer ,PRIMARY KEY(taskID))" % filename)

    cur.execute("COMMIT")
    cur.close()
    conn.close()

    return render_template('moguchan.html')

# ホスト側の待機
# htmlファイルを返す
@app.route('/host-waiting')
def index():
    # cur.execute("INSERT INTO %s (task, result,flag) VALUES (%d, '%s', %d);" % (filename,0,'0',0))
    return render_template('menu.html')

# hostからrequestを受けとり、タスクの進行度を返す
@app.route('/host-task')
def host_task(): 
    global count
    conn = psycopg2.connect(host=HOST, port=PORT, database=DATABASE, user=USER, password=PASSWORD)
    cur = conn.cursor()
    result = 'false'
    cur.execute("SELECT taskID,result FROM %s WHERE flag=0 AND result!='0';" % filename)
    
    stock_tasks = cur.fetchall()
    if(stock_tasks != None):
        if(len(stock_tasks)>=unit):
            c = count
            count = c+1
            print(count)
            result = 'true'
            print(len(stock_tasks))
            print('in host-task:true')
            for i in range(unit):
                cur.execute("UPDATE %s SET flag=1 WHERE taskID = %d;" % (filename,stock_tasks[i][0]))

    cur.execute("SELECT taskID,result FROM %s WHERE flag=1;" % filename)
    tasks = cur.fetchall()
    if(tasks != None):
        tasks = len(tasks)
        if(tasks>=TASK_NUM):
            cur.execute("DROP TABLE %s;" % filename)
    
    cur.execute("COMMIT")
    cur.close()
    conn.close()
    
    return result

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
    conn = psycopg2.connect(host=HOST, port=PORT, database=DATABASE, user=USER, password=PASSWORD)
    cur = conn.cursor()
    
    check = 0
    cur.execute("SELECT relname FROM pg_stat_user_tables;")
    tables=cur.fetchall()
    for i in tables:
        if i[0] == filename:
            check = 1
    if(check == 0):
        info = {
            "target": 0,
            "taskID": 0,
        }  
        return jsonify(info)

    # 乱数生成
    # target = random.randint(50000,100000)
    target = 5000
    cur.execute("INSERT INTO %s (task, result,flag) VALUES (%d, '%s', %d);" % (filename,target,'0', 0))
    cur.execute("SELECT taskID,task,result FROM %s WHERE result='0';" % filename)
    taskID = cur.fetchone()
    if(taskID != None):
        info = {
            "target": target,
            "taskID": int(taskID[0]),
            }

    cur.execute("COMMIT")
    cur.close()
    conn.close()

    return jsonify(info)

# /user で user.js により呼び出される
# タスク終了時にcsvファイルにタスクの情報を書き込む 
@app.route('/complete-task', methods=['POST'])
def complete():
    conn = psycopg2.connect(host=HOST, port=PORT, database=DATABASE, user=USER, password=PASSWORD)
    cur = conn.cursor()
    
    taskID = request.form['taskID']
    result = request.form['result']
    cur.execute("UPDATE %s SET result='%s' WHERE taskID='%s';" % (filename,result,taskID))

    cur.execute("COMMIT")
    cur.close()
    conn.close()
    
    return 'complete-task'

# flask 設定
if __name__ == "__main__":
    app.run()
