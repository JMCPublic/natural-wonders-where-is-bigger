#!/usr/bin/env python3
"""Builds the German page de/index.html from index.html.
Run from the repo folder after any change to index.html:  python3 tools/build_de.py
Every replacement says how many times it must match, so a change to the English page
that breaks the German one stops the build instead of going live half-translated."""
import json, re, os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
s=open(os.path.join(ROOT,'index.html'),encoding='utf-8').read()
NAMES=json.load(open(os.path.join(HERE,'names_de.json'),encoding='utf-8'))
CAPS={'Vienna':'Wien','Copenhagen':'Kopenhagen','Warsaw':'Warschau','Rome':'Rom','Moscow':'Moskau','Prague':'Prag','Brussels':'Brüssel','Lisbon':'Lissabon','Athens':'Athen','Belgrade':'Belgrad','Bucharest':'Bukarest','Kyiv':'Kyjiw','Kiev':'Kyjiw','Luxembourg':'Luxemburg','Nicosia':'Nikosia','Beijing':'Peking','Tokyo':'Tokio','Mexico City':'Mexiko-Stadt','Cairo':'Kairo','Tehran':'Teheran','Baghdad':'Bagdad','Damascus':'Damaskus','Riyadh':'Riad','Kuwait City':'Kuwait-Stadt','Guatemala City':'Guatemala-Stadt','Panama City':'Panama-Stadt','Algiers':'Algier','Tripoli':'Tripolis','Khartoum':'Khartum','Addis Ababa':'Addis Abeba','Havana':'Havanna','Reykjavik':'Reykjavík','Tbilisi':'Tiflis','Yerevan':'Jerewan','Chisinau':'Chișinău','Kathmandu':'Kathmandu','New Delhi':'Neu-Delhi','Hanoi':'Hanoi','Jerusalem':'Jerusalem','Amman':'Amman','Muscat':'Maskat','Sana\'a':'Sanaa','Mogadishu':'Mogadischu','Dar es Salaam':'Daressalam','Dodoma':'Dodoma','Cape Town':'Kapstadt','Pretoria':'Pretoria','Rabat':'Rabat','Tunis':'Tunis','Bern':'Bern','Berlin':'Berlin','Ulaanbaatar':'Ulan-Bator','Bishkek':'Bischkek','Dushanbe':'Duschanbe','Tashkent':'Taschkent','Ashgabat':'Aschgabat','Port Moresby':'Port Moresby','Singapore':'Singapur','Pyongyang':'Pjöngjang','Kabul':'Kabul','Port of Spain':'Port of Spain','Brasília':'Brasília','Bogotá':'Bogotá','Asunción':'Asunción','Montevideo':'Montevideo','Washington D.C.':'Washington, D.C.','Belmopan':'Belmopan','Djibouti':'Dschibuti','Kingston':'Kingston','Doha':'Doha','Seoul':'Seoul','Quito':'Quito'}
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
rep('<html lang="en">','<html lang="de">')
rep('<title>Natural Wonders · Where is Bigger?</title>','''<title>Natural Wonders · Wo ist es größer?</title>
<meta name="description" content="Welches Land ist größer? Zwei Minuten, kostenlos, ohne Anmeldung.">
<meta property="og:title" content="Wo ist es größer? · Natural Wonders">
<meta property="og:description" content="Welches Land ist größer? Zwei Minuten, kostenlos, ohne Anmeldung.">
<meta property="og:image" content="https://twominute.games/de/card-v1.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="https://twominute.games/natural-wonders-where-is-bigger/de/">
<meta property="og:locale" content="de_DE"><meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="en" href="https://twominute.games/natural-wonders-where-is-bigger/">
<link rel="alternate" hreflang="de" href="https://twominute.games/natural-wonders-where-is-bigger/de/">''')
# ---- timer ----
rep("'Time left for this question'","'Verbleibende Zeit für diese Frage'")
rep("`${s} second${s===1?'':'s'}`","`${s} Sekunde${s===1?'':'n'}`")
rep("`left the page ${this.left} time${this.left===1?'':'s'}`:'stayed on the page throughout'","`Seite ${this.left}-mal verlassen`:'die ganze Zeit auf der Seite geblieben'")
rep('<div class="label">Timer</div>','<div class="label">Zeit</div>')
rep('⏱ Timed<small>','⏱ Mit Zeit<small>')
rep('No timer<small>Take your time</small>','Ohne Zeit<small>Lass dir Zeit</small>')
# ---- home countries, Saarland instead of Wales, German numbers ----
rep("const WALES=20782;","const WALES=20782;\nconst HOME=new Set(['DEU','AUT','CHE','LUX']);const SAAR=2570;")
rep("COUNTRIES.filter(c=>UKSET.has(c.id))","COUNTRIES.filter(c=>HOME.has(c.id))",2)
rep("COUNTRIES.filter(c=>!UKSET.has(c.id))","COUNTRIES.filter(c=>!HOME.has(c.id))",2)
rep("const fmt=n=>n.toLocaleString('en-GB');","const fmt=n=>n.toLocaleString('de-DE');const dec=(x,d)=>x.toFixed(d).replace('.',',');")
rep("function wales(a){const w=a/WALES;if(Math.abs(w-1)<.005)return 'exactly 1 Wales';if(w>=100)return '≈ '+fmt(Math.round(w))+' Waleses';if(w>=1)return '≈ '+w.toFixed(1)+' Waleses';return '≈ '+(w<.1?w.toFixed(2):w.toFixed(1))+' of a Wales'}",
    "function wales(a){const w=a/SAAR;if(Math.abs(w-1)<.005)return 'genau 1 Saarland';if(w>=100)return '≈ '+fmt(Math.round(w))+'-mal das Saarland';if(w>=1)return '≈ '+dec(w,1)+'-mal das Saarland';return '≈ '+dec(w,w<.1?2:1)+' Saarland'}")
