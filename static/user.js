"use strict";

// loadingのdivを取得
var loading = document.getElementById('loading');
// contentsのdivを取得
var contents = document.getElementById('contents');


function judgePrimeNumber(n) {
    if (n === 2) return true;
    for (let i = 2; i < n; i++) {
        if (n % i === 0) return false;
    }
    return true;
};

function showAllCurrentFunc(n, func) {
    // document.write("数値:" + n + "を計算<br><br>");
    // const startTime = Date.now();
    var count = 0;
    for (let i = 1; i < n; i++) {
        if(judgePrimeNumber(i)){
            count++;
        }
    }
    // const endTime = Date.now();
    // document.write(endTime - startTime + "ミリ秒<br>");
    return count;
};

var xhrGet = new XMLHttpRequest();
var xhrPost = new XMLHttpRequest();
var id;
var target;

xhrPost.onload = function(){
    // console.log(this.response)
}

xhrGet.onload = function(){
    var response = JSON.parse(xhrGet.response);
    target = response["target"];
    id = response['taskID']
}

var dig = function(){
    console.log('dig start ')
    xhrGet.open('GET', 'make-task', false);
    xhrGet.send(null);
    console.log('id = ' + id )
    if (id != "0") {
        setTimeout(dig,500);//あとで調整 
    }
    else{
        end();
    }
    var count = showAllCurrentFunc(target);
    xhrPost.open('POST', 'complete-task', false);
    xhrPost.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
    xhrPost.send('taskID=' + id + '&' + 'result=' + count + '&' + 'target=' + target)
}

window.addEventListener("load", dig) 

var end = function(){
    loading.style.display = 'none';
    contents.classList.remove('hidden');
    setTimeout("location.href='/user-waiting'",3000)
}