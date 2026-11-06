#!/usr/bin/env python3
"""Builds the Turkish page tr/index.html from index.html.
Run from the repo folder after any change to index.html:  python3 tools/build_tr.py
Every replacement says how many times it must match, so a change to the English page
that breaks the German one stops the build instead of going live half-translated."""
import json, re, os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
s=open(os.path.join(ROOT,'index.html'),encoding='utf-8').read()
NAMES=json.load(open(os.path.join(HERE,'names_tr.json'),encoding='utf-8'))
CAPS={'Kabul': 'Kabil', 'Tirana': 'Tiran', 'Algiers': 'Cezayir', 'Yerevan': 'Erivan', 'Vienna': 'Viyana', 'Baku': 'Bakü', 'Dhaka': 'Dakka', 'Brussels': 'Brüksel', 'Sarajevo': 'Saraybosna', 'Sofia': 'Sofya', 'Beijing': 'Pekin', 'Havana': 'Havana', 'Nicosia': 'Lefkoşa', 'Prague': 'Prag', 'Copenhagen': 'Kopenhag', 'Djibouti': 'Cibuti', 'Kinshasa': 'Kinşasa', 'Cairo': 'Kahire', 'London': 'Londra', 'Tbilisi': 'Tiflis', 'Accra': 'Akra', 'Athens': 'Atina', 'Guatemala City': 'Guatemala', 'Budapest': 'Budapeşte', 'New Delhi': 'Yeni Delhi', 'Jakarta': 'Cakarta', 'Tehran': 'Tahran', 'Baghdad': 'Bağdat', 'Jerusalem': 'Kudüs', 'Rome': 'Roma', 'Kuwait City': 'Kuveyt', 'Bishkek': 'Bişkek', 'Beirut': 'Beyrut', 'Tripoli': 'Trablus', 'Luxembourg': 'Lüksemburg', 'Mexico City': 'Meksiko', 'Chișinău': 'Kişinev', 'Ulan Bator': 'Ulan Batur', 'Kathmandu': 'Katmandu', 'Skopje': 'Üsküp', 'Muscat': 'Maskat', 'Islamabad': 'İslamabad', 'Panama City': 'Panama', 'Warsaw': 'Varşova', 'Lisbon': 'Lizbon', 'Bucharest': 'Bükreş', 'Moscow': 'Moskova', 'Riyadh': 'Riyad', 'Belgrade': 'Belgrad', 'Mogadishu': 'Mogadişu', 'Seoul': 'Seul', 'Colombo': 'Kolombo', 'Khartoum': 'Hartum', 'Damascus': 'Şam', 'Dushanbe': 'Duşanbe', 'Ashgabat': 'Aşkabat', 'Abu Dhabi': 'Abu Dabi', 'Kyiv': 'Kiev', 'Washington D.C.': 'Washington', 'Tashkent': 'Taşkent', "Sana'a": 'Sana', 'Ankara': 'Ankara'}
n_done=0
def rep(old,new,count=1):
    global s,n_done
    c=s.count(old)
    if c!=count: sys.exit(f'build_de: expected {count}× but found {c}× of:\n  {old[:120]}')
    s=s.replace(old,new); n_done+=1
# ---- country names and capitals in the data ----
def name_sub(m):
    i,n=m.group(1),m.group(2); return f'"id": "{i}", "n": "{NAMES.get(i,n)}"'