rep("function multTxt(r){return r>=10?Math.round(r)+'×':r>=.1?r.toFixed(1)+'×':r>=.01?r.toFixed(2)+'×':r.toFixed(3)+'×'}",
    "function multTxt(r){return r>=10?Math.round(r)+'×':r>=.1?dec(r,1)+'×':r>=.01?dec(r,2)+'×':dec(r,3)+'×'}")
rep('aria-label="Country silhouette"','aria-label="Landesumriss"')
# ---- option lists ----
rep("const MODES={names:{t:'Mode 1 — Silhouette + name',s:'See the shape and the name'},hidden:{t:'Mode 2 — Silhouette only',s:'Just the shape. Names revealed at the end'}};",
    "const MODES={names:{t:'Modus 1 — Umriss + Name',s:'Umriss und Name sehen'},hidden:{t:'Modus 2 — Nur Umriss',s:'Nur der Umriss. Namen erst am Ende'}};")
rep("const DIFFS3T={easy:{t:'Easy',s:'Giants and tiddlers'},medium:{t:'Medium',s:'1.3× to 3× the target'},hard:{t:'Hard',s:'Close to the target’s size'}};",
    "const DIFFS3T={easy:{t:'Leicht',s:'Riesen und Winzlinge'},medium:{t:'Mittel',s:'1,3- bis 3-mal so groß'},hard:{t:'Schwer',s:'Fast so groß wie das Ziel'}};")
rep("const DIFFS={easy:{t:'Easy',s:'2× to 8× apart',lo:2,hi:8},medium:{t:'Medium',s:'1.3× to 2.2× apart',lo:1.3,hi:2.2},hard:{t:'Hard',s:'Within 35% of each other',lo:1.03,hi:1.35}};",
    "const DIFFS={easy:{t:'Leicht',s:'2- bis 8-mal so groß',lo:2,hi:8},medium:{t:'Mittel',s:'1,3- bis 2,2-mal so groß',lo:1.3,hi:2.2},hard:{t:'Schwer',s:'Höchstens 35 % Unterschied',lo:1.03,hi:1.35}};")
rep("const REGIONS={world:{t:'Whole world',s:'Mixed from every continent'},home:{t:'Home nations',s:'England, Scotland, Wales, NI or UK v the world'},Europe:{t:'Europe'},Asia:{t:'Asia'},Africa:{t:'Africa'},Americas:{t:'Americas & Oceania'}};",
    "const REGIONS={world:{t:'Ganze Welt',s:'Gemischt von allen Kontinenten'},home:{t:'Deutschsprachige Länder',s:'Deutschland, Österreich, die Schweiz und Luxemburg gegen die Welt'},Europe:{t:'Europa'},Asia:{t:'Asien'},Africa:{t:'Afrika'},Americas:{t:'Amerika & Ozeanien'}};")
