"use strict";

// loadingのdivを取得

// contentsのdivを取得



function judgePrimeNumber(n) {
    if (n === 2) return true;
    for (let i = 2; i < n; i++) {
        if (n % i === 0) return false;
    }
    return true;
};

function showAllCurrentFunc(n, func) {
    var count = 0;
    for (let i = 1; i < n; i++) {
        setTimeout(judgePrimeNumber(i),1000);
        if(judgePrimeNumber(i)){
            count++;
        }
    }
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
    id = response['taskID'];
}

var end = function(){
    // var contents = document.getElementById('contents');
    // var contents = document.getElementById('contents');
    // cobtents.style.display = 'none';
    // contents.classList.remove('hidden');
    // console.log('end')
    document.getElementById("contents").innerText = "モグちゃんが宝を見つけました!";
    document.getElementById("num").innerText = "";
    setTimeout("location.href='/user-waiting'",3000);
}

var dig = function(){
    // console.log('dig start ');
    xhrGet.open('GET', 'make-task', false);
    xhrGet.send(null);
    console.log('id = ' + id );
    if (id == "0"){
        end();
        return;
    }
    console.log('JS, target =' +  target)
    document.getElementById("num").innerText = target;
    var count = showAllCurrentFunc(target);
    xhrPost.open('POST', 'complete-task', false);
    xhrPost.setRequestHeader('content-type', 'application/x-www-form-urlencoded');
    xhrPost.send('taskID=' + id + '&' + 'result=' + count + '&' + 'target=' + target);
    setTimeout(dig, 0);
}

setTimeout(dig, 500);
