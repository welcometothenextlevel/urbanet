import json,os,html,hashlib,urllib.parse as U
from content import *
H=os.path.dirname(os.path.abspath(__file__));D=os.path.join(H,'..','docs')
BASE='https://welcometothenextlevel.github.io/urbanet/'
LB,LK=open(H+'/logo_paths.txt').read().split('\n')[:2]
M=json.load(open(H+'/map.json'))
try: STO=json.load(open(H+'/stories.json'))
except Exception: STO=[]
def ver(p): return hashlib.md5(open(os.path.join(D,p),'rb').read()).hexdigest()[:8]
def wa(t='Bonjour Urba-Net, j’aimerais un devis.'): return 'https://wa.me/41793631012?text='+U.quote(t)
def ic(n): return f'<svg class="i" aria-hidden="true"><use href="#i-{n}"/></svg>'
LOGO=f'<svg class="logo" viewBox="275 76 986 776" role="img" aria-label="Urba-Net Facility Services"><path fill-rule="evenodd" d="{LB}"/><path class="l2" fill-rule="evenodd" d="{LK}"/></svg>'
LOGOU='<svg class="logo" viewBox="275 76 986 776" role="img" aria-label="Urba-Net Facility Services"><use href="#lg1"/><use class="l2" href="#lg2"/></svg>'
SPR='''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<path id="lg1" fill-rule="evenodd" d="%s"/><path id="lg2" fill-rule="evenodd" d="%s"/>
<symbol id="i-tel" viewBox="0 0 24 24"><path fill="currentColor" d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></symbol>
<symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2a9.9 9.9 0 0 0-8.5 14.95L2.1 22l5.2-1.36A9.9 9.9 0 1 0 12.04 2zm0 18.1a8.2 8.2 0 0 1-4.18-1.15l-.3-.18-3.08.8.82-3-.2-.3a8.2 8.2 0 1 1 6.94 3.83zm4.5-6.15c-.25-.12-1.46-.72-1.69-.8-.22-.08-.39-.12-.55.12-.16.25-.63.8-.78.96-.14.17-.28.19-.53.07a6.7 6.7 0 0 1-3.35-2.93c-.25-.43.25-.4.72-1.33.08-.17.04-.3-.02-.43-.06-.12-.55-1.33-.76-1.82-.2-.48-.4-.41-.55-.42h-.47c-.16 0-.43.06-.65.3-.22.25-.86.84-.86 2.05s.88 2.38 1 2.54c.12.17 1.73 2.65 4.2 3.71 1.56.67 2.17.73 2.95.61.47-.07 1.46-.6 1.66-1.17.2-.58.2-1.07.14-1.17-.06-.11-.22-.17-.47-.29z"/></symbol>
<symbol id="i-ig" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/></g><circle cx="17.4" cy="6.6" r="1.2" fill="currentColor"/></symbol>
<symbol id="i-li" viewBox="0 0 24 24"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4V21H3zM9.5 9.75h3.8v1.54h.05c.53-.95 1.83-1.95 3.76-1.95 4.02 0 4.77 2.5 4.77 5.8V21h-4v-5.2c0-1.24-.02-2.84-1.8-2.84s-2.08 1.36-2.08 2.75V21h-4z"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.7" d="M3 5.5h18v13H3zM3.5 6l8.5 7 8.5-7"/></symbol>
<symbol id="i-arr" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M4 12h15M13 6l6 6-6 6"/></symbol>
<symbol id="i-x" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" d="M5 5l14 14M19 5L5 19"/></symbol>
<symbol id="i-doc" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.7" d="M6 3h8l4 4v14H6zM9 12h6M9 16h6"/></symbol>
<symbol id="i-play" viewBox="0 0 24 24"><path fill="currentColor" d="M8 5l11 7-11 7z"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.7" d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.6" r="2.3" fill="currentColor"/></symbol>
</defs></svg>'''%(LB,LK)
def img(n,alt,cls='',eager=False,sizes=''):
    from struct import unpack
    b=n
    srcs=''
    base,w=n.rsplit('-',1)
    big=os.path.join(D,'img',base+'-1400.webp')
    if w=='800' and os.path.exists(big): srcs=f' srcset="img/{n}.webp 800w, img/{base}-1400.webp 1400w" sizes="{sizes or "(min-width:900px) 45vw, 92vw"}"'
    return f'<img src="img/{b}.webp"{srcs} alt="{html.escape(alt)}" {"fetchpriority=high" if eager else "loading=lazy"} decoding="async"{f" class={cls!r}" if cls else ""}>'