rep("const LAYOUTS={auto:'Auto',phone:'Phone',tablet:'Tablet',desktop:'Desktop'};","const LAYOUTS={auto:'Auto',phone:'Handy',tablet:'Tablet',desktop:'Computer'};")
# ---- start screen ----
rep('<b>Natural Wonders</b> · Game 8 of 10 · <a href="https://twominute.games/wonders/">All games</a>','<b>Natural Wonders</b> · Spiel 8 von 10 · <a href="https://twominute.games/wonders/">Alle Spiele</a>')
rep('<h1>Where is Bigger?</h1>','<h1>Wo ist es größer?</h1>',3)
rep('Which covers more land? Make all your guesses, then see the real sizes at the end. Prepare to be surprised.','Welches Land ist größer? Erst alle Tipps abgeben, am Ende siehst du die echten Größen. Mach dich auf Überraschungen gefasst.')
rep('<div class="label">Game mode</div>','<div class="label">Spielmodus</div>')
rep('<div class="label">Number of rounds</div>','<div class="label">Anzahl der Runden</div>')
rep('${n} rounds<small>${n*5} answers</small>','${n} Runden<small>${n*5} Antworten</small>')
rep('<div class="label">Number of pairs</div>','<div class="label">Anzahl der Paare</div>')
rep('${n} pairs</button>','${n} Paare</button>')
rep("TM.menuRow('30 seconds a round')","TM.menuRow('30 Sekunden pro Runde')")
rep('<div class="label">Difficulty</div>','<div class="label">Schwierigkeit</div>')
rep('<div class="label">Countries from</div>','<div class="label">Länder aus</div>')
rep("Start — ${S.mode==='bigger'?S.rounds3+' rounds':S.count+' pairs'}","Los geht’s — ${S.mode==='bigger'?S.rounds3+' Runden':S.count+' Paare'}")
rep('<p class="foot">Layout <span class="lay">','<p class="foot">Ansicht <span class="lay">')
rep('${COUNTRIES.length} countries · areas are total area in km² (land plus inland water) · Natural Wonders: Where is Bigger ${VERSION} · <button class="srclink" onclick="openSources()">Sources</button>',
    '${COUNTRIES.length} Länder · Flächen sind Gesamtflächen in km² (Land plus Binnengewässer) · Natural Wonders: Wo ist es größer? ${VERSION} · <button class="srclink" onclick="openSources()">Quellen</button>')
