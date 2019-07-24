// 参照先を格納
const ground_b = "static/img/ground-before-250-250.gif";
const ground_a = "static/img/ground-after-250-250.gif";
const sutegoro = "static/img/sutegoro-250-250-30.gif";
const pickeler = "static/img/pickel-250-250-30.gif";
const driller = "static/img/drill-250-250-30.gif";
const parking = "static/img/parking-250-250.gif";
const diamond = "static/img/treasure-250-250-30.gif";
const yattane = "static/img/yattane-250-250-30.gif";

let num = 0;

const digtimer = document.getElementById('digtimer');
// const mogumogu = document.getElementById('mogumogu');
const timer = document.getElementById("timer");

// 経過時間を保存する変数（単位:ミリ秒）
let elapsedTime;
// スタートボタンを押したときのUnix Epoch
let startTime;
// タイマーのID
let timerId;


// ページが読み込まれた時にタイム計測開始
window.onload = function(){
  // digtimer.style.visibility="hidden";
  // clear.style.visibility="hidden";
  startTime = Date.now();
  countUp();
  setInterval(sendGet, 1000);   
}

// mogumogu.addEventListener('click', function(){
const mogumogu = function(num){

  // 画像全てを表示パターンごとに読み込み直す

    switch (num) {
      case 1:
        document.getElementById("l1c1").src=ground_a;
        document.getElementById("l1c2").src=sutegoro;
        break;
      case 2:
        document.getElementById("l1c2").src=ground_a;
        document.getElementById("l1c3").src=sutegoro;
        break;
      case 3:
        document.getElementById("l1c3").src=ground_a;
        document.getElementById("l1c4").src=sutegoro;
        break;
      case 4:
        document.getElementById("l1c1").src=ground_a;
        document.getElementById("l1c2").src=ground_a;
        document.getElementById("l1c3").src=ground_a;
        document.getElementById("l1c4").src=ground_a;
        break;
      case 5:
        document.getElementById("l2c4").src=pickeler;
        break;
      case 6:
        document.getElementById("l2c3").src=pickeler;
        document.getElementById("l2c4").src=ground_a;
        break;
      case 7:
        document.getElementById("l2c2").src=pickeler;
        document.getElementById("l2c3").src=ground_a;
        break;
      case 8:
        document.getElementById("l2c1").src=pickeler;
        document.getElementById("l2c2").src=ground_a;
        break;
      case 9:
        document.getElementById("l2c1").src=ground_a;
        document.getElementById("l2c2").src=ground_a;
        document.getElementById("l2c3").src=ground_a;
        document.getElementById("l2c4").src=ground_a;
        break;
      case 10:
        document.getElementById("l3c1").src=driller;
        break;
      case 11:
        document.getElementById("l3c1").src=ground_a;
        document.getElementById("l3c2").src=driller;
        break;
      case 12:
        document.getElementById("l3c2").src=ground_a;
        document.getElementById("l3c3").src=driller;
        break;
      case 13:
        document.getElementById("l3c1").src=ground_a;
        document.getElementById("l3c2").src=ground_a;
        document.getElementById("l3c3").src=parking;
        document.getElementById("l3c4").src=yattane;

        let clear = document.createElement('div');
        clear.style.position = 'absolute';

        let clearimg = document.createElement('img');
        clearimg.src='static/img/clear.png';
        clearimg.alt='clear';
        document.getElementById('clear').appendChild(clearimg);

        clearTimeout(timerId);
        document.getElementById('digtimer').innerText = '00:00:000';
        updateTimeText();


        setTimeout(function() {
          location.href = './host-waiting?time=' + String(elapsedTime);
        }, 5000)
        break;
      default:
          break;
  }
};

// 表示される内容をアップデートする関数
const updateTimeText = () => {
  // 1分 = 1000 ミリ秒 * 60秒
  let m = Math.floor(elapsedTime / (1000 * 60));
  // 1分に満たなかったミリ秒のうち，秒となったもの
  let s = Math.floor((elapsedTime % (1000 * 60)) / 1000);
  // 1秒になれなかったもの
  let ms = elapsedTime % 1000;

  // ゼロパディング
  m = `0${m}`.slice(-2);
  s = `0${s}`.slice(-2);
  ms = `00${ms}`.slice(-3);

  digtimer.textContent = `${m}:${s}:${ms}`;
};

// 経過時間の管理と計算を行う関数
const countUp = () => {
  timerId = setTimeout(() => {
    elapsedTime = Date.now() - startTime;
    countUp();
  }, 10);
};

const xhrGet = new XMLHttpRequest();
const sendGet = function(){
  xhrGet.open('GET', 'host-task', false);
  xhrGet.send(null);
  
}

xhrGet.onload = function(){
  if (this.responseText == 'true') {
    num++;
    mogumogu(num);
  }
  console.log('num = ' + num);
}