s,k=re.subn(r'"id": "([A-Z]{3})", "n": "([^"]*)"',name_sub,s)
if k<150: sys.exit('build_de: country names not found')
s=re.sub(r'"cap": "([^"]*)"',lambda m:'"cap": "%s"'%CAPS.get(m.group(1),m.group(1)),s)
# ---- page head ----
rep('<html lang="en">','<html lang="tr">')
rep('<title>Natural Wonders · Where is Bigger?</title>','''<title>Natural Wonders · Hangisi Daha Büyük?</title>
<meta name="description" content="Hangi ülke daha büyük? İki dakika, ücretsiz, üyelik yok.">
<meta property="og:title" content="Hangisi Daha Büyük? · Natural Wonders">
<meta property="og:description" content="Hangi ülke daha büyük? İki dakika, ücretsiz, üyelik yok.">
<meta property="og:image" content="https://twominute.games/tr/card-v1.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="https://twominute.games/natural-wonders-where-is-bigger/tr/">
<meta property="og:locale" content="tr_TR"><meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="en" href="https://twominute.games/natural-wonders-where-is-bigger/">
<link rel="alternate" hreflang="tr" href="https://twominute.games/natural-wonders-where-is-bigger/tr/">''')
# ---- timer ----
rep("'Time left for this question'","'Bu soru için kalan süre'")
rep("`${s} second${s===1?'':'s'}`:`${Math.floor(s/60)} min ${s%60} s`","`${s} saniye`:`${Math.floor(s/60)} dk ${s%60} sn`")
rep("${right}/${total} in ${this.fmt(secs)}","${right}/${total}, ${this.fmt(secs)}")
rep("`left the page ${this.left} time${this.left===1?'':'s'}`:'stayed on the page throughout'","`sayfadan ${this.left} kez ayrıldın`:'baştan sona sayfada kaldın'")
rep('<div class="label">Timer</div>','<div class="label">Süre</div>')
rep('⏱ Timed<small>','⏱ Süreli<small>')
rep('No timer<small>Take your time</small>','Süresiz<small>Acele etme</small>')
# ---- home countries, İstanbul instead of Wales, Turkish numbers and suffixes ----
rep("const WALES=20782;","""const WALES=20782;
const HOME=new Set(['TUR','GRC','BGR','GEO','ARM','AZE','IRN','IRQ','SYR']);const IST=5196;
/* Turkish ablative suffix after a name, following vowel harmony: Almanya'dan, İran'dan, Mısır'dan, ABD'den, Fildişi Sahili'nden */
function abl(n){const s=String(n).trim(),last=s.split(/[\\s-]+/).pop();if(/^[A-ZÇĞİÖŞÜ]{2,}$/.test(last))return /A$/.test(last)?"'dan":"'den";
  const lo=s.toLocaleLowerCase('tr'),v=(lo.match(/[aıoueiöü](?=[^aıoueiöü]*$)/)||['e'])[0],back='aıou'.includes(v);
  if(/(cumhuriyeti|sahili|ginesi)$/.test(lo))return "'n"+(back?'dan':'den');
  return "'"+(/[fstkçşhp]$/.test(lo)?'t':'d')+(back?'a':'e')+'n'}""")
rep("COUNTRIES.filter(c=>UKSET.has(c.id))","COUNTRIES.filter(c=>HOME.has(c.id))",2)
rep("COUNTRIES.filter(c=>!UKSET.has(c.id))","COUNTRIES.filter(c=>!HOME.has(c.id))",2)
rep("const fmt=n=>n.toLocaleString('en-GB');","const fmt=n=>n.toLocaleString('tr-TR');const dec=(x,d)=>x.toFixed(d).replace('.',',');")
rep("function wales(a){const w=a/WALES;if(Math.abs(w-1)<.005)return 'exactly 1 Wales';if(w>=100)return '≈ '+fmt(Math.round(w))+' Waleses';if(w>=1)return '≈ '+w.toFixed(1)+' Waleses';return '≈ '+(w<.1?w.toFixed(2):w.toFixed(1))+' of a Wales'}",
    "function wales(a){const w=a/IST;if(Math.abs(w-1)<.005)return 'tam 1 İstanbul';if(w>=100)return '≈ '+fmt(Math.round(w))+' İstanbul';if(w>=1)return '≈ '+dec(w,1)+' İstanbul';return '≈ '+dec(w,w<.1?2:1)+' İstanbul'}")