rep("toast('Not enough countries for that combination. Try another region.')","toast('Nicht genug Länder für diese Kombination. Probier eine andere Region.')")
rep("toast('Not enough countries for that combination. Try fewer pairs or another region.')","toast('Nicht genug Länder für diese Kombination. Probier weniger Paare oder eine andere Region.')")
# ---- play ----
rep('aria-label="Pick ${named?esc(c.n):\'country \'+k}"','aria-label="${named?esc(c.n):\'Land \'+k} wählen"')
rep("${side?'→':'←'} key</span>","${side?'→':'←'} Taste</span>")
rep('<button class="link" onclick="back()">← Previous pair</button>','<button class="link" onclick="back()">← Voriges Paar</button>')
rep('<button class="link" onclick="back()">← Previous round</button>','<button class="link" onclick="back()">← Vorige Runde</button>')
rep('<button class="link" onclick="quit()">Quit</button>','<button class="link" onclick="quit()">Beenden</button>',2)
rep('Which is bigger?<span>Pair ${S.cur+1} of ${S.pairs.length}</span>','Welches ist größer?<span>Paar ${S.cur+1} von ${S.pairs.length}</span>')
rep('Shapes are not drawn to scale. Each one is stretched to fill its box.','Die Umrisse sind nicht maßstabsgetreu. Jeder füllt sein Feld aus.')
# ---- results ----
rep("const rtxt=r<1.1?`only ${((r-1)*100).toFixed(1)}% bigger`:`${r.toFixed(r<10?1:0)}× bigger`;","const rtxt=r<1.1?`nur ${dec((r-1)*100,1)} % größer`:`${dec(r,r<10?1:0)}-mal so groß`;")
rep("${i+1}. ${esc(a.n)} v ${esc(b.n)}","${i+1}. ${esc(a.n)} gegen ${esc(b.n)}")
rep("${ok?'✓ You got it':S.picks[i]==null?'⏱ Time ran out':'✗ You picked '+esc(p[S.picks[i]].n)}","${ok?'✓ Richtig':S.picks[i]==null?'⏱ Zeit abgelaufen':'✗ Du hast '+esc(p[S.picks[i]].n)+' gewählt'}")
rep('<span class="tstat">${S.times[i].toFixed(1)} s</span>','<span class="tstat">${dec(S.times[i],1)} s</span>')
rep('<b>${esc(big.n)}</b> is ${rtxt} than <b>${esc(small.n)}</b>','<b>${esc(big.n)}</b> ist ${rtxt}${r<1.1?\' als\':\' wie\'} <b>${esc(small.n)}</b>')
rep("' · capital '+esc(","' · Hauptstadt '+esc(",2)
V=["'Perfect score. Cartographer level.'","'Excellent. You know your maps.'","'Solid effort. A few surprises in there.'","'The map has fooled you a bit.'","'Shapes can be very deceiving!'"]
VD=["'Volle Punktzahl. Kartografen-Niveau.'","'Ausgezeichnet. Du kennst dich mit Karten aus.'","'Ordentlich. Ein paar Überraschungen waren dabei.'","'Die Karte hat dich ein bisschen getäuscht.'","'Umrisse können ganz schön täuschen!'"]
for a,b in zip(V,VD): rep(a,b,2)
rep("😲 <b>Biggest surprise:</b> ${esc(surprise.big.n)} is ${surprise.r.toFixed(1)}× the size of ${esc(surprise.small.n)}.","😲 <b>Größte Überraschung:</b> ${esc(surprise.big.n)} ist ${dec(surprise.r,1)}-mal so groß wie ${esc(surprise.small.n)}.")
rep("🎯 <b>Closest call:</b> ${esc(closest.big.n)} beats ${esc(closest.small.n)} by just ${fmt(closest.big.a-closest.small.a)} km².","🎯 <b>Knappste Entscheidung:</b> ${esc(closest.big.n)} ist nur ${fmt(closest.big.a-closest.small.a)} km² größer als ${esc(closest.small.n)}.")
rep('<h1>Results</h1>','<h1>Ergebnis</h1>',2)
rep('onclick="startGame()">Play again</button>','onclick="startGame()">Nochmal spielen</button>',2)
rep('onclick="quit()">Change settings</button>','onclick="quit()">Einstellungen ändern</button>',2)
rep('>Share score</button>','>Ergebnis teilen</button>',2)
rep('<button class="btn ghost" onclick="openSources()">Sources</button>','<button class="btn ghost" onclick="openSources()">Quellen</button>')
rep('href="https://twominute.games/wonders/">More games</a>','href="https://twominute.games/wonders/">Weitere Spiele</a>')
rep('The answers, drawn to the same scale (bigger country in black)','Die Antworten im gleichen Maßstab (das größere Land in Schwarz)')
rep('aria-label="Both countries drawn to the same scale"','aria-label="Beide Länder im gleichen Maßstab"')
rep('Areas: CIA World Factbook (final edition, total area); England, Scotland, Wales and Northern Ireland: Office for National Statistics. Outlines: Natural Earth. <button class="srclink" onclick="openSources()">See all sources</button>',
    'Flächen: CIA World Factbook (letzte Ausgabe, Gesamtfläche); England, Schottland, Wales und Nordirland: Office for National Statistics. Umrisse: Natural Earth. <button class="srclink" onclick="openSources()">Alle Quellen ansehen</button>',2)
