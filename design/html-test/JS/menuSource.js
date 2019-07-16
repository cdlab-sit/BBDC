const menu = document.getElementById('menu');

menu.addEventListener('click', function(){
  location.replace('./moguchan.html');
});

// タイマーのID
let timerId;
// 経過時間を保存する変数（単位:ミリ秒）
let elapsedTime;
const timer = document.getElementById("menutimer");

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

// ページが読み込まれた時に読み込み開始
window.onload = function(){
  let query = location.search;
  let value = query.split('=');

  // queryがなかったら0にする
  if(!location.search.substring(1)) value[1]='0';

  elapsedTime = Number(value[1]);
  updateTimeText();
}