rep("function multTxt(r){return r>=10?Math.round(r)+'×':r>=.1?r.toFixed(1)+'×':r>=.01?r.toFixed(2)+'×':r.toFixed(3)+'×'}",
    "function multTxt(r){return r>=10?Math.round(r)+'×':r>=.1?dec(r,1)+'×':r>=.01?dec(r,2)+'×':dec(r,3)+'×'}")
rep('aria-label="Country silhouette"','aria-label="Ülke silueti"')
# ---- option lists ----
rep("const MODES={names:{t:'Mode 1 — Silhouette + name',s:'See the shape and the name'},hidden:{t:'Mode 2 — Silhouette only',s:'Just the shape. Names revealed at the end'}};",
    "const MODES={names:{t:'Mod 1 — Siluet + ad',s:'Şekli ve adı gör'},hidden:{t:'Mod 2 — Yalnızca siluet',s:'Yalnızca şekil. Adlar sonunda açıklanır'}};")
rep("const DIFFS3T={easy:{t:'Easy',s:'Giants and tiddlers'},medium:{t:'Medium',s:'1.3× to 3× the target'},hard:{t:'Hard',s:'Close to the target’s size'}};",
    "const DIFFS3T={easy:{t:'Kolay',s:'Devler ve cüceler'},medium:{t:'Orta',s:'Hedefin 1,3 ile 3 katı'},hard:{t:'Zor',s:'Hedefe yakın büyüklükte'}};")
rep("const DIFFS={easy:{t:'Easy',s:'2× to 8× apart',lo:2,hi:8},medium:{t:'Medium',s:'1.3× to 2.2× apart',lo:1.3,hi:2.2},hard:{t:'Hard',s:'Within 35% of each other',lo:1.03,hi:1.35}};",
    "const DIFFS={easy:{t:'Kolay',s:'2 ile 8 kat fark',lo:2,hi:8},medium:{t:'Orta',s:'1,3 ile 2,2 kat fark',lo:1.3,hi:2.2},hard:{t:'Zor',s:'En fazla %35 fark',lo:1.03,hi:1.35}};")
rep("const REGIONS={world:{t:'Whole world',s:'Mixed from every continent'},home:{t:'Home nations',s:'England, Scotland, Wales, NI or UK v the world'},Europe:{t:'Europe'},Asia:{t:'Asia'},Africa:{t:'Africa'},Americas:{t:'Americas & Oceania'}};",
    "const REGIONS={world:{t:'Tüm dünya',s:'Her kıtadan karışık'},home:{t:'Türkiye ve komşuları',s:'Türkiye ve komşuları dünyaya karşı'},Europe:{t:'Avrupa'},Asia:{t:'Asya'},Africa:{t:'Afrika'},Americas:{t:'Amerika ve Okyanusya'}};")
rep("const LAYOUTS={auto:'Auto',phone:'Phone',tablet:'Tablet',desktop:'Desktop'};","const LAYOUTS={auto:'Otomatik',phone:'Telefon',tablet:'Tablet',desktop:'Bilgisayar'};")
# ---- start screen ----
rep('<b>Natural Wonders</b> · Game 8 of 10 · <a href="https://twominute.games/wonders/">All games</a>','<b>Natural Wonders</b> · Oyun 8 / 10 · <a href="https://twominute.games/wonders/">Tüm oyunlar</a>')
rep('<h1>Where is Bigger?</h1>','<h1>Hangisi Daha Büyük?</h1>',3)
rep('Which covers more land? Make all your guesses, then see the real sizes at the end. Prepare to be surprised.','Hangisi daha çok yer kaplıyor? Önce bütün tahminlerini yap, gerçek büyüklükleri sonunda gör. Şaşırmaya hazır ol.')
rep('<div class="label">Game mode</div>','<div class="label">Oyun modu</div>')
rep('<div class="label">Number of rounds</div>','<div class="label">Tur sayısı</div>')
rep('${n} rounds<small>${n*5} answers</small>','${n} tur<small>${n*5} cevap</small>')
rep('<div class="label">Number of pairs</div>','<div class="label">Çift sayısı</div>')
rep('${n} pairs</button>','${n} çift</button>')
rep("TM.menuRow('30 seconds a round')","TM.menuRow('Tur başına 30 saniye')")
rep('<div class="label">Difficulty</div>','<div class="label">Zorluk</div>')
rep('<div class="label">Countries from</div>','<div class="label">Ülkeler</div>')
rep("Start — ${S.mode==='bigger'?S.rounds3+' rounds':S.count+' pairs'}","Başla — ${S.mode==='bigger'?S.rounds3+' tur':S.count+' çift'}")
rep('<p class="foot">Layout <span class="lay">','<p class="foot">Görünüm <span class="lay">')
rep('${COUNTRIES.length} countries · areas are total area in km² (land plus inland water) · Natural Wonders: Where is Bigger ${VERSION} · <button class="srclink" onclick="openSources()">Sources</button>',
    '${COUNTRIES.length} ülke · alanlar km² cinsinden toplam yüzölçümüdür (kara ve iç sular) · Natural Wonders: Hangisi Daha Büyük? ${VERSION} · <button class="srclink" onclick="openSources()">Kaynaklar</button>')