# Which of Five results (not offered in the menu of this game, translated anyway)
rep("'<span class=\"st ok\">✓ Ticked — correct</span>':'<span class=\"st no\">✗ Ticked — but it’s smaller</span>'","'<span class=\"st ok\">✓ Angekreuzt — richtig</span>':'<span class=\"st no\">✗ Angekreuzt — aber es ist kleiner</span>'")
rep("'<span class=\"st ok\">✓ Left blank — correct</span>':'<span class=\"st no\">✗ Missed — it’s bigger</span>'","'<span class=\"st ok\">✓ Frei gelassen — richtig</span>':'<span class=\"st no\">✗ Übersehen — es ist größer</span>'")
rep('<div class="slabel">Round ${ri+1}</div><h3>Bigger than ${esc(t.n)}?</h3>','<div class="slabel">Runde ${ri+1}</div><h3>Größer als ${esc(t.n)}?</h3>')
rep("'Time ran out: your ticks were locked in as they stood':'Answered in '+R.secs.toFixed(1)+' s'","'Zeit abgelaufen: deine Kreuze wurden so übernommen':'Beantwortet in '+dec(R.secs,1)+' s'")
rep('aria-label="All six countries drawn to the same scale"','aria-label="Alle sechs Länder im gleichen Maßstab"');rep('All six drawn to the same scale','Alle sechs im gleichen Maßstab')
rep("😲 <b>Biggest surprise:</b> ${esc(surprise.c.n)} is ${surprise.r>1?multTxt(surprise.r)+' the size of':'only '+multTxt(surprise.r)+' the size of'} ${esc(surprise.t.n)}.","😲 <b>Größte Überraschung:</b> ${esc(surprise.c.n)} ist ${surprise.r>1?multTxt(surprise.r):'nur '+multTxt(surprise.r)} so groß wie ${esc(surprise.t.n)}.")
rep("🎯 <b>Closest call:</b> ${esc(closest.c.n)} is ${multTxt(closest.r)} the size of ${esc(closest.t.n)}, and you still got it right.","🎯 <b>Knappste Entscheidung:</b> ${esc(closest.c.n)} ist ${multTxt(closest.r)} so groß wie ${esc(closest.t.n)}, und du lagst trotzdem richtig.")
rep('${S.game3.length} rounds ·','${S.game3.length} Runden ·')
rep('<div class="label" style="margin-top:28px">Round by round</div>','<div class="label" style="margin-top:28px">Runde für Runde</div>')
rep("' Keys A–E tick, Enter locks in.'","' Tasten A–E kreuzen an, Enter legt fest.'")
rep('>Lock in answer<','>Antwort festlegen<');rep('>Lock in<','>Festlegen<')
rep('>The one to beat<','>Die Marke, die es zu schlagen gilt<',2);rep('>Your answer<','>Deine Antwort<',2)
rep("'None ticked'","'Nichts angekreuzt'")
rep('Round ${S.cur+1} of ','Runde ${S.cur+1} von ',2)
rep('Tick all that apply. It could be none, it could be all five.','Kreuze alle passenden an. Es können keine sein, es können alle fünf sein.')
rep('Which are bigger than <em>','Welche sind größer als <em>');rep('Which of these are bigger than <em>','Welche davon sind größer als <em>')
# ---- share ----
rep("const t=`Natural Wonders: Where is Bigger. I scored ${r}/${n} (${S.mode==='bigger'?'Bigger than…, ':''}${DIFFS[S.diff].t}, ${REGIONS[S.region].t}). Can you beat me?`;",
    "const t=`Natural Wonders: Wo ist es größer? Ich habe ${r}/${n} geschafft (${S.mode==='bigger'?'Größer als…, ':''}${DIFFS[S.diff].t}, ${REGIONS[S.region].t}). Schaffst du mehr?`;")
