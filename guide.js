var toc=document.getElementById('toc'),scrim=document.getElementById('scrim'),tb=document.getElementById('tocBtn');
function closeToc(){toc.classList.remove('open');scrim.classList.remove('on');tb.setAttribute('aria-expanded','false');}
tb.addEventListener('click',function(){var o=toc.classList.toggle('open');scrim.classList.toggle('on',o);
 tb.setAttribute('aria-expanded',o?'true':'false');});
scrim.addEventListener('click',closeToc);
toc.addEventListener('click',function(e){if(e.target.tagName==='A'&&window.innerWidth<=980)closeToc();});
document.getElementById('printBtn').addEventListener('click',function(){window.print();});
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeToc();});
var links=[].slice.call(toc.querySelectorAll('a')),
    secs=links.map(function(a){var h=a.getAttribute('href');return h.charAt(0)==='#'?document.getElementById(h.slice(1)):null;}),
    prog=document.getElementById('prog');
function onScroll(){var h=document.documentElement,sc=h.scrollTop||document.body.scrollTop,max=h.scrollHeight-h.clientHeight;
 prog.style.width=(max>0?sc/max*100:0)+'%';
 var cur=0;for(var i=0;i<secs.length;i++){if(secs[i]&&secs[i].getBoundingClientRect().top<140)cur=i;}
 links.forEach(function(a,i){a.classList.toggle('on',i===cur);});}
window.addEventListener('scroll',onScroll,{passive:true});onScroll();

/* ---- knowledge checks. The correct option is stored as a hash, not as an index. ---- */
function fnv(s){var h=0x811c9dc5;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=(h+((h<<1)+(h<<4)+(h<<7)+(h<<8)+(h<<24)))>>>0;}return ('0000000'+h.toString(16)).slice(-8);}
var answered=0,correct=0;
document.querySelectorAll('.kc').forEach(function(card){
 var want=card.dataset.h,id=card.dataset.id,done=false;
 card.querySelectorAll('.opt').forEach(function(btn){btn.addEventListener('click',function(){
  if(done)return;done=true;
  var ok=fnv(id+':'+btn.dataset.a)===want;
  card.querySelectorAll('.opt').forEach(function(b){b.disabled=true;if(fnv(id+':'+b.dataset.a)===want)b.classList.add('right');});
  if(!ok)btn.classList.add('wrong');
  card.querySelector('.fb').classList.add('on');
  answered++;if(ok)correct++;
  var n=document.getElementById('scoreN'),c=document.getElementById('scoreC');
  if(n)n.textContent=answered;if(c)c.textContent=correct;});});});
document.querySelectorAll('.rev').forEach(function(b){b.addEventListener('click',function(){
 var a=b.closest('.resp').querySelector('.ans'),on=a.classList.toggle('on');
 b.textContent=on?'Hide the model answer':'Compare with a model answer';});});
