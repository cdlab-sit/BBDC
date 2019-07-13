var ground_b = "../gif/ground-before-250-250.png";
var ground_a = "../gif/ground-after-250-250.png";
var sutegoro = "../gif/sutegoro-250-250-30.gif";
var pickeler = "../gif/pickel-250-250-30.gif";
var driller = "../gif/drill-250-250-30.gif";
var parking = "../gif/parking-250-250.png";
var diamond = "../gif/treasure-250-250-30.gif";
var yattane = "../gif/yattane-250-250-30.gif";

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
var num = -1;

const mogumogu = document.getElementById('mogumogu')
mogumogu.addEventListener('click', function(){
  if (num == 13)num = 0;
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
});