rep("toast('Score copied. Paste it to a friend.')","toast('Ergebnis kopiert. Schick es an Freunde.')")
# ---- sources ----
rep('aria-label="Sources"><button class="srcx" onclick="closeSources()">Close</button>','aria-label="Quellen"><button class="srcx" onclick="closeSources()">Schließen</button>')
rep("COUNTRIES.slice().sort((a,b)=>a.n.localeCompare(b.n))","COUNTRIES.slice().sort((a,b)=>a.n.localeCompare(b.n,'de'))")
rep('<h2>Sources</h2>','<h2>Quellen</h2>')
src_start=s.index('<p class="gf">'); src_end=s.index('<h3>Every country and its area</h3>')
block=s[src_start:src_end]
SRC=[('The figures in this game were taken in good faith from the published sources below in October 2026 and are shown exactly as those sources give them. Different reputable sources measure areas in slightly different ways (for example whether lakes, rivers and coastal waters are included), so you may find other figures elsewhere, and a source can occasionally be wrong. If you think a figure is wrong, this is where it came from.',
      'Die Zahlen in diesem Spiel stammen nach bestem Wissen aus den unten genannten Quellen (Stand Oktober 2026) und werden genau so gezeigt, wie die Quellen sie angeben. Seriöse Quellen messen Flächen leicht unterschiedlich (zum Beispiel mit oder ohne Seen, Flüsse und Küstengewässer), daher findest du anderswo womöglich andere Zahlen, und auch eine Quelle kann einmal falsch liegen. Wenn du eine Zahl für falsch hältst, siehst du hier, woher sie stammt.'),
     ('<h3>Country areas</h3>','<h3>Landesflächen</h3>'),
     (', total area (land plus inland water), from its final edition. The CIA stopped publishing the Factbook in February 2026; its data is preserved in the public',', Gesamtfläche (Land plus Binnengewässer), aus der letzten Ausgabe. Die CIA hat das Factbook im Februar 2026 eingestellt; die Daten sind im öffentlichen'),
     ('factbook.json archive</a>','factbook.json-Archiv</a> erhalten'),
     ("France uses the Factbook's figure for metropolitan France (551,500 km²), to match the outline shown, which leaves out overseas regions such as French Guiana.","Für Frankreich gilt die Factbook-Zahl für das europäische Frankreich (551.500 km²), passend zum gezeigten Umriss ohne Überseegebiete wie Französisch-Guayana."),
     ("Morocco is not included: the Factbook's figure includes the disputed territory of Western Sahara, so the figure and the outline would not match.","Marokko ist nicht dabei: Die Factbook-Zahl schließt das umstrittene Gebiet Westsahara ein, Zahl und Umriss würden also nicht zusammenpassen."),
     ('<h3>England, Scotland, Wales and Northern Ireland</h3>','<h3>England, Schottland, Wales und Nordirland</h3>'),
     (', Standard Area Measurements, as given on',', Standard Area Measurements, wie angegeben auf'),
     (': England 130,462 km², Scotland 78,803 km², Wales 20,782 km², Northern Ireland 14,333 km². “Waleses” use Wales at 20,782 km².',': England 130.462 km², Schottland 78.803 km², Wales 20.782 km², Nordirland 14.333 km².</li><li>Vergleiche mit dem Saarland nutzen 2.570 km² (Statistisches Amt Saarland).'),
     ('<h3>Capitals</h3>','<h3>Hauptstädte</h3>'),
     ('The open “world-countries” dataset by Mohammed Le Doze (','Der offene Datensatz „world-countries“ von Mohammed Le Doze ('),
     ('<h3>Maps</h3>','<h3>Karten</h3>'),('Country outlines:','Länderumrisse:'),
     (' (1:10m, public domain). Remote overseas territories are left off the outlines.',' (1:10m, gemeinfrei). Entlegene Überseegebiete fehlen in den Umrissen.')]
for a,b in SRC:
    if block.count(a)!=1: sys.exit('build_de: sources text changed: '+a[:60])
    block=block.replace(a,b)
