// 参照先を格納
var ground_b = "../gif/ground-before-250-250.gif";
var ground_a = "../gif/ground-after-250-250.gif";
var sutegoro = "../gif/sutegoro-250-250-30.gif";
var pickeler = "../gif/pickel-250-250-30.gif";
var driller = "../gif/drill-250-250-30.gif";
var parking = "../gif/parking-250-250.gif";
var diamond = "../gif/treasure-250-250-30.gif";
var yattane = "../gif/yattane-250-250-30.gif";

// 14パターンの参照先を格納した配列を場所ごとに用意
var l1c1_src = new Array(sutegoro,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a);
var l1c2_src = new Array(ground_b,sutegoro,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a);
var l1c3_src = new Array(ground_b,ground_b,sutegoro,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a);
var l1c4_src = new Array(ground_b,ground_b,ground_b,sutegoro,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a);
var l2c4_src = new Array(ground_b,ground_b,ground_b,ground_b,ground_b,pickeler,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a);
var l2c3_src = new Array(ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,pickeler,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a);
var l2c2_src = new Array(ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,pickeler,ground_a,ground_a,ground_a,ground_a,ground_a,ground_a);
var l2c1_src = new Array(ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,pickeler,ground_a,ground_a,ground_a,ground_a,ground_a);
var l3c1_src = new Array(ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,driller,ground_a,ground_a,ground_a);
var l3c2_src = new Array(ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,driller,ground_a,ground_a);
var l3c3_src = new Array(ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,ground_b,driller,parking);
var l3c4_src = new Array(diamond,diamond,diamond,diamond,diamond,diamond,diamond,diamond,diamond,diamond,diamond,diamond,diamond,yattane);
var num = 0;

const mogumogu = document.getElementById('mogumogu')
mogumogu.addEventListener('click', function(){
  // 画像全てを表示パターンごとに読み込み直す
  if(num < 13){
    if (num == 12) {
      clearTimeout(timerId);
      setTimeout(function() {
        location.href = './menu.html?time=' + String(elapsedTime);
      }, 5000)
      num++;
    }
    else num ++;
    document.getElementById("l1c1").src=l1c1_src[num];
    document.getElementById("l1c2").src=l1c2_src[num];
    document.getElementById("l1c3").src=l1c3_src[num];
    document.getElementById("l1c4").src=l1c4_src[num];
    document.getElementById("l2c1").src=l2c1_src[num];
    document.getElementById("l2c2").src=l2c2_src[num];
    document.getElementById("l2c3").src=l2c3_src[num];
    document.getElementById("l2c4").src=l2c4_src[num];
    document.getElementById("l3c1").src=l3c1_src[num];
    document.getElementById("l3c2").src=l3c2_src[num];
    document.getElementById("l3c3").src=l3c3_src[num];
    document.getElementById("l3c4").src=l3c4_src[num];
  }
});

const timer = document.getElementById("timer");

// 経過時間を保存する変数（単位:ミリ秒）
let elapsedTime;
// スタートボタンを押したときのUnix Epoch
let startTime;
// タイマーのID
let timerId;

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

  timer.textContent = `${m}:${s}:${ms}`;
};

// 経過時間の管理と計算を行う関数
const countUp = () => {
  timerId = setTimeout(() => {
    elapsedTime = Date.now() - startTime;
    countUp();
  }, 10);
};

// ページが読み込まれた時にタイム計測開始
window.onload = function(){
  startTime = Date.now();
  countUp();
}