rep("toast('Not enough countries for that combination. Try another region.')","toast('Bu seçim için yeterli ülke yok. Başka bir bölge dene.')")
rep("toast('Not enough countries for that combination. Try fewer pairs or another region.')","toast('Bu seçim için yeterli ülke yok. Daha az çift ya da başka bir bölge dene.')")
# ---- play ----
rep('aria-label="Pick ${named?esc(c.n):\'country \'+k}"','aria-label="${named?esc(c.n):\'Ülke \'+k} seç"')
rep("${side?'→':'←'} key</span>","${side?'→':'←'} tuşu</span>")
rep('<button class="link" onclick="back()">← Previous pair</button>','<button class="link" onclick="back()">← Önceki çift</button>')
rep('<button class="link" onclick="back()">← Previous round</button>','<button class="link" onclick="back()">← Önceki tur</button>')
rep('<button class="link" onclick="quit()">Quit</button>','<button class="link" onclick="quit()">Çık</button>',2)
rep('Which is bigger?<span>Pair ${S.cur+1} of ${S.pairs.length}</span>','Hangisi daha büyük?<span>Çift ${S.cur+1} / ${S.pairs.length}</span>')
rep('Shapes are not drawn to scale. Each one is stretched to fill its box.','Şekiller ölçekli değil. Her biri kutusunu dolduracak kadar büyütüldü.')
# ---- results ----
rep("const rtxt=r<1.1?`only ${((r-1)*100).toFixed(1)}% bigger`:`${r.toFixed(r<10?1:0)}× bigger`;","const rtxt=r<1.1?`yalnızca %${dec((r-1)*100,1)} daha büyük`:`${dec(r,r<10?1:0)} kat daha büyük`;")
rep("${i+1}. ${esc(a.n)} v ${esc(b.n)}","${i+1}. ${esc(a.n)} – ${esc(b.n)}")
rep("${ok?'✓ You got it':S.picks[i]==null?'⏱ Time ran out':'✗ You picked '+esc(p[S.picks[i]].n)}","${ok?'✓ Bildin':S.picks[i]==null?'⏱ Süre doldu':'✗ Seçimin: '+esc(p[S.picks[i]].n)}")
rep('<span class="tstat">${S.times[i].toFixed(1)} s</span>','<span class="tstat">${dec(S.times[i],1)} sn</span>')
rep('<b>${esc(big.n)}</b> is ${rtxt} than <b>${esc(small.n)}</b>','<b>${esc(big.n)}</b>, <b>${esc(small.n)}</b>${abl(small.n)} ${rtxt}')
rep("' · capital '+esc(","' · başkent '+esc(",2)
V=["'Perfect score. Cartographer level.'","'Excellent. You know your maps.'","'Solid effort. A few surprises in there.'","'The map has fooled you a bit.'","'Shapes can be very deceiving!'"]
VT=["'Tam puan. Haritacı seviyesi.'","'Harika. Haritaları iyi biliyorsun.'","'İyi iş. Birkaç sürpriz vardı.'","'Harita seni biraz yanılttı.'","'Şekiller insanı çok yanıltabilir!'"]
for a,b in zip(V,VT): rep(a,b,2)
rep("😲 <b>Biggest surprise:</b> ${esc(surprise.big.n)} is ${surprise.r.toFixed(1)}× the size of ${esc(surprise.small.n)}.","😲 <b>En büyük sürpriz:</b> ${esc(surprise.big.n)}, ${esc(surprise.small.n)}${abl(surprise.small.n)} ${dec(surprise.r,1)} kat daha büyük.")
rep("🎯 <b>Closest call:</b> ${esc(closest.big.n)} beats ${esc(closest.small.n)} by just ${fmt(closest.big.a-closest.small.a)} km².","🎯 <b>Kıl payı:</b> ${esc(closest.big.n)}, ${esc(closest.small.n)}${abl(closest.small.n)} yalnızca ${fmt(closest.big.a-closest.small.a)} km² daha büyük.")
rep('<h1>Results</h1>','<h1>Sonuçlar</h1>',2)
rep('onclick="startGame()">Play again</button>','onclick="startGame()">Tekrar oyna</button>',2)
rep('onclick="quit()">Change settings</button>','onclick="quit()">Ayarları değiştir</button>',2)
rep('>Share score</button>','>Skoru paylaş</button>',2)
rep('<button class="btn ghost" onclick="openSources()">Sources</button>','<button class="btn ghost" onclick="openSources()">Kaynaklar</button>')
rep('href="https://twominute.games/wonders/">More games</a>','href="https://twominute.games/wonders/">Diğer oyunlar</a>')
rep('The answers, drawn to the same scale (bigger country in black)','Cevaplar aynı ölçekte (büyük olan ülke siyah)')
rep('aria-label="Both countries drawn to the same scale"','aria-label="İki ülke aynı ölçekte"')
rep('Areas: CIA World Factbook (final edition, total area); England, Scotland, Wales and Northern Ireland: Office for National Statistics. Outlines: Natural Earth. <button class="srclink" onclick="openSources()">See all sources</button>',
    'Alanlar: CIA World Factbook (son baskı, toplam yüzölçümü); İngiltere, İskoçya, Galler ve Kuzey İrlanda: Office for National Statistics. Sınırlar: Natural Earth. <button class="srclink" onclick="openSources()">Tüm kaynakları gör</button>',2)