def head(title,desc,slug,ld=None,home=False):
    u=BASE+slug
    return f'''<!doctype html><html lang="fr-CH"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}"><meta name="robots" content="noindex"><link rel="canonical" href="{u}">
<meta property="og:type" content="website"><meta property="og:locale" content="fr_CH"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{u}"><meta property="og:image" content="{BASE}img/og.jpg"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ffffff"><meta name="format-detection" content="telephone=no"><link rel="icon" href="img/icon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="img/apple.png">
<link rel="preload" href="fonts/albert.woff2" as="font" type="font/woff2" crossorigin>{'<link rel="preload" as="image" href="img/hero-poster.webp">' if home else ''}
<script>document.documentElement.className='js pre'</script><link rel="stylesheet" href="css/site.css?v={ver('css/site.css')}">
{f'<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>' if ld else ''}</head>'''
NAV=[('./#services','Services'),('realisations','Réalisations'),('./#methode','Méthode'),('./#apropos','À propos'),('./#zone','Zone')]
def header():
    sub=''.join(f'<a href="{f["slug"]}">{f["nav"]}</a>' for f in FAM)
    n=f'<div class="dd"><a href="./#services">Services</a><div class="ddp">{sub}</div></div>'+''.join(f'<a href="{h}">{t}</a>' for h,t in NAV[1:])
    return f'''<body>{SPR}<a class="skip" href="#main">Aller au contenu</a>
<header class="hd" id="hd"><a class="brand" href="./" aria-label="Urba-Net, accueil">{LOGOU}</a><nav class="nav" aria-label="Navigation">{n}</nav>
<div class="hda"><a class="tel" href="tel:{TELI}">{ic('tel')}<span>{TEL}</span></a><a class="btn sm" href="#devis">Devis gratuit</a><button class="burger" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mm"><i></i><i></i></button></div></header>
<div class="mm" id="mm" inert><nav aria-label="Menu mobile">{sub}{''.join(f'<a href="{h}">{t}</a>' for h,t in NAV[1:])}<a href="#devis">Devis gratuit</a></nav>
<div class="mmc"><a class="btn" href="tel:{TELI}">{ic('tel')}Appeler le {TEL}</a><a class="btn wa" href="{wa()}" target="_blank" rel="noopener">{ic('wa')}Écrire sur WhatsApp</a></div></div><main id="main">'''
def devis(pre=''):
    fam=[('Entretien régulier','Bureaux, immeuble, conciergerie'),('Fin de bail','Logement ou locaux à rendre'),('Fin de chantier','Après construction ou rénovation'),('Toiture, façade, vitres','Nacelle, haute pression, solaire'),('Après sinistre','Feu, fumée, eau, moisissures'),('Travaux spéciaux','Démolition, débarras, désinfection')]
    r=''.join(f'<label class="opt"><input type="radio" name="besoin" value="{a}"{" checked" if a==pre else ""}><span><b>{a}</b><small>{b}</small></span></label>' for a,b in fam)
    q=''.join(f'<label class="chip"><input type="radio" name="qui" value="{a}"{" checked" if i==0 else ""}><span>{a}</span></label>' for i,a in enumerate(['Particulier','Régie ou PPE','Entreprise','Chantier','Assurance']))
    d=''.join(f'<label class="chip"><input type="radio" name="delai" value="{a}"{" checked" if i==1 else ""}><span>{a}</span></label>' for i,a in enumerate(['Urgent','Ce mois-ci','Plus tard','Contrat régulier']))
    return f'''<section class="devis" id="devis"><div class="w dv"><div class="dvl"><h2>Demandez votre offre, sans engagement</h2><p>Trois questions, puis votre message part directement chez Fabio Costa, sur WhatsApp ou par e-mail. Ajoutez vos photos dans la conversation : elles aident à chiffrer juste.</p>
<ul class="ct"><li><a href="tel:{TELI}">{ic('tel')}<span>Appeler<b>{TEL}</b></span></a></li><li><a href="{wa()}" target="_blank" rel="noopener">{ic('wa')}<span>WhatsApp<b>{TEL}</b></span></a></li><li><a href="mailto:{MAIL}">{ic('mail')}<span>E-mail<b>{MAIL}</b></span></a></li><li><a href="https://maps.google.com/?q=Chemin+de+la+Redoute+2,+1752+Villars-sur-Gl%C3%A2ne" target="_blank" rel="noopener">{ic('pin')}<span>Adresse<b>Chemin de la Redoute 2, 1752 Villars-sur-Glâne</b></span></a></li></ul></div>
<form class="wz" novalidate><div class="wzp" aria-hidden="true"><i></i></div>
<fieldset class="st on"><legend>De quoi avez-vous besoin ?</legend><div class="opts">{r}</div></fieldset>
<fieldset class="st"><legend>Parlez-nous du lieu</legend><p class="lb">Vous êtes</p><div class="chips">{q}</div><p class="lb">Délai</p><div class="chips">{d}</div><label class="fi">Localité<input name="lieu" autocomplete="address-level2" placeholder="Ex. Fribourg"></label></fieldset>
<fieldset class="st"><legend>Où vous répondre ?</legend><div class="two"><label class="fi">Nom<input name="nom" autocomplete="name"></label><label class="fi">Téléphone<input name="tel" type="tel" autocomplete="tel"></label></div><label class="fi">Votre projet<textarea name="msg" rows="4" placeholder="Surface, état des lieux, accès…"></textarea></label><p class="err" role="alert"></p></fieldset>
<div class="wzb"><button type="button" class="back" hidden>Retour</button><button type="button" class="btn next">Continuer {ic('arr')}</button><div class="send" hidden><button type="submit" class="btn wa">{ic('wa')}Envoyer sur WhatsApp</button><button type="button" class="btn ghost mailb">{ic('mail')}Envoyer par e-mail</button></div></div></form></div></section>'''
def footer(extra=''):
    stories=[]
    for s in STO: stories.append(s)
    for k,(t,d,c,x) in REELS.items(): stories.append(dict(id=k,title=t,items=[dict(v=f'video/{k}.mp4',p=f'img/reel-{k}.webp',d=d,c=x,u=f'https://www.instagram.com/reel/{c}/')]))
    pj=[dict(p=f'img/post-{k}-1080.webp',t=t,d=d,c=x,u=f'https://www.instagram.com/p/{c}/') for k,t,d,c,x in POSTS]
    qs=['J’aimerais un devis','Je rends un logement (fin de bail)','C’est urgent, après un sinistre','Toiture, façade ou vitres']
    return f'''</main><footer class="ft"><div class="w ftg"><div><a href="./" class="fl">{LOGOU}</a><p>L’expertise au service de vos espaces.</p><div class="soc"><a href="https://www.instagram.com/urbanet.facility.services" target="_blank" rel="noopener" aria-label="Instagram">{ic('ig')}</a><a href="https://ch.linkedin.com/company/urba-net-facility-services" target="_blank" rel="noopener" aria-label="LinkedIn">{ic('li')}</a><a href="{wa()}" target="_blank" rel="noopener" aria-label="WhatsApp">{ic('wa')}</a></div></div>
<div><h3>Services</h3>{''.join(f'<a href="{f["slug"]}">{f["nav"]}</a>' for f in FAM)}</div><div><h3>Entreprise</h3><a href="realisations">Réalisations</a><a href="./#methode">Méthode</a><a href="./#apropos">À propos</a><a href="./#zone">Zone d’intervention</a></div>
<div><h3>Contact</h3><a href="tel:{TELI}">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a><p>Chemin de la Redoute 2<br>1752 Villars-sur-Glâne</p></div></div><div class="w ftb"><span>© 2026 Urba-Net Facility Services</span><a href="confidentialite">Confidentialité</a></div></footer>
<div class="wdg" id="wdg"><div class="wdp" id="wdp" role="dialog" aria-label="Écrire à Urba-Net sur WhatsApp" inert><div class="wdh"><img src="img/fabio-sq.webp" alt="" width="44" height="44" loading="lazy"><div><b>Fabio Costa</b><span>Urba-Net Facility Services</span></div><button aria-label="Fermer" class="wdx">{ic('x')}</button></div><div class="wdb"><p class="bub">Bonjour, dites-nous en deux mots ce qu’il vous faut. Vous pouvez joindre des photos.</p>{''.join(f'<a href="{wa("Bonjour Urba-Net. "+q+".")}" target="_blank" rel="noopener">{q}</a>' for q in qs)}</div></div><button class="wdt" aria-expanded="false" aria-controls="wdp" aria-label="WhatsApp">{ic('wa')}</button></div>
<div class="bar"><a href="tel:{TELI}">{ic('tel')}Appeler</a><a class="g" href="{wa()}" target="_blank" rel="noopener">{ic('wa')}WhatsApp</a><a class="b" href="#devis">{ic('doc')}Devis gratuit</a></div>
<a class="dock" href="#devis"><span>Devis gratuit</span>{ic('arr')}</a>
<div class="sv" id="sv" role="dialog" aria-modal="true" aria-label="Publications" hidden><button class="svx" aria-label="Fermer">{ic('x')}</button><button class="sva l" aria-label="Précédent">{ic('arr')}</button><div class="svc"><div class="svp"></div><div class="svm"></div></div><div class="svt"></div><button class="sva r" aria-label="Suivant">{ic('arr')}</button></div>
<script>window.ST={json.dumps(stories,ensure_ascii=False)};window.PO={json.dumps(pj,ensure_ascii=False)}</script>
<script src="js/gsap.min.js" defer></script><script src="js/ScrollTrigger.min.js" defer></script><script src="js/lenis.min.js" defer></script><script src="js/site.js?v={ver('js/site.js')}" defer></script></body></html>'''
def bubbles():
    o=''
    for s in STO: o+=f'<button class="sb" data-story="{s["id"]}"><span class="hx"><img src="{s["items"][0]["p"]}" alt="" loading="lazy"></span>{s["title"]}</button>'
    return o
