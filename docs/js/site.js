(function(){
var d=document,h=d.documentElement,$=function(s,c){return(c||d).querySelector(s)},$$=function(s,c){return[].slice.call((c||d).querySelectorAll(s))};
var rm=matchMedia('(prefers-reduced-motion:reduce)').matches,mob=matchMedia('(max-width:800px)'),G=window.gsap,lenis;
if(G&&window.ScrollTrigger)G.registerPlugin(ScrollTrigger);
if(!rm&&window.Lenis&&!mob.matches){lenis=new Lenis({lerp:.11});G.ticker.add(function(t){lenis.raf(t*1000)});G.ticker.lagSmoothing(0);lenis.on('scroll',ScrollTrigger.update)}
function go(el){if(lenis)lenis.scrollTo(el,{offset:-60});else el.scrollIntoView({behavior:rm?'auto':'smooth'})}
d.addEventListener('click',function(e){var a=e.target.closest('a[href*="#"]');if(!a)return;var u=new URL(a.href);if(u.pathname.replace(/index\.html$/,'')!==location.pathname.replace(/index\.html$/,'')||!u.hash)return;var t=$(u.hash);if(t){e.preventDefault();menu(false);go(t);history.replaceState(null,'',u.hash)}});
/* header + menu */
var hd=$('#hd'),dock=$('.dock'),dv=$('#devis');
function onS(){var y=scrollY;hd.classList.toggle('s',y>40);var r=dv.getBoundingClientRect();if(dock)dock.classList.toggle('on',y>innerHeight*1.2&&(r.top>innerHeight*.8||r.bottom<0))}
addEventListener('scroll',onS,{passive:true});onS();
var bg=$('.burger'),mm=$('#mm');function menu(o){d.body.classList.toggle('open',o);bg.setAttribute('aria-expanded',o);bg.setAttribute('aria-label',o?'Fermer le menu':'Ouvrir le menu');mm.inert=!o;if(lenis)o?lenis.stop():lenis.start();d.body.style.overflow=o?'hidden':''}
bg.addEventListener('click',function(){menu(!d.body.classList.contains('open'))});
/* whatsapp widget */
var wd=$('#wdg'),wp=$('#wdp'),wt=$('.wdt');function wtog(o){wd.classList.toggle('on',o);wp.inert=!o;wt.setAttribute('aria-expanded',o)}
wt.addEventListener('click',function(){wtog(!wd.classList.contains('on'))});$('.wdx').addEventListener('click',function(){wtog(false);wt.focus()});
d.addEventListener('keydown',function(e){if(e.key==='Escape'){wtog(false);if(d.body.classList.contains('open'))menu(false);close()}});
/* hero */
var hero=$('.hero');
if(hero&&G){
 var st=$('.stage'),fu=$('.hfull'),im=$('img',fu),hw=$('.hexw',hero),hv=$('.hexv',hero),tx=$('.htx'),he=$('.hend'),A,W,H;
 function ms(){W=st.clientWidth;H=st.clientHeight;var w=hw.offsetWidth*.932,q=hw.offsetHeight*.932,cs=hw.getBoundingClientRect(),s=st.getBoundingClientRect();var x=cs.left-s.left+(cs.width-w)/2,y=cs.top-s.top+(cs.height-q)/2;A=[[x+w/2,y],[x+w,y+q*.17],[x+w,y+q*.83],[x+w/2,y+q],[x,y+q*.83],[x,y+q*.17]];B=[[W/2,-2],[W+2,-2],[W+2,H+2],[W/2,H+2],[-2,H+2],[-2,-2]]}
 var B;function cl(v){return v<0?0:v>1?1:v}function ease(t){return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2}
 function draw(p){var k=ease(cl(p/.72));fu.style.clipPath='polygon('+A.map(function(a,i){return(a[0]+(B[i][0]-a[0])*k).toFixed(1)+'px '+(a[1]+(B[i][1]-a[1])*k).toFixed(1)+'px'}).join(',')+')';
  fu.style.opacity=cl(p/.12);hv.style.opacity=1-cl((p-.06)/.14);$('.hexo',hero).style.opacity=1-cl(p/.25);im.style.transform=mob.matches?'scale('+(1.25-.25*k)+')':'translate('+(18*(1-k))+'%,'+(-9*(1-k))+'%) scale('+(1.6-.6*k)+')';
  var o=cl(p/.4);tx.style.opacity=1-o;tx.style.visibility=o>=1?'hidden':'';tx.style.marginLeft=(-o*90)+'px';
  var f=cl((p-.6)/.25);he.style.opacity=f;he.style.visibility=f>0?'visible':'hidden';he.style.transform='translateY('+(1-f)*40+'px)';hd.classList.toggle('s',scrollY>40)}
 if(!rm){ms();draw(0);ScrollTrigger.create({trigger:hero,start:'top top',end:'bottom bottom',scrub:true,onUpdate:function(s){draw(s.progress)},onRefresh:function(s){var t=hw.style.transform;ms();draw(s.progress)}});
  addEventListener('resize',function(){ms()})}
 var ps=$$('.hexo path',hero);
 h.classList.remove('pre');
 if(!rm&&performance.now()<2300){
  ps.forEach(function(p){var L=p.getTotalLength()*8;p.style.strokeDasharray=L;G.fromTo(p,{strokeDashoffset:L},{strokeDashoffset:0,duration:1.6,ease:'power2.inOut',onComplete:function(){p.style.strokeDasharray=''}})});
  G.fromTo(hv,{scale:.72,autoAlpha:0},{scale:1,autoAlpha:1,duration:1.3,ease:'power3.out',delay:.15,clearProps:'transform'});
  G.from(tx.children,{y:34,autoAlpha:0,duration:1,stagger:.12,ease:'power3.out',delay:.2})}
}else h.classList.remove('pre');
/* reveals */
if(G&&!rm){$$('[data-r]').forEach(function(el){G.from(el,{y:44,opacity:0,duration:1,ease:'power3.out',scrollTrigger:{trigger:el,start:'top 92%',once:true}})});
 $$('.sg').forEach(function(g){G.from($$('li',g),{y:18,opacity:0,duration:.6,stagger:.04,ease:'power2.out',scrollTrigger:{trigger:g,start:'top 85%',once:true}})});
 var ai=$('.abi img');if(ai)G.fromTo(ai,{yPercent:0},{yPercent:-9,ease:'none',scrollTrigger:{trigger:'.abt',start:'top bottom',end:'bottom top',scrub:true}});
 var bs=$('.bas');if(bs)G.fromTo(bs,{'--p':'96%'},{'--p':'50%',duration:1.8,ease:'power3.inOut',scrollTrigger:{trigger:bs,start:'top 70%',once:true},onComplete:function(){$('input',bs).value=50}});
 var mps=$$('.ct2,.fr');if(mps.length)G.from(mps,{opacity:0,y:12,duration:.7,stagger:.09,scrollTrigger:{trigger:'.map',start:'top 80%',once:true}});
 var cs=$('.case');if(cs){ScrollTrigger.matchMedia({'(min-width:801px)':function(){var tr=$('.ctr');G.to(tr,{x:function(){return-(tr.scrollWidth-(innerWidth-$('.ctx').offsetWidth))},ease:'none',scrollTrigger:{trigger:cs,start:'top top',end:'bottom bottom',scrub:.4,invalidateOnRefresh:true}})}})}
}else if(rm){var c=$('.case');if(c&&!mob.matches){c.style.height='auto';$('.ctr').style.overflowX='auto'}}
/* tabs */
var tb=$('.tabs');if(tb){var P=JSON.parse(tb.dataset.pub),bt=$$('button',tb),pn=$('#pn');function sel(i){var p=P[i];bt.forEach(function(b,j){b.setAttribute('aria-selected',j===i);b.tabIndex=j===i?0:-1});pn.setAttribute('aria-labelledby','t'+i);$('p',pn).textContent=p.d;$('ul',pn).innerHTML=p.s.map(function(x){return'<li>'+x+'</li>'}).join('');$('a',pn).href=p.w;var g=$('img',pn);g.src=p.im;if(G&&!rm){G.fromTo(g,{scale:1.15,opacity:0},{scale:1,opacity:1,duration:.9,ease:'power3.out',overwrite:true});G.fromTo($$('.pnt p,.pnt li',pn),{y:16,opacity:0},{y:0,opacity:1,duration:.5,stagger:.05,overwrite:true})}}
 bt.forEach(function(b,i){b.tabIndex=i?-1:0;b.addEventListener('click',function(){sel(i)});b.addEventListener('keydown',function(e){var k=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;if(k){i=(+b.dataset.i+k+bt.length)%bt.length;sel(i);bt[i].focus()}})})}
/* slider */
var bas=$('.bas');if(bas)$('input',bas).addEventListener('input',function(){if(G)G.killTweensOf(bas);bas.style.setProperty('--p',this.value+'%')});
/* peek */
var pk=$('.peek');if(pk&&G&&matchMedia('(hover:hover)').matches){var pi=$('img',pk),X=G.quickTo(pk,'x',{duration:.5,ease:'power3'}),Y=G.quickTo(pk,'y',{duration:.5,ease:'power3'});$$('[data-im]').forEach(function(a){a.addEventListener('mouseenter',function(){pi.src=a.dataset.im;G.to(pk,{opacity:1,scale:1,duration:.35})});a.addEventListener('mouseleave',function(){G.to(pk,{opacity:0,scale:.8,duration:.3})})});var sv0=$('.srv');sv0.addEventListener('mousemove',function(e){X(Math.min(e.clientX+36,innerWidth-270));Y(e.clientY-150)})}
/* reels preview */
$$('.rl').forEach(function(r){var v=$('video',r);function on(){if(!v.src)v.src=v.dataset.src;var p=v.play();if(p)p.then(function(){r.classList.add('pl')}).catch(function(){})}function off(){v.pause();r.classList.remove('pl')}
 if(matchMedia('(hover:hover)').matches){r.addEventListener('mouseenter',on);r.addEventListener('mouseleave',off)}
 else if('IntersectionObserver'in window&&!rm)new IntersectionObserver(function(e){e[0].intersectionRatio>.75?on():off()},{threshold:[0,.75]}).observe(r)});
/* viewer */
var sv=$('#sv'),sm=$('.svm'),sp=$('.svp'),sx=$('.svt'),mode,gi,ii,raf,last,t0;
function esc(s){return(s||'').replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function show(){cancelAnimationFrame(raf);sm.innerHTML='';
 if(mode==='s'){var g=ST[gi],it=g.items[ii];sv.classList.remove('sq');sp.innerHTML=g.items.map(function(_,j){return'<i><b style="width:'+(j<ii?100:0)+'%"></b></i>'}).join('');var bar=sp.children[ii].firstChild;
  if(it.v){var v=d.createElement('video');v.src=it.v;v.poster=it.p;v.playsInline=true;v.muted=true;v.autoplay=true;sm.appendChild(v);v.onended=function(){nav(1)};(function f(){if(v.duration)bar.style.width=v.currentTime/v.duration*100+'%';raf=requestAnimationFrame(f)})();v.play().catch(function(){})}
  else{var m=new Image();m.src=it.p;m.alt=g.title;sm.appendChild(m);t0=performance.now();(function f(n){var k=(performance.now()-t0)/5500;bar.style.width=Math.min(k,1)*100+'%';if(k>=1)nav(1);else raf=requestAnimationFrame(f)})()}
  txt(g.title,it.d,it.c,it.u)}
 else if(mode==='p'){sv.classList.add('sq');var p=PO[gi],q=new Image();q.src=p.p;q.alt=p.t;sm.appendChild(q);txt(p.t,p.d,p.c,p.u)}
 else{sv.classList.add('sq');var z=ZO[gi],y=new Image();y.src=z.dataset.zoom;y.alt=$('b',z).textContent;sm.appendChild(y);txt($('b',z).textContent,'',$('figcaption span',z).textContent)}}
var ZO=$$('.rg');
function txt(t,dt,c,u){sx.innerHTML='<h3>'+esc(t)+'</h3>'+(dt?'<time>'+esc(dt)+'</time>':'')+'<p>'+esc(c)+'</p>'+(u?'<a class="lk" target="_blank" rel="noopener" href="'+u+'"><svg class="i"><use href="#i-ig"/></svg>Voir sur Instagram</a>':'')}
function nav(k){if(mode==='s'){ii+=k;if(ii>=ST[gi].items.length){gi++;ii=0}else if(ii<0){gi--;ii=0}if(gi>=ST.length||gi<0)return close()}else{var n=mode==='p'?PO.length:ZO.length;gi=(gi+k+n)%n}show()}
function open(m,g,i){mode=m;gi=g;ii=i||0;last=d.activeElement;sv.hidden=false;d.body.style.overflow='hidden';if(lenis)lenis.stop();show();$('.svx').focus()}
function close(){if(sv.hidden)return;cancelAnimationFrame(raf);sv.hidden=true;sm.innerHTML='';d.body.style.overflow='';if(lenis)lenis.start();if(last)last.focus({preventScroll:true})}
$('.svx').addEventListener('click',close);$('.sva.l').addEventListener('click',function(){nav(-1)});$('.sva.r').addEventListener('click',function(){nav(1)});sv.addEventListener('click',function(e){if(e.target===sv)close()});
d.addEventListener('keydown',function(e){if(sv.hidden)return;if(e.key==='ArrowRight')nav(1);if(e.key==='ArrowLeft')nav(-1);if(e.key==='Tab'){var f=$$('button,a',sv),i=f.indexOf(d.activeElement);e.preventDefault();f[(i+(e.shiftKey?-1:1)+f.length)%f.length].focus()}});
$$('[data-story]').forEach(function(b){b.addEventListener('click',function(){var i=ST.findIndex(function(s){return s.id===b.dataset.story});if(i>-1)open('s',i)})});
$$('[data-post]').forEach(function(b){b.addEventListener('click',function(){open('p',+b.dataset.post)})});
ZO.forEach(function(z,i){z.tabIndex=0;z.setAttribute('role','button');z.addEventListener('click',function(){open('z',i)});z.addEventListener('keydown',function(e){if(e.key==='Enter')open('z',i)})});
/* wizard */
$$('.wz').forEach(function(f){var s=$$('.st',f),n=0,nx=$('.next',f),bk=$('.back',f),sd=$('.send',f),er=$('.err',f);
 function up(){s.forEach(function(x,i){x.classList.toggle('on',i===n)});$('.wzp i',f).style.width=(n+1)*33.34+'%';bk.hidden=!n;nx.hidden=n===2;nx.style.display=n===2?'none':'';sd.hidden=n!==2;if(G&&!rm)G.from(s[n],{x:24,opacity:0,duration:.45,clearProps:'all'});if(window.ScrollTrigger)ScrollTrigger.refresh()}
 nx.addEventListener('click',function(){n++;up()});bk.addEventListener('click',function(){n--;up()});
 $$('input[name=besoin]',f).forEach(function(r){r.addEventListener('click',function(e){if(e.detail>0||e.pointerType)setTimeout(function(){if(n===0){n=1;up()}},260)})});
 function val(k){var e=f.elements[k];return e?(e.value||'').trim():''}
 function msg(){if(!val('nom')){er.textContent='Indiquez votre nom pour que nous puissions vous répondre.';f.elements.nom.focus();return}er.textContent='';return['Bonjour Urba-Net, j’aimerais un devis.','',(val('besoin')?'Besoin : '+val('besoin'):''),'Profil : '+val('qui'),'Délai : '+val('delai'),val('lieu')&&'Localité : '+val('lieu'),'Nom : '+val('nom'),val('tel')&&'Téléphone : '+val('tel'),val('msg')&&'Projet : '+val('msg')].filter(function(x,i){return i===1||x}).join('\n')}
 f.addEventListener('submit',function(e){e.preventDefault();if(n<2){n++;up();return}var m=msg();if(m)window.open('https://wa.me/41793631012?text='+encodeURIComponent(m),'_blank','noopener')});
 $('.mailb',f).addEventListener('click',function(){var m=msg();if(m)location.href='mailto:info@urba-net.ch?subject='+encodeURIComponent('Demande de devis, '+val('nom'))+'&body='+encodeURIComponent(m)})});
addEventListener('load',function(){if(window.ScrollTrigger)ScrollTrigger.refresh();if(location.hash&&$(location.hash))setTimeout(function(){go($(location.hash))},100)});
})();