# Which of Five results (not offered in this game's menu, translated anyway)
rep("'<span class=\"st ok\">✓ Ticked — correct</span>':'<span class=\"st no\">✗ Ticked — but it’s smaller</span>'","'<span class=\"st ok\">✓ İşaretledin — doğru</span>':'<span class=\"st no\">✗ İşaretledin — ama daha küçük</span>'")
rep("'<span class=\"st ok\">✓ Left blank — correct</span>':'<span class=\"st no\">✗ Missed — it’s bigger</span>'","'<span class=\"st ok\">✓ Boş bıraktın — doğru</span>':'<span class=\"st no\">✗ Kaçırdın — daha büyük</span>'")
rep('<div class="slabel">Round ${ri+1}</div><h3>Bigger than ${esc(t.n)}?</h3>','<div class="slabel">Tur ${ri+1}</div><h3>${esc(t.n)}${abl(t.n)} büyük mü?</h3>')
rep("'Time ran out: your ticks were locked in as they stood':'Answered in '+R.secs.toFixed(1)+' s'","'Süre doldu: işaretlerin olduğu gibi kaydedildi':'Cevap süresi '+dec(R.secs,1)+' sn'")
rep('aria-label="All six countries drawn to the same scale"','aria-label="Altı ülke aynı ölçekte"');rep('All six drawn to the same scale','Altısı aynı ölçekte')
rep("😲 <b>Biggest surprise:</b> ${esc(surprise.c.n)} is ${surprise.r>1?multTxt(surprise.r)+' the size of':'only '+multTxt(surprise.r)+' the size of'} ${esc(surprise.t.n)}.","😲 <b>En büyük sürpriz:</b> ${esc(surprise.c.n)}, ${esc(surprise.t.n)} büyüklüğünün ${surprise.r>1?'':'yalnızca '}${multTxt(surprise.r)} katı.")
rep("🎯 <b>Closest call:</b> ${esc(closest.c.n)} is ${multTxt(closest.r)} the size of ${esc(closest.t.n)}, and you still got it right.","🎯 <b>Kıl payı:</b> ${esc(closest.c.n)}, ${esc(closest.t.n)} büyüklüğünün ${multTxt(closest.r)} katı ve yine de doğru bildin.")
rep('${S.game3.length} rounds ·','${S.game3.length} tur ·')
rep('<div class="label" style="margin-top:28px">Round by round</div>','<div class="label" style="margin-top:28px">Tur tur</div>')
rep("' Keys A–E tick, Enter locks in.'","' A–E tuşları işaretler, Enter kilitler.'")
rep('>Lock in answer<','>Cevabı kilitle<');rep('>Lock in<','>Kilitle<')
rep('>The one to beat<','>Geçilecek ülke<',2);rep('>Your answer<','>Cevabın<',2)
rep("'None ticked'","'Hiçbiri işaretlenmedi'")
rep('Round ${S.cur+1} of ','Tur ${S.cur+1} / ',2)
rep('Tick all that apply. It could be none, it could be all five.','Uygun olanların hepsini işaretle. Hiçbiri de olabilir, beşi de.')
rep('Which are bigger than <em>','Hangileri şundan büyük: <em>');rep('Which of these are bigger than <em>','Bunlardan hangileri şundan büyük: <em>')
# ---- share ----
rep("const t=`Natural Wonders: Where is Bigger. I scored ${r}/${n} (${S.mode==='bigger'?'Bigger than…, ':''}${DIFFS[S.diff].t}, ${REGIONS[S.region].t}). Can you beat me?`;",
    "const t=`Natural Wonders: Hangisi Daha Büyük? ${r}/${n} yaptım (${S.mode==='bigger'?'Hangisi büyük…, ':''}${DIFFS[S.diff].t}, ${REGIONS[S.region].t}). Beni geçebilir misin?`;")