def reels(): return ''.join(f'<button class="rl" data-story="{k}"><img src="img/reel-{k}.webp" alt="{v[0]}" loading="lazy" width="540" height="960"><video muted loop playsinline preload="none" data-src="video/{k}.mp4"></video><span>{ic("play")}<b>{v[0]}</b><small>{v[1]}</small></span></button>' for k,v in REELS.items())
def posts(): return ''.join(f'<button class="po" data-post="{i}"><img src="img/post-{p[0]}-500.webp" alt="{p[1]}" loading="lazy" width="500" height="500"><span>{p[1]}</span></button>' for i,p in enumerate(POSTS))
def social(full=False):
    return f'''<section class="soci" id="instagram"><div class="w"><div class="sh"><h2>Nos interventions, filmées sur place</h2><a class="lk" href="https://www.instagram.com/urbanet.facility.services" target="_blank" rel="noopener">{ic('ig')}@urbanet.facility.services</a></div>{'<div class="sbs">'+bubbles()+'</div>' if STO else ''}</div><div class="rls">{reels()}</div><div class="w"><div class="pos">{posts()}</div></div></section>'''
def hexsvg(): return '<svg class="hexo" viewBox="0 0 100 118" preserveAspectRatio="none" aria-hidden="true"><path d="M0 50V20L50 0L100 20V50"/><path d="M0 68V98L50 118L100 98V68"/></svg>'
def mp():
    C=M['c'];P=M['p'];hi={'10'}
    s=''.join(f'<path class="{"fr" if k=="10" else "ct2"}{" be" if k=="2" else ""}" d="{C[k]}"/>' for k in ['2','25','22','24','26','23','10'])
    t=''
    for n,(x,y) in P.items():
        big=n in('Villars-sur-Glâne','Zermatt')
        t+=f'<g class="pt{" big" if big else ""}" transform="translate({x:.1f} {y:.1f})">'+('<circle class="pg" r="4"/>' if big else '')+f'<circle r="{2.6 if big else 1.6}"/><text {"x=5 y=2.6" if n not in ("Zermatt","Villars-sur-Glâne") else ("x=-6 y=-5 text-anchor=end" if n=="Zermatt" else "x=6 y=-3")}>{n}</text></g>'
    x1,y1=P['Villars-sur-Glâne'];x2,y2=P['Zermatt']
    return f'<svg class="map" viewBox="0 0 330 345" role="img" aria-label="Carte de la Suisse romande, siège à Villars-sur-Glâne, intervention jusqu’à Zermatt">{s}<path class="rt" d="M{x1:.0f} {y1:.0f}Q{x1+70:.0f} {y1+50:.0f} {x2:.0f} {y2:.0f}"/>{t}</svg>'
