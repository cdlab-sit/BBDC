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
var id;
var target;

xhrPost.onload = function(){
    console.log(this.response)
}

xhrGet.onload = function(){
    var response = JSON.parse(xhrGet.response);
    target = response["target"];
    id = response['taskID']
    console.log('id = ' + id )
}

// var mycallback = function(){
//     setTimeout("location.href='/user-waiting'",3000)
// }

window.onload = function(){
    for(;;){
        xhrGet.open('GET', 'make-task', false);
        xhrGet.send(null);
        if (id == "0") break;
        var count = showAllCurrentFunc(target);
        xhrPost.open('POST', 'complete-task', false);
        xhrPost.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
        xhrPost.send('taskID=' + id + '&' + 'result=' + count)
    }
    setTimeout("location.href='/user-waiting'",3000)
}