rep("toast('Score copied. Paste it to a friend.')","toast('Skor kopyalandı. Bir arkadaşına gönder.')")
# ---- sources ----
rep('aria-label="Sources"><button class="srcx" onclick="closeSources()">Close</button>','aria-label="Kaynaklar"><button class="srcx" onclick="closeSources()">Kapat</button>')
rep("COUNTRIES.slice().sort((a,b)=>a.n.localeCompare(b.n))","COUNTRIES.slice().sort((a,b)=>a.n.localeCompare(b.n,'tr'))")
rep('<h2>Sources</h2>','<h2>Kaynaklar</h2>')
src_start=s.index('<p class="gf">'); src_end=s.index('<h3>Every country and its area</h3>')
block=s[src_start:src_end]
SRC=[('The figures in this game were taken in good faith from the published sources below in October 2026 and are shown exactly as those sources give them. Different reputable sources measure areas in slightly different ways (for example whether lakes, rivers and coastal waters are included), so you may find other figures elsewhere, and a source can occasionally be wrong. If you think a figure is wrong, this is where it came from.',
      'Bu oyundaki rakamlar Ekim 2026’da aşağıdaki yayımlanmış kaynaklardan iyi niyetle alındı ve kaynakların verdiği şekliyle gösteriliyor. Güvenilir kaynaklar yüzölçümünü biraz farklı biçimlerde ölçer (örneğin göller, nehirler ve kıyı suları dahil mi), bu yüzden başka yerlerde farklı rakamlar görebilirsin; bir kaynak zaman zaman yanılabilir de. Bir rakamın yanlış olduğunu düşünüyorsan, nereden geldiğini burada bulabilirsin.'),
     ('<h3>Country areas</h3>','<h3>Ülke yüzölçümleri</h3>'),
     (', total area (land plus inland water), from its final edition. The CIA stopped publishing the Factbook in February 2026; its data is preserved in the public',', toplam yüzölçümü (kara ve iç sular), son baskısından. CIA, Factbook’u Şubat 2026’da yayımlamayı bıraktı; verileri herkese açık'),
     ('factbook.json archive</a>','factbook.json arşivinde</a> saklanıyor'),
     ("France uses the Factbook's figure for metropolitan France (551,500 km²), to match the outline shown, which leaves out overseas regions such as French Guiana.","Fransa için, gösterilen sınırla uyumlu olsun diye Factbook’un anakara Fransa rakamı (551.500 km²) kullanıldı; Fransız Guyanası gibi denizaşırı bölgeler dahil değil."),
     ("Morocco is not included: the Factbook's figure includes the disputed territory of Western Sahara, so the figure and the outline would not match.","Fas oyunda yok: Factbook’un rakamı tartışmalı Batı Sahra bölgesini de içeriyor, bu yüzden rakam ile sınır uyuşmazdı."),
     ('<h3>England, Scotland, Wales and Northern Ireland</h3>','<h3>İngiltere, İskoçya, Galler ve Kuzey İrlanda</h3>'),
     (', Standard Area Measurements, as given on',', Standard Area Measurements, kaynak:'),
     (': England 130,462 km², Scotland 78,803 km², Wales 20,782 km², Northern Ireland 14,333 km². “Waleses” use Wales at 20,782 km².',': İngiltere 130.462 km², İskoçya 78.803 km², Galler 20.782 km², Kuzey İrlanda 14.333 km².</li><li>İstanbul karşılaştırmalarında, TÜİK’in nüfus yoğunluğu hesabında kullandığı İstanbul ili yüzölçümü olan 5.196 km² kullanıldı.'),
     ('<h3>Capitals</h3>','<h3>Başkentler</h3>'),
     ('The open “world-countries” dataset by Mohammed Le Doze (','Mohammed Le Doze’un açık “world-countries” veri seti ('),
     ('<h3>Maps</h3>','<h3>Haritalar</h3>'),('Country outlines:','Ülke sınırları:'),
     (' (1:10m, public domain). Remote overseas territories are left off the outlines.',' (1:10m, kamu malı). Uzak denizaşırı topraklar sınırlarda gösterilmiyor.')]