LD={'@context':'https://schema.org','@type':'LocalBusiness','name':'Urba-Net Facility Services','url':'https://www.urba-net.ch/','telephone':TELI,'email':MAIL,'image':BASE+'img/og.jpg','address':{'@type':'PostalAddress','streetAddress':'Chemin de la Redoute 2','postalCode':'1752','addressLocality':'Villars-sur-Glâne','addressRegion':'FR','addressCountry':'CH'},'areaServed':['Fribourg','Suisse romande'],'founder':{'@type':'Person','name':'Fabio Costa'},'sameAs':['https://www.instagram.com/urbanet.facility.services','https://ch.linkedin.com/company/urba-net-facility-services']}
def home():
    fq={'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQ]}
    sv=''
    for f in FAM:
        sv+=f'<div class="sg"><h3><a href="{f["slug"]}">{f["nav"]}{ic("arr")}</a></h3><img class="sgi" src="img/{f["img"]}.webp" alt="{f["alt"]}" loading="lazy"><ul>'+''.join(f'<li><a href="{f["slug"]}" data-im="img/{im}.webp"><span>{t}</span></a></li>' for t,_,im in f['items'])+'</ul></div>'
    pb=''.join(f'<button role="tab" id="t{i}" aria-controls="pn" aria-selected="{"true" if i==0 else "false"}" data-i="{i}">{p[0]}</button>' for i,p in enumerate(PUB))
    pj=html.escape(json.dumps([dict(t=p[0],d=p[1],s=p[2],w=wa(f'Bonjour Urba-Net, je suis {p[3]}. Voici mon besoin : '),im=f'img/{p[4]}.webp') for p in PUB],ensure_ascii=False))
    p0=PUB[0]
    case=[('incendie-1100','L’état des lieux','Une cuisine après le feu. Suie sur chaque surface, odeur dans chaque pièce.'),('brut-800','On met à nu','Ce qui ne peut pas être sauvé est démonté et évacué.'),('reel-feu','On décontamine','Pierre, bois et charpente sont traités à la main, aspirés, rincés.'),('chambre-800','On prépare la suite','Les pièces sont saines et vides, prêtes pour les corps de métier.'),('chalet-800','On rend les lieux','Sol en pierre lavé, poutres nettes, lumière retrouvée.')]
    cs=''.join(f'<figure class="cp"><div class="cpi"><img src="img/{a}.webp" alt="{b}" loading="lazy"></div><figcaption><b>{b}</b><span>{c}</span></figcaption></figure>' for a,b,c in case)
    met=[('Vous décrivez','Un appel, un message ou trois photos sur WhatsApp suffisent pour commencer.'),('Nous évaluons','Accès, surfaces, délais, moyens techniques. Vous recevez une offre gratuite et personnalisée.'),('Nous intervenons','Produits professionnels, matériel adapté, équipe organisée.'),('Nous contrôlons','Le résultat est vérifié avant de vous rendre les lieux.')]
    return head('Urba-Net | Nettoyage et travaux spéciaux à Fribourg','Entreprise de nettoyage à Fribourg : entretien, fin de bail, fin de chantier, toiture, après sinistre et travaux spéciaux en Suisse romande. Devis gratuit.','',[LD,fq],True)+header()+f'''
<section class="hero"><div class="stage"><div class="hfull"><picture><source media="(max-width:800px)" srcset="img/toit-mobile-900.webp"><img src="img/toit-large-2200.webp" alt="Toiture en tuiles nettoyée par Urba-Net, vue depuis la nacelle" decoding="async"></picture></div>
<div class="htx"><h1>Là où les autres s’arrêtent, nous trouvons la solution.</h1><p>Nettoyage, entretien et travaux spéciaux à Fribourg et dans toute la Suisse romande. Pour les régies, les entreprises, les chantiers et les particuliers.</p><div class="cta"><a class="btn" href="#devis">Devis gratuit {ic('arr')}</a><a class="btn ghost" href="tel:{TELI}">{ic('tel')}{TEL}</a></div></div>
<div class="hexw"><div class="hexv"><video autoplay muted loop playsinline poster="img/hero-poster.webp" preload="auto" aria-hidden="true"><source src="video/hero.mp4" type="video/mp4"></video></div>{hexsvg()}</div>
<div class="hend"><p>L’expertise au service de vos espaces.</p><a class="btn white" href="realisations">Voir les réalisations {ic('arr')}</a></div></div></section>
<section class="pub"><div class="w"><h2 data-r>Vous êtes…</h2><div class="tabs" role="tablist" aria-label="Votre profil" data-pub="{pj}">{pb}</div><div class="pn" id="pn" role="tabpanel" aria-labelledby="t0"><div class="pnt"><p>{p0[1]}</p><ul>{''.join(f'<li>{x}</li>' for x in p0[2])}</ul><a class="btn wa" target="_blank" rel="noopener" href="{wa(f'Bonjour Urba-Net, je suis {p0[3]}. Voici mon besoin : ')}">{ic('wa')}Expliquer mon besoin</a></div><div class="pni"><img src="img/{p0[4]}.webp" alt="" loading="lazy"></div></div></div></section>
<section class="ba"><div class="w bag"><div class="bat" data-r><h2>Le même toit. Faites glisser.</h2><p>Des années de mousse et de pollution, puis les tuiles d’origine. Ce toit a été nettoyé depuis la nacelle.</p><p>Une toiture propre dure plus longtemps et évite des frais plus lourds. Nous nettoyons aussi façades, vitrages et panneaux solaires.</p><div class="cta"><a class="btn" href="{wa('Bonjour Urba-Net, j’aimerais un devis pour le nettoyage de ma toiture. Je vous envoie des photos.')}" target="_blank" rel="noopener">{ic('wa')}Envoyer une photo de mon toit</a><button class="lk" data-story="toiture">{ic('play')}Voir le film</button></div></div>
<div class="bas" style="--p:62%"><img src="img/ba-apres-1200.webp" alt="Toiture après nettoyage" loading="lazy" width="1200" height="1108"><div class="baa"><img src="img/ba-avant-1200.webp" alt="Toiture pendant le nettoyage" loading="lazy" width="1200" height="1108"></div><span class="tg a">Pendant</span><span class="tg b">Après</span><div class="bah"><i></i></div><input type="range" min="0" max="100" value="62" aria-label="Comparer avant et après"></div></div></section>
<section class="srv" id="services"><div class="w"><div class="sh"><h2 data-r>Trois métiers, une seule équipe</h2><p data-r>De l’entretien hebdomadaire d’un bureau à la démolition intérieure à Zermatt.</p></div><div class="sgs">{sv}</div></div><div class="peek" aria-hidden="true"><img alt=""></div></section>
<section class="case"><div class="cst"><div class="ctx"><h2>Après le feu</h2><p>Comment nous remettons en état un lieu sinistré, étape par étape.</p><button class="btn white" data-story="feu">{ic('play')}Voir l’intervention</button></div><div class="ctr">{cs}<div class="cp cend"><p>Un sinistre chez vous ou dans votre immeuble ?</p><a class="btn white" href="tel:{TELI}">{ic('tel')}{TEL}</a><a class="btn wa" href="{wa('Bonjour Urba-Net, j’ai besoin d’une intervention après sinistre.')}" target="_blank" rel="noopener">{ic('wa')}WhatsApp</a></div></div></div></section>
{social()}
<section class="met" id="methode"><div class="w"><h2 data-r>Comment ça se passe</h2><ol class="ml">{''.join(f'<li data-r><b>{a}</b><p>{b}</p></li>' for a,b in met)}</ol></div></section>
<section class="abt" id="apropos"><div class="w abg"><div class="abi"><img src="img/fabio-1100.webp" alt="Fabio Costa, directeur général d’Urba-Net" loading="lazy" width="1100" height="1375"></div><div class="abx" data-r><h2>Faire ce que tout le monde ne fait pas, et être fier du résultat.</h2><p>Nous ne recherchons pas uniquement les interventions faciles. Nous aimons les projets qui nous poussent à progresser et les environnements qui demandent une attention particulière.</p><p>Un travail bien réalisé commence par une bonne compréhension des besoins, une organisation efficace et le souci du détail. Nous voulons des relations durables avec nos clients et nos partenaires.</p><p class="sig"><b>Fabio Costa</b><span>Directeur général</span></p><div class="cta"><a class="btn" href="tel:{TELI}">{ic('tel')}Parler à Fabio</a><a class="lk" href="https://ch.linkedin.com/company/urba-net-facility-services" target="_blank" rel="noopener">{ic('li')}LinkedIn</a></div></div></div></section>
<section class="zon" id="zone"><div class="w zog"><div class="zox" data-r><h2>Basés à Villars-sur-Glâne, partout en Suisse romande</h2><p>Fribourg, Bulle, Morat, Romont, Estavayer-le-Lac, Payerne, Lausanne, Neuchâtel, Sion, Genève… et jusqu’à Zermatt quand le chantier le demande.</p><a class="btn" href="{wa('Bonjour Urba-Net, intervenez-vous dans ma localité ? C’est à : ')}" target="_blank" rel="noopener">{ic('wa')}Demander pour ma localité</a></div>{mp()}</div></section>
<section class="faq"><div class="w fqg"><h2 data-r>Questions fréquentes</h2><div>{''.join(f'<details><summary>{q}<i></i></summary><p>{a}</p></details>' for q,a in FAQ)}</div></div></section>
{devis()}'''+footer()
def svc(f):
    pre={'nettoyage-entretien':'Entretien régulier','nettoyages-specialises':'Toiture, façade, vitres','travaux-speciaux':'Travaux spéciaux'}[f['slug']]
    ld=[dict(LD),{'@context':'https://schema.org','@type':'Service','name':f['h1'],'provider':{'@type':'LocalBusiness','name':'Urba-Net Facility Services'},'areaServed':'Suisse romande','description':f['desc']}]
    it=''.join(f'<article class="it"><div class="iti">{img(im,t)}</div><h2>{t}</h2><p>{d}</p><a class="lk" href="{wa(f"Bonjour Urba-Net, j’aimerais un devis : {t}.")}" target="_blank" rel="noopener">{ic("wa")}Demander un devis</a></article>' for t,d,im in f['items'])
    ot=''.join(f'<a class="ot" href="{g["slug"]}">{img(g["img"],g["alt"])}<span>{g["nav"]}{ic("arr")}</span></a>' for g in FAM if g is not f)
    return head(f['title']+' | Urba-Net' if len(f['title'])<52 else f['title'],f['desc'],f['slug'],ld)+header()+f'''<section class="ph"><div class="w phg"><div class="phx"><h1>{f['h1']}</h1><p>{f['lead']}</p><div class="cta"><a class="btn" href="#devis">Devis gratuit {ic('arr')}</a><a class="btn ghost" href="tel:{TELI}">{ic('tel')}{TEL}</a></div></div><div class="hexw still"><div class="hexv">{img(f['img'],f['alt'],eager=True)}</div>{hexsvg()}</div></div></section>
<section class="its"><div class="w itg">{it}</div></section>
<section class="strip"><button class="sfilm" data-story="{f['film']}"><img src="img/reel-{f['film']}.webp" alt="" loading="lazy"><span>{ic('play')}Voir une intervention en vidéo</span></button></section>
<section class="faq"><div class="w fqg"><h2>Questions fréquentes</h2><div>{''.join(f'<details><summary>{q}<i></i></summary><p>{a}</p></details>' for q,a in FAQ)}</div></div></section>
{devis(pre)}<section class="ots"><div class="w"><div class="otg">{ot}</div></div></section>'''+footer()
def real():
    g=[('chalet-800','Chalet, remise en état après sinistre','Sol en pierre, bois et poutres'),('toit-800','Toiture en tuiles','Nettoyage complet depuis la nacelle'),('musee-900','Site culturel','Intervention en hauteur, en intérieur'),('balcon-900','Chalet de montagne','Terrasse et vitrages'),('solaire-1100','Installation photovoltaïque','Nettoyage des panneaux'),('nacelle-1100','Immeuble en ville','Travail en nacelle'),('bain-900','Salle de bains en pierre','Fin de chantier'),('convoyeur-1100','Ligne de convoyage','Nettoyage industriel'),('couloir-900','Appartement','Fin de bail'),('evier-1100','Cuisine','Fin de bail'),('sdb-900','Salle de bains','Fin de bail'),('appart-800','Appartement neuf','Fin de chantier'),('industrie-1100','Bâtiment industriel','Façade'),('chambre-800','Chambre en bois','Chantier en cours'),('brut-800','Local technique','Chantier en cours'),('incendie-1100','Cuisine sinistrée','Avant intervention')]
    c=''.join(f'<figure class="rg" data-zoom="img/{(a.replace("-800","-1400"))}.webp">{img(a,b)}<figcaption><b>{b}</b><span>{d}</span></figcaption></figure>' for a,b,d in g)
    return head('Réalisations | Urba-Net, nettoyage à Fribourg','Toitures, chalets, sites culturels, installations solaires, immeubles : les interventions d’Urba-Net en photos et en vidéos.','realisations',[LD])+header()+f'''<section class="ph nm"><div class="w"><h1>Des projets qui reflètent notre savoir-faire</h1><p>Sites culturels, chalets, immeubles, installations industrielles. Voici nos interventions en photos et en vidéos.</p></div></section><section class="rgs"><div class="w rgg">{c}</div></section>{social(True)}{devis()}'''+footer()
def conf():
    return head('Confidentialité | Urba-Net','Protection des données du site Urba-Net Facility Services.','confidentialite')+header()+f'''<section class="ph nm"><div class="w prose"><h1>Confidentialité</h1><p>Ce site est édité par Urba-Net Facility Services, Chemin de la Redoute 2, 1752 Villars-sur-Glâne. Contact : <a href="mailto:{MAIL}">{MAIL}</a>.</p><h2>Formulaire de devis</h2><p>Le site n’enregistre aucune donnée. Le formulaire prépare un message que vous envoyez vous-même depuis WhatsApp ou votre messagerie.</p><h2>Cookies et mesure d’audience</h2><p>Ce site n’utilise ni cookie ni outil de suivi. Les polices, images et vidéos sont hébergées avec le site.</p><h2>Services tiers</h2><p>Les liens vers WhatsApp, Instagram, LinkedIn et Google Maps ouvrent des services soumis à leurs propres règles.</p></div></section>{devis()}'''+footer()
W={'index.html':home(),'realisations.html':real(),'confidentialite.html':conf()}
for f in FAM: W[f['slug']+'.html']=svc(f)
for k,v in W.items(): open(os.path.join(D,k),'w').write(v)
open(D+'/404.html','w').write(head('Page introuvable | Urba-Net','Page introuvable','404').replace('<head>','<head><base href="/urbanet/">')+header()+'<section class="ph nm"><div class="w"><h1>Cette page n’existe pas</h1><p><a class="btn" href="./">Retour à l’accueil</a></p></div></section>'+devis()+footer())
open(D+'/.nojekyll','w').write('')
open(D+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}{"" if k=="index.html" else k[:-5]}</loc></url>' for k in W)+'</urlset>')
TOP=''.join('M'+x for x in LB.split('M')[1:] if float(x.replace('C','L').split('L')[0].split()[1])<425)
open(D+'/img/icon.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="456 -60 620 620"><path fill="#0050A3" fill-rule="evenodd" d="{TOP}"/></svg>')
open(D+'/img/logo.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="275 76 986 776"><path fill="#0050A3" fill-rule="evenodd" d="{LB}"/><path fill="#2b3550" fill-rule="evenodd" d="{LK}"/></svg>')
print('ok',{k:len(v) for k,v in W.items()})
