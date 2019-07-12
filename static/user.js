"use strict";

function judgePrimeNumber(n) {
    if (n === 2) return true;
    for (let i = 2; i < n; i++) {
        if (n % i === 0) return false;
    }
    return true;
};

function showAllCurrentFunc(n, func) {
    // document.write("数値:" + n + "を計算<br><br>");
    const startTime = Date.now();
    var count = 0;
    for (let i = 1; i < n; i++) {
        if(judgePrimeNumber(i)){
            count++;
        }
    }
    const endTime = Date.now();
    document.write(endTime - startTime + "ミリ秒<br>");
    return count;
};

var xhrGet = new XMLHttpRequest();
var xhrPost = new XMLHttpRequest();
var isRunning = true;

xhrPost.onload = function(){
    if (this.response == "false") isRunning = false;
    else isRunning = true;
}

xhrGet.onload = function(){
    var response = JSON.parse(xhrGet.response);
    console.log(this.response)
    var target = response["target"];
    var id = response['taskID']
    if (id == 0) return;
    var count = showAllCurrentFunc(target); // varの有無
    xhrPost.open('POST', 'complete-task', false);
    xhrPost.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
    xhrPost.send('taskID=' + response['taskID'] + '&' + 'result=' + count)
    console.log('処理完了')

}

while(isRunning){
    // console.log('isRunning = ' + isRunning)
    xhrGet.open('GET', 'make-task', false);
    xhrGet.send(null);
}