for a,b in SRC:
    if block.count(a)!=1: sys.exit('build_tr: sources text changed: '+a[:60])
    block=block.replace(a,b)
block=re.sub(r'\. See (<a [^>]*>)',r'. Ayrıca bkz. \1',block)
s=s[:src_start]+block+s[src_end:]
rep('<h3>Every country and its area</h3><details><summary>${COUNTRIES.length} countries</summary>','<h3>Tüm ülkeler ve yüzölçümleri</h3><details><summary>${COUNTRIES.length} ülke</summary>')
# ---- game switcher strip and "Try next" ----
rep("setAttribute('aria-label','Switch game')","setAttribute('aria-label','Oyun değiştir')")
rep('<a class="home" href="/wonders/">← All games</a>','<a class="home" href="/wonders/">← Tüm oyunlar</a>')
rep("{n:'Where is Bigger?',slug:'where-is-bigger',ic:'bigger',t:'Two countries side by side. Which covers more land? Maps have been fooling you for years.'}","{n:'Hangisi Daha Büyük?',slug:'where-is-bigger',ic:'bigger',t:'Yan yana iki ülke. Hangisi daha büyük? Haritalar yıllardır seni yanıltıyor.'}")
rep('/^Play again$/','/^Tekrar oyna$/')
rep("Try next${rec.games[n.slug]?' · your lowest score':' · not played yet'}","Sıradaki${rec.games[n.slug]?' · en düşük skorun':' · henüz oynanmadı'} · İngilizce")
rep('<span class="go">Play →</span>','<span class="go">Oyna →</span>')
rep('<b>${done} of ${GAMES.length}</b>','<b>${done} / ${GAMES.length}</b>')
rep('</b> Natural Wonders explored</span><a href="/wonders/#record">Your record →</a>','</b> Natural Wonders keşfedildi</span><a href="/wonders/#record">Rekorların →</a>')
# ---- feedback box ----
FB=[("[['idea','💡 Idea','What would make it better?'],['like','👍 Like it','What did you enjoy?'],['wrong','🐞 Something’s wrong','What went wrong, and where?']]","[['idea','💡 Fikir','Ne daha iyi yapardı?'],['like','👍 Beğendim','En çok neyi sevdin?'],['wrong','🐞 Bir sorun var','Ne ters gitti, nerede?']]"),
    ('aria-label="Feedback or report a problem"><h2>Tell us what you think</h2>','aria-label="Görüş bildir ya da sorun bildir"><h2>Ne düşündüğünü söyle</h2>'),
    ('Ideas, likes, gripes or something broken. It goes privately to Two Minute Games; nobody else can read it.','Fikirler, beğeniler, şikâyetler ya da bozuk bir şey. Mesaj yalnızca Two Minute Games’e gider; başka kimse okuyamaz.'),
    ('aria-label="Your message"','aria-label="Mesajın"'),
    ('placeholder="Name or email, only if you’d like a reply (optional)" aria-label="Name or email (optional)"','placeholder="Ad ya da e-posta, yalnızca cevap istersen (isteğe bağlı)" aria-label="Ad ya da e-posta (isteğe bağlı)"'),
    ('We also send which game you were on and your type of device, nothing else.','Ayrıca hangi oyunda olduğunu ve cihaz türünü gönderiyoruz, başka bir şey değil.'),
    ('<button type="button" class="tmgfb-b">Cancel</button><button type="submit" class="tmgfb-b go">Send</button>','<button type="button" class="tmgfb-b">Vazgeç</button><button type="submit" class="tmgfb-b go">Gönder</button>'),
    ("m.textContent='Sending…'","m.textContent='Gönderiliyor…'"),("m.textContent='Thank you. Sent!'","m.textContent='Teşekkürler. Gönderildi!'"),
    ("m.textContent='Couldn’t send just now. Please try again in a moment.'","m.textContent='Şu an gönderilemedi. Lütfen birazdan tekrar dene.'"),
    ("p.setAttribute('aria-label','Feedback or report a problem');p.innerHTML=ICON+'Feedback or bug'","p.setAttribute('aria-label','Görüş bildir ya da sorun bildir');p.innerHTML=ICON+'Görüş ya da hata'")]
for a,b in FB: rep(a,b)
# open on the home region the first time, remembered per language afterwards
rep("localStorage.getItem('wib_settings')","localStorage.getItem('wib_settings_tr')")
rep("localStorage.setItem('wib_settings',","localStorage.setItem('wib_settings_tr',")
rep("region:'world',layout","region:'home',layout")
s=s.replace('<!doctype html>','<!doctype html>\n<!-- GENERATED by tools/build_tr.py from ../index.html. Edit the English page, then run the build again. -->',1)
os.makedirs(os.path.join(ROOT,'tr'),exist_ok=True)
open(os.path.join(ROOT,'tr','index.html'),'w',encoding='utf-8').write(s)
left=sorted(set(re.findall(r"(?:>|')([A-Z][a-z]+(?: [a-z]+){2,}[.?!]?)(?:<|')",s)))
print(f'build_tr: {n_done} replacements, {k} names. Possible English left:',left[:40])
