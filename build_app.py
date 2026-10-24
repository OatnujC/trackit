import json,re
src=open('gen.py').read()
pre=src.split("for g in groups.values()")[0]
ns={}
exec(pre,ns)
groups=ns['groups'];T=ns['T']
for g in groups.values():
    for e in g: e['img']=T[e['vid']]
data=json.dumps(groups,ensure_ascii=False)
html=r'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0b0f14">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="JT Workout">
<title>JT's Badminton Workout</title>
<style>
:root{--bg:#0b0f14;--card:#151c25;--card2:#1c2531;--line:#263241;--txt:#e9eef4;--mut:#93a1b2;--acc:#c6ff3d;--acc2:#2ee6a6;--warn:#ffb020;--bad:#ff5c6c}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;background:var(--bg);color:var(--txt);font:16px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
body{padding-bottom:calc(150px + env(safe-area-inset-bottom))}
header{position:sticky;top:0;z-index:20;background:rgba(11,15,20,.94);backdrop-filter:blur(8px);padding:calc(10px + env(safe-area-inset-top)) 14px 8px;border-bottom:1px solid var(--line)}
h1{font-size:19px;margin:0 0 2px;letter-spacing:.2px}h1 span{color:var(--acc)}
.sub{color:var(--mut);font-size:13px}
.tabs{display:flex;gap:6px;overflow-x:auto;padding:8px 0 2px;scrollbar-width:none}.tabs::-webkit-scrollbar{display:none}
.tab{flex:0 0 auto;min-width:52px;min-height:44px;padding:6px 12px;border-radius:12px;border:1px solid var(--line);background:var(--card);color:var(--txt);font-weight:600;font-size:14px;cursor:pointer}
.tab.on{background:var(--acc);color:#0b0f14;border-color:var(--acc)}
.tab .today{display:block;font-size:10px;font-weight:700;opacity:.8}
main{max-width:760px;margin:0 auto;padding:12px}
.hero{background:linear-gradient(135deg,#1b2a12,#10202a);border:1px solid var(--line);border-radius:18px;padding:14px;margin-bottom:12px}
.hero h2{margin:0;font-size:22px}.hero p{margin:4px 0 10px;color:var(--mut);font-size:14px}
.bar{height:12px;background:#0006;border-radius:99px;overflow:hidden}.bar i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--acc2),var(--acc));transition:width .3s}
.prow{display:flex;justify-content:space-between;align-items:center;margin-top:8px;font-size:14px;color:var(--mut)}
.btn{min-height:44px;padding:8px 14px;border-radius:12px;border:1px solid var(--line);background:var(--card2);color:var(--txt);font-weight:600;font-size:15px;cursor:pointer}
.btn.pri{background:var(--acc);color:#0b0f14;border-color:var(--acc)}.btn.sm{min-height:36px;padding:4px 10px;font-size:13px}
h3.sec{margin:20px 4px 8px;font-size:15px;text-transform:uppercase;letter-spacing:1px;color:var(--acc)}
.note{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:12px;margin:8px 0;color:var(--mut);font-size:14px}
.note b{color:var(--txt)}
.card{display:grid;grid-template-columns:112px 1fr;gap:12px;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:10px;margin:8px 0}
.card.done{border-color:var(--acc2);background:#122420}
.thumb{width:112px;height:63px;border-radius:10px;object-fit:cover;background:#000;display:block}
.card h4{margin:0;font-size:16px}.sets{color:var(--acc);font-weight:700;font-size:14px;margin:2px 0}.cue{color:var(--mut);font-size:14px;margin:2px 0 6px}
.src{font-size:11px;color:var(--mut);margin-top:4px}
.chk{display:flex;flex-wrap:wrap;gap:8px;margin-top:6px}
.chk label{position:relative}
.chk input{position:absolute;opacity:0;width:1px;height:1px}
.chk span{display:flex;align-items:center;justify-content:center;width:44px;height:44px;border-radius:12px;border:2px solid var(--line);background:var(--card2);font-weight:700;color:var(--mut);cursor:pointer}
.chk input:checked+span{background:var(--acc2);border-color:var(--acc2);color:#0b0f14}
.chk input:focus-visible+span{outline:2px solid var(--acc)}
.actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:6px}
a.watch{display:inline-flex;align-items:center;gap:6px;min-height:40px;padding:6px 12px;border-radius:10px;background:#ff3b3b;color:#fff;text-decoration:none;font-weight:700;font-size:14px}
.rule{border:1px solid var(--warn);background:#2a2110;border-radius:16px;padding:12px;margin:10px 0}
.rule h4{margin:0 0 4px;color:var(--warn)}.rule p{margin:4px 0;font-size:14px}
.hist{list-style:none;padding:0;margin:8px 0 0;font-size:13px;color:var(--mut)}.hist li{padding:3px 0;border-top:1px solid #ffffff10}
.ok{color:var(--acc2);font-weight:700}.stiff{color:var(--bad);font-weight:700}
.cue-row{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:12px;margin:8px 0}.cue-row b{display:block;color:var(--acc);margin-bottom:2px}
table.wk{width:100%;border-collapse:collapse;font-size:14px}table.wk td{padding:8px;border-top:1px solid var(--line)}table.wk tr.cur td{color:var(--acc);font-weight:700}
#timer{position:fixed;left:0;right:0;bottom:0;z-index:30;background:rgba(16,22,30,.97);border-top:1px solid var(--line);padding:8px 12px calc(8px + env(safe-area-inset-bottom));backdrop-filter:blur(8px)}
#timer .in{max-width:760px;margin:0 auto}
.trow{display:flex;gap:6px;align-items:center;flex-wrap:wrap}
#tdisp{font:700 30px/1 ui-monospace,SFMono-Regular,Menlo,monospace;min-width:92px;color:var(--acc)}
#tlabel{font-size:12px;color:var(--mut);width:100%;margin-bottom:4px}
#timer.alarm{animation:fl .4s 6 alternate}@keyframes fl{to{background:#3a4a10}}
#timer .btn{min-height:42px;padding:6px 10px;font-size:14px}
.hide{display:none!important}
@media (min-width:600px){.card{grid-template-columns:160px 1fr}.thumb{width:160px;height:90px}}
</style>
</head>
<body>
<header>
<h1>JT's <span>Badminton</span> Workout</h1>
<div class="sub" id="datesub"></div>
<nav class="tabs" id="tabs"></nav>
</header>
<main id="main"></main>
<div id="timer"><div class="in">
<div id="tlabel">Rest timer</div>
<div class="trow">
<div id="tdisp">1:00</div>
<button class="btn" data-rest="30">30s</button><button class="btn" data-rest="60">60s</button><button class="btn" data-rest="90">90s</button>
<button class="btn pri" id="tgo">Start</button><button class="btn" id="treset">Reset</button>
</div>
<div class="trow" style="margin-top:6px">
<button class="btn sm" id="tint">Intervals 8 × 30/30</button><button class="btn sm" id="tiso">Iso hold 45s</button><button class="btn sm" id="tisox">Iso 5 × 45s</button>
</div>
</div></div>
<script>
"use strict";
var G = __DATA__;
var DAYS=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];
var VIEWS={
 Mon:{title:"Gym + rehab finisher",desc:"About 65–75 min. Plyos first while fresh, then strength, core, conditioning, then the calf finisher.",blocks:[["Gym 1: Warm-up","warmup"],["Gym 2: Plyometrics (do these fresh)","plyo"],["Gym 3: Strength","strength"],["Gym 4: Core","core"],["Gym 5: Conditioning","cond"],["Rehab finisher","fin"]]},
 Tue:{title:"Home routine + court",desc:"15–20 min home routine, then take the cues onto court.",blocks:[["Home routine","home"]],note:"<b>On court:</b> split step on every opponent hit, racket up after every shot, scissor-land-go on smashes, chest proud in the net lunge and push back with 2 quick steps."},
 Wed:{title:"Calf & Achilles rehab",desc:"About 20 min. Slow and controlled. Check the Achilles rule below.",blocks:[["Calf & Achilles rehab","rehab"]],rule:true},
 Thu:{title:"Gym + rehab finisher",desc:"Same as Monday. Try to add a little load or a rep vs Monday.",blocks:[["Gym 1: Warm-up","warmup"],["Gym 2: Plyometrics (do these fresh)","plyo"],["Gym 3: Strength","strength"],["Gym 4: Core","core"],["Gym 5: Conditioning","cond"],["Rehab finisher","fin"]]},
 Fri:{title:"Home + isometric holds",desc:"Light day before matches: home routine plus isometric calf holds. No heavy legs.",blocks:[["Home routine","home"],["Isometric holds","iso"]]},
 Sat:{title:"Match day",desc:"Quick warm-up, then play. Keep the cues simple.",blocks:[["Quick warm-up","sat"]],match:true},
 Sun:{title:"Rest",desc:"Full rest. Easy walk or stretch if you like. Do your morning-after Achilles check.",blocks:[],rule:true}
};
G.fin=[G.rehab[1],G.rehab[3],G.rehab[4]];
G.iso=[G.rehab[0]];
G.sat=[G.warmup[0],G.warmup[1],G.warmup[2],G.plyo[0],G.plyo[4]];
var SECTIONS=[["warmup","Gym 1: Warm-up"],["plyo","Gym 2: Plyometrics"],["strength","Gym 3: Strength"],["core","Gym 4: Core"],["cond","Gym 5: Conditioning"],["rehab","Calf & Achilles rehab"],["home","Home routine"]];
var CUES=[["Chest proud in the lunge","Hinge from the hip crease with a flat back, never fold at the waist. Knee over ankle, not past the toes."],["Scissor, land, go","Switch legs in the air on every smash, land on the left foot and move forward to the net."],["Racket up after every shot","Racket head back in front of your chest before your opponent hits."],["Morning-after Achilles check","Stiff or sore the morning after jumping means two-footed jumps only for a session or two."]];
var MATCH=[["Split step every hit","Small hop as the opponent hits, land on the balls of the feet."],["Racket up","Racket head above your hand between shots, never below the waist."],["Scissor, land, go","After the smash land on the left foot and follow in to the net."],["Don't lift and hang at the net","If you lift, get back to base and defend side-by-side."],["Pace yourself","Against weaker players, play patient, set up the kill; use drives and net shots instead of lifting."]];

function londonDate(){
 try{var p=new Intl.DateTimeFormat("en-GB",{timeZone:"Europe/London",year:"numeric",month:"2-digit",day:"2-digit",weekday:"short"}).formatToParts(new Date());var o={};p.forEach(function(x){o[x.type]=x.value});return {key:o.year+"-"+o.month+"-"+o.day,wd:o.weekday.slice(0,3)};}
 catch(e){var d=new Date();return {key:d.toISOString().slice(0,10),wd:DAYS[d.getDay()]};}
}
var TODAY=londonDate();
function load(k,d){try{var v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function save(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
var SK="jtw:"+TODAY.key;
var state=load(SK,{});
var current=load("jtw:view",null);
if(!current||current.date!==TODAY.key) current={date:TODAY.key,v:TODAY.wd};
function esc(s){return String(s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
function nSets(s){var m=/^\s*(\d+)\s*(?:[–-]\s*\d+\s*)?[×x]/.exec(s);if(m){var n=parseInt(m[1],10);return n>0&&n<=10?n:1}return 1}
function restFor(e){return /plyo|Pogo|jump|hop|bound/i.test(e.name)?90:60}

function tabs(){
 var h="";DAYS.slice(1).concat(["Sun"]).forEach(function(d){h+='<button class="tab'+(current.v===d?" on":"")+'" data-v="'+d+'">'+d+(d===TODAY.wd?'<span class="today">TODAY</span>':"")+"</button>"});
 h+='<button class="tab'+(current.v==="all"?" on":"")+'" data-v="all">All</button>';
 h+='<button class="tab'+(current.v==="cues"?" on":"")+'" data-v="cues">Cues</button>';
 h+='<button class="tab'+(current.v==="week"?" on":"")+'" data-v="week">Week</button>';
 document.getElementById("tabs").innerHTML=h;
}
function card(e,blk,i){
 var n=nSets(e.sets),id=blk+"-"+i+"-"+e.vid,c="",done=0,arr=state[id]||[];
 for(var k=0;k<n;k++){var on=!!arr[k];if(on)done++;c+='<label><input type="checkbox" data-id="'+id+'" data-k="'+k+'" data-n="'+n+'"'+(on?" checked":"")+' aria-label="'+esc(e.name)+' set '+(k+1)+'"><span>'+(n>1?k+1:"✓")+"</span></label>"}
 return '<div class="card'+(done===n?" done":"")+'" data-card="'+id+'"><img class="thumb" alt="Demo: '+esc(e.vt)+'" src="'+e.img+'"><div><h4>'+esc(e.name)+'</h4><div class="sets">'+esc(e.sets)+'</div><div class="cue">'+esc(e.cue)+'</div><div class="actions"><a class="watch" target="_blank" rel="noopener" href="https://www.youtube.com/watch?v='+e.vid+'">▶ Watch demo</a><button class="btn sm" data-rest="'+restFor(e)+'">Rest '+restFor(e)+'s</button></div><div class="chk">'+c+'</div><div class="src">'+esc(e.vt)+" · "+esc(e.ch)+"</div></div></div>";
}
function ruleBox(){
 var hist=load("jtw:checkins",[]),today=hist.filter(function(x){return x.d===TODAY.key})[0];
 var h='<div class="rule"><h4>⚠ Achilles rule</h4><p>Pain up to <b>3/10</b> during training is fine, as long as it has settled by the next morning.</p><p>Stiff or sore the <b>morning after</b>? Only two-footed jumps for a session or two, then build back up.</p>';
 h+='<p style="margin-top:8px"><b>Morning-after check-in'+(today?" (today: <span class=\""+today.s+"\">"+today.s.toUpperCase()+"</span>)":"")+'</b></p><div class="actions"><button class="btn" data-ci="ok">👍 OK</button><button class="btn" data-ci="stiff">⚠ Stiff / sore</button></div>';
 if(today&&today.s==="stiff")h+='<p class="stiff">Today: two-footed jumps only, skip single-leg hops and bounds.</p>';
 if(hist.length){h+='<ul class="hist">';hist.slice(-10).reverse().forEach(function(x){h+='<li>'+esc(x.d)+' — <span class="'+x.s+'">'+x.s+'</span></li>'});h+="</ul>"}
 return h+"</div>";
}
function cuesHtml(){var h='<h3 class="sec">Coaching cues</h3>';CUES.forEach(function(c){h+='<div class="cue-row"><b>'+esc(c[0])+"</b>"+esc(c[1])+"</div>"});return h}
function progress(blocks){
 var t=0,d=0;blocks.forEach(function(b){G[b[1]].forEach(function(e,i){var n=nSets(e.sets),arr=state[b[1]+"-"+i+"-"+e.vid]||[];t+=n;for(var k=0;k<n;k++)if(arr[k])d++})});return [d,t];
}
function render(){
 tabs();
 var v=current.v,h="",m=document.getElementById("main");
 document.getElementById("datesub").textContent="Today: "+TODAY.wd+" "+TODAY.key+" · "+(VIEWS[TODAY.wd]?VIEWS[TODAY.wd].title:"");
 if(VIEWS[v]){
  var V=VIEWS[v],p=progress(V.blocks),pc=p[1]?Math.round(p[0]/p[1]*100):0;
  h+='<section class="hero"><h2>'+v+": "+esc(V.title)+(v===TODAY.wd?" <small style=\"color:var(--acc);font-size:13px\">TODAY</small>":"")+'</h2><p>'+esc(V.desc)+'</p>';
  if(p[1])h+='<div class="bar"><i id="pbar" style="width:'+pc+'%"></i></div><div class="prow"><span id="ptxt">'+p[0]+" / "+p[1]+" sets · "+pc+'%</span><button class="btn sm" id="resetday">Reset today</button></div>';
  h+="</section>";
  if(V.rule||V.blocks.some(function(b){return b[1]==="plyo"}))h+=ruleBox();
  if(V.note)h+='<div class="note">'+V.note+"</div>";
  if(V.match){h+='<h3 class="sec">Match-day cues</h3>';MATCH.forEach(function(c){h+='<div class="cue-row"><b>'+esc(c[0])+"</b>"+esc(c[1])+"</div>"})}
  V.blocks.forEach(function(b){h+='<h3 class="sec">'+esc(b[0])+"</h3>";G[b[1]].forEach(function(e,i){h+=card(e,b[1],i)})});
  if(v==="Sun")h+=cuesHtml();
 }else if(v==="all"){
  h+='<section class="hero"><h2>All sections</h2><p>Every exercise in the plan. Ticks here are saved for today too.</p></section>';
  SECTIONS.forEach(function(s){h+='<h3 class="sec">'+esc(s[1])+"</h3>";G[s[0]].forEach(function(e,i){h+=card(e,s[0],i)})});
  h+=ruleBox()+cuesHtml();
 }else if(v==="cues"){h+=cuesHtml()+ruleBox()}
 else if(v==="week"){
  h+='<section class="hero"><h2>Weekly schedule</h2><p>No heavy legs or calf work the day before you play.</p></section><div class="note"><table class="wk">';
  ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"].forEach(function(d){h+='<tr class="'+(d===TODAY.wd?"cur":"")+'"><td>'+d+"</td><td>"+esc(VIEWS[d].title)+'</td><td><button class="btn sm" data-v="'+d+'">Open</button></td></tr>'});
  h+="</table></div>";
 }
 m.innerHTML=h;
}
function updProgress(){
 var V=VIEWS[current.v];if(!V)return;var p=progress(V.blocks),pc=p[1]?Math.round(p[0]/p[1]*100):0;
 var b=document.getElementById("pbar"),t=document.getElementById("ptxt");if(b)b.style.width=pc+"%";if(t)t.textContent=p[0]+" / "+p[1]+" sets · "+pc+"%"+(pc===100?" 🎉":"");
}
document.addEventListener("click",function(ev){
 var t=ev.target.closest("[data-v],[data-rest],[data-ci],#resetday");if(!t)return;
 if(t.dataset.v){current={date:TODAY.key,v:t.dataset.v};save("jtw:view",current);render();window.scrollTo(0,0);return}
 if(t.dataset.rest){setRest(parseInt(t.dataset.rest,10),true);return}
 if(t.dataset.ci){var hist=load("jtw:checkins",[]).filter(function(x){return x.d!==TODAY.key});hist.push({d:TODAY.key,s:t.dataset.ci});save("jtw:checkins",hist.slice(-60));render();return}
 if(t.id==="resetday"){if(confirm("Clear all ticks for today?")){state={};save(SK,state);render()}}
});
document.addEventListener("change",function(ev){
 var c=ev.target;if(!c.dataset||!c.dataset.id)return;
 var id=c.dataset.id,n=+c.dataset.n,arr=state[id]||[];arr[+c.dataset.k]=c.checked;state[id]=arr;save(SK,state);
 var done=0;for(var k=0;k<n;k++)if(arr[k])done++;
 document.querySelectorAll('[data-card="'+id+'"]').forEach(function(el){el.classList.toggle("done",done===n)});
 updProgress();
 if(c.checked&&done<n)setRest(restFor({name:id}),true);
});

/* ---------- Timer ---------- */
var T={mode:"rest",len:60,left:60,run:false,iv:null,end:0,phases:null,pi:0};
var actx=null;
function beep(n){try{actx=actx||new (window.AudioContext||window.webkitAudioContext)();for(var i=0;i<(n||3);i++){var o=actx.createOscillator(),g=actx.createGain();o.frequency.value=880;o.connect(g);g.connect(actx.destination);var s=actx.currentTime+i*0.3;g.gain.setValueAtTime(0.3,s);g.gain.exponentialRampToValueAtTime(0.001,s+0.25);o.start(s);o.stop(s+0.26)}}catch(e){}}
function buzz(p){try{if(navigator.vibrate)navigator.vibrate(p)}catch(e){}}
function fmt(s){s=Math.max(0,Math.ceil(s));return Math.floor(s/60)+":"+("0"+s%60).slice(-2)}
function draw(){
 document.getElementById("tdisp").textContent=fmt(T.left);
 document.getElementById("tgo").textContent=T.run?"Pause":"Start";
 var l="Rest timer";if(T.phases){var ph=T.phases[T.pi];l=ph.label+" · "+(T.pi+1)+"/"+T.phases.length}
 document.getElementById("tlabel").textContent=l;
}
function stop(){T.run=false;clearInterval(T.iv);T.iv=null}
function tick(){
 T.left=(T.end-Date.now())/1000;
 if(T.left<=0){
  if(T.phases&&T.pi<T.phases.length-1){T.pi++;var ph=T.phases[T.pi];T.left=ph.s;T.end=Date.now()+ph.s*1000;beep(ph.hard?3:1);buzz(ph.hard?[200,100,200]:200)}
  else{T.left=0;stop();beep(4);buzz([300,150,300,150,300]);var el=document.getElementById("timer");el.classList.remove("alarm");void el.offsetWidth;el.classList.add("alarm")}
 }
 draw();
}
function start(){if(T.left<=0)resetT();try{actx=actx||new (window.AudioContext||window.webkitAudioContext)();if(actx.resume)actx.resume()}catch(e){}T.end=Date.now()+T.left*1000;T.run=true;clearInterval(T.iv);T.iv=setInterval(tick,200);draw()}
function resetT(){stop();if(T.phases){T.pi=0;T.left=T.phases[0].s}else T.left=T.len;draw()}
function setRest(s,go){stop();T.phases=null;T.len=s;T.left=s;draw();if(go)start()}
function setPhases(p){stop();T.phases=p;T.pi=0;T.left=p[0].s;draw()}
document.getElementById("tgo").onclick=function(){T.run?(stop(),draw()):start()};
document.getElementById("treset").onclick=resetT;
document.getElementById("tint").onclick=function(){var p=[{label:"Get ready",s:10}];for(var i=1;i<=8;i++){p.push({label:"HARD "+i+"/8",s:30,hard:true});p.push({label:"Easy "+i+"/8",s:30})}setPhases(p)};
document.getElementById("tiso").onclick=function(){setPhases([{label:"Get ready",s:5},{label:"HOLD",s:45,hard:true}])};
document.getElementById("tisox").onclick=function(){var p=[{label:"Get ready",s:5}];for(var i=1;i<=5;i++){p.push({label:"HOLD "+i+"/5",s:45,hard:true});if(i<5)p.push({label:"Rest "+i+"/4",s:60})}setPhases(p)};
render();draw();
</script>
</body>
</html>
'''
html=html.replace('__DATA__',data)
open('jt-workout-app.html','w').write(html)
print(len(html))