block=re.sub(r'\. See (<a [^>]*>)',r'. Siehe \1',block)
s=s[:src_start]+block+s[src_end:]
rep('<h3>Every country and its area</h3><details><summary>${COUNTRIES.length} countries</summary>','<h3>Alle Länder und ihre Fläche</h3><details><summary>${COUNTRIES.length} Länder</summary>')
# ---- game switcher strip and "Try next" ----
rep("setAttribute('aria-label','Switch game')","setAttribute('aria-label','Spiel wechseln')")
rep('<a class="home" href="/wonders/">← All games</a>','<a class="home" href="/wonders/">← Alle Spiele</a>')
rep("{n:'Where is Bigger?',slug:'where-is-bigger',ic:'bigger',t:'Two countries side by side. Which covers more land? Maps have been fooling you for years.'}","{n:'Wo ist es größer?',slug:'where-is-bigger',ic:'bigger',t:'Zwei Länder nebeneinander. Welches ist größer? Karten täuschen dich seit Jahren.'}")
rep('/^Play again$/','/^Nochmal spielen$/')
rep("Try next${rec.games[n.slug]?' · your lowest score':' · not played yet'}","Als Nächstes${rec.games[n.slug]?' · dein schwächstes Ergebnis':' · noch nicht gespielt'} · auf Englisch")
rep('<span class="go">Play →</span>','<span class="go">Spielen →</span>')
rep('<b>${done} of ${GAMES.length}</b>','<b>${done} von ${GAMES.length}</b>')
rep('</b> Natural Wonders explored</span><a href="/wonders/#record">Your record →</a>','</b> Natural Wonders entdeckt</span><a href="/wonders/#record">Deine Bestwerte →</a>')
# ---- feedback box ----
FB=[("[['idea','💡 Idea','What would make it better?'],['like','👍 Like it','What did you enjoy?'],['wrong','🐞 Something’s wrong','What went wrong, and where?']]","[['idea','💡 Idee','Was würde es besser machen?'],['like','👍 Gefällt mir','Was hat dir gefallen?'],['wrong','🐞 Etwas stimmt nicht','Was ist schiefgegangen, und wo?']]"),
    ('aria-label="Feedback or report a problem"><h2>Tell us what you think</h2>','aria-label="Feedback oder Fehler melden"><h2>Sag uns deine Meinung</h2>'),
    ('Ideas, likes, gripes or something broken. It goes privately to Two Minute Games; nobody else can read it.','Ideen, Lob, Kritik oder etwas kaputt? Die Nachricht geht privat an Two Minute Games, niemand sonst kann sie lesen.'),
    ('aria-label="Your message"','aria-label="Deine Nachricht"'),
    ('placeholder="Name or email, only if you’d like a reply (optional)" aria-label="Name or email (optional)"','placeholder="Name oder E-Mail, nur wenn du eine Antwort möchtest (freiwillig)" aria-label="Name oder E-Mail (freiwillig)"'),
    ('We also send which game you were on and your type of device, nothing else.','Wir senden außerdem, in welchem Spiel du warst und welches Gerät du nutzt, sonst nichts.'),
    ('<button type="button" class="tmgfb-b">Cancel</button><button type="submit" class="tmgfb-b go">Send</button>','<button type="button" class="tmgfb-b">Abbrechen</button><button type="submit" class="tmgfb-b go">Senden</button>'),
    ("m.textContent='Sending…'","m.textContent='Wird gesendet…'"),("m.textContent='Thank you. Sent!'","m.textContent='Danke. Gesendet!'"),
    ("m.textContent='Couldn’t send just now. Please try again in a moment.'","m.textContent='Konnte gerade nicht senden. Bitte versuch es gleich noch einmal.'"),
    ("p.setAttribute('aria-label','Feedback or report a problem');p.innerHTML=ICON+'Feedback or bug'","p.setAttribute('aria-label','Feedback oder Fehler melden');p.innerHTML=ICON+'Feedback oder Fehler'")]
for a,b in FB: rep(a,b)
# ---- banner: this file is generated ----
# open on the home region the first time, remembered per language afterwards
rep("localStorage.getItem('wib_settings')","localStorage.getItem('wib_settings_de')")
rep("localStorage.setItem('wib_settings',","localStorage.setItem('wib_settings_de',")
rep("region:'world',layout","region:'home',layout")
s=s.replace('<!doctype html>','<!doctype html>\n<!-- GENERATED by tools/build_de.py from ../index.html. Edit the English page, then run the build again. -->',1)
os.makedirs(os.path.join(ROOT,'de'),exist_ok=True)
open(os.path.join(ROOT,'de','index.html'),'w',encoding='utf-8').write(s)
# report English words left in visible-looking strings, for a human check
left=sorted(set(re.findall(r"(?:>|')([A-Z][a-z]+(?: [a-z]+){2,}[.?!]?)(?:<|')",s)))
print(f'build_de: {n_done} replacements, {k} names. Possible English left:',left[:40])
