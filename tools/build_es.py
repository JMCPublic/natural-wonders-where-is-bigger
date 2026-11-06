#!/usr/bin/env python3
"""Spanish page es/index.html. Run from the repo folder: python3 tools/build_es.py
Numbers use a decimal point and thin-space thousands so they read the same in Spain and Latin America."""
import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));import langkit
S="""AFG=Afganistán;ALB=Albania;DZA=Argelia;AGO=Angola;ARG=Argentina;ARM=Armenia;AUS=Australia;AUT=Austria;AZE=Azerbaiyán;BGD=Bangladés;BLR=Bielorrusia;BEL=Bélgica;BLZ=Belice;BEN=Benín;BTN=Bután;BOL=Bolivia;BIH=Bosnia y Herzegovina;BWA=Botsuana;BRA=Brasil;BRN=Brunéi;BGR=Bulgaria;BFA=Burkina Faso;BDI=Burundi;KHM=Camboya;CMR=Camerún;CAN=Canadá;CAF=República Centroafricana;TCD=Chad;CHL=Chile;CHN=China;COL=Colombia;CRI=Costa Rica;CIV=Costa de Marfil;HRV=Croacia;CUB=Cuba;CYP=Chipre;CZE=Chequia;DNK=Dinamarca;DJI=Yibuti;DOM=República Dominicana;COD=RD del Congo;ECU=Ecuador;EGY=Egipto;SLV=El Salvador;ENG=Inglaterra;GNQ=Guinea Ecuatorial;ERI=Eritrea;EST=Estonia;SWZ=Esuatini;ETH=Etiopía;FIN=Finlandia;FRA=Francia;GAB=Gabón;GMB=Gambia;GEO=Georgia;DEU=Alemania;GHA=Ghana;GRC=Grecia;GTM=Guatemala;GIN=Guinea;GNB=Guinea-Bisáu;GUY=Guyana;HTI=Haití;HND=Honduras;HUN=Hungría;ISL=Islandia;IND=India;IDN=Indonesia;IRN=Irán;IRQ=Irak;IRL=Irlanda;ISR=Israel;ITA=Italia;JAM=Jamaica;JPN=Japón;JOR=Jordania;KAZ=Kazajistán;KEN=Kenia;KWT=Kuwait;KGZ=Kirguistán;LAO=Laos;LVA=Letonia;LBN=Líbano;LSO=Lesoto;LBR=Liberia;LBY=Libia;LTU=Lituania;LUX=Luxemburgo;MDG=Madagascar;MWI=Malaui;MYS=Malasia;MLI=Malí;MLT=Malta;MRT=Mauritania;MEX=México;MDA=Moldavia;MNG=Mongolia;MNE=Montenegro;MOZ=Mozambique;MMR=Myanmar;NAM=Namibia;NPL=Nepal;NLD=Países Bajos;NZL=Nueva Zelanda;NIC=Nicaragua;NER=Níger;NGA=Nigeria;PRK=Corea del Norte;MKD=Macedonia del Norte;NIR=Irlanda del Norte;NOR=Noruega;OMN=Omán;PAK=Pakistán;PAN=Panamá;PNG=Papúa Nueva Guinea;PRY=Paraguay;PER=Perú;PHL=Filipinas;POL=Polonia;PRT=Portugal;QAT=Catar;COG=República del Congo;ROU=Rumania;RUS=Rusia;RWA=Ruanda;WSM=Samoa;SAU=Arabia Saudita;SCT=Escocia;SEN=Senegal;SRB=Serbia;SLE=Sierra Leona;SVK=Eslovaquia;SVN=Eslovenia;SOM=Somalia;ZAF=Sudáfrica;KOR=Corea del Sur;SSD=Sudán del Sur;ESP=España;LKA=Sri Lanka;SDN=Sudán;SUR=Surinam;SWE=Suecia;CHE=Suiza;SYR=Siria;TJK=Tayikistán;TZA=Tanzania;THA=Tailandia;TLS=Timor Oriental;TGO=Togo;TTO=Trinidad y Tobago;TUN=Túnez;TUR=Turquía;TKM=Turkmenistán;ARE=Emiratos Árabes Unidos;UGA=Uganda;UKR=Ucrania;GBR=Reino Unido;USA=Estados Unidos;URY=Uruguay;UZB=Uzbekistán;VEN=Venezuela;VNM=Vietnam;WLS=Gales;YEM=Yemen;ZMB=Zambia;ZWE=Zimbabue"""
NAMES=dict(x.split('=',1) for x in S.split(';'))
CAPS={"Algiers":"Argel","Yerevan":"Ereván","Vienna":"Viena","Baku":"Bakú","Dhaka":"Daca","Brussels":"Bruselas","Beijing":"Pekín","Havana":"La Habana","Prague":"Praga","Copenhagen":"Copenhague","Djibouti":"Yibuti","Kinshasa":"Kinsasa","Cairo":"El Cairo","London":"Londres","Tbilisi":"Tiflis","Accra":"Acra","Athens":"Atenas","Guatemala City":"Ciudad de Guatemala","New Delhi":"Nueva Delhi","Jakarta":"Yakarta","Tehran":"Teherán","Jerusalem":"Jerusalén","Rome":"Roma","Kuwait City":"Ciudad de Kuwait","Bishkek":"Biskek","Tripoli":"Trípoli","Luxembourg":"Luxemburgo","Mexico City":"Ciudad de México","Chișinău":"Chisináu","Ulan Bator":"Ulán Bator","Kathmandu":"Katmandú","Skopje":"Skopie","Muscat":"Mascate","Panama City":"Ciudad de Panamá","Warsaw":"Varsovia","Lisbon":"Lisboa","Bucharest":"Bucarest","Moscow":"Moscú","Riyadh":"Riad","Edinburgh":"Edimburgo","Belgrade":"Belgrado","Mogadishu":"Mogadiscio","Seoul":"Seúl","Khartoum":"Jartum","Stockholm":"Estocolmo","Bern":"Berna","Damascus":"Damasco","Dushanbe":"Dusambé","Tunis":"Túnez","Ashgabat":"Asjabad","Abu Dhabi":"Abu Dabi","Washington D.C.":"Washington D. C.","Tashkent":"Taskent","Hanoi":"Hanói","Sana'a":"Saná","Tokyo":"Tokio","Addis Ababa":"Adís Abeba","Pyongyang":"Pionyang","Ljubljana":"Liubliana","Valletta":"La Valeta","Reykjavik":"Reikiavik","Vilnius":"Vilna","Port-au-Prince":"Puerto Príncipe","Port Moresby":"Puerto Moresby","Port of Spain":"Puerto España","Phnom Penh":"Nom Pen","Vientiane":"Vientián","Thimphu":"Timbu","Astana":"Astaná","Dublin":"Dublín","Paris":"París","Tallinn":"Tallin","Amman":"Amán","Yaoundé":"Yaundé","N'Djamena":"Yamena","Ouagadougou":"Uagadugú","Yamoussoukro":"Yamusukro","Lilongwe":"Lilongüe","Singapore":"Singapur","Cape Town":"Ciudad del Cabo","Kyiv":"Kiev"}
HOME=['ESP','MEX','COL','ARG','PER','VEN','CHL','ECU','GTM','CUB','BOL','DOM','HND','PRY','SLV','NIC','CRI','PAN','URY','GNQ']
T=['${right}/${total} en ${this.fmt(secs)}',
"const WALES=20782;\nconst HOME=new Set("+json.dumps(HOME)+");const UNIT=21041; /* El Salvador, CIA World Factbook */",
'COUNTRIES.filter(c=>HOME.has(c.id))','COUNTRIES.filter(c=>!HOME.has(c.id))',
"const rtxt=r<1.1?`solo un ${dec((r-1)*100,1)} % más grande`:`${dec(r,r<10?1:0)} veces más grande`;",
'${i+1}. ${esc(a.n)} – ${esc(b.n)}',
'😲 <b>La mayor sorpresa:</b> ${esc(surprise.big.n)} es ${dec(surprise.r,1)} veces más grande que ${esc(surprise.small.n)}.',
'🎯 <b>Por los pelos:</b> ${esc(closest.big.n)} supera a ${esc(closest.small.n)} por solo ${fmt(closest.big.a-closest.small.a)} km².',
"'<span class=\"st ok\">✓ Marcado — correcto</span>':'<span class=\"st no\">✗ Marcado — pero es más pequeño</span>'",
"'<span class=\"st ok\">✓ En blanco — correcto</span>':'<span class=\"st no\">✗ Se te pasó — es más grande</span>'",
'🎯 <b>Por los pelos:</b> ${esc(closest.c.n)} mide ${multTxt(closest.r)} el tamaño de ${esc(closest.t.n)}, y aun así acertaste.',
"COUNTRIES.slice().sort((a,b)=>a.n.localeCompare(b.n,'es'))",
'<html lang="es">','<title>Natural Wonders · ¿Cuál es más grande?</title>',
"'Tiempo restante para esta pregunta'",
"`${s} segundo${s===1?'':'s'}`:`${Math.floor(s/60)} min ${s%60} s`",
"`saliste de la página ${this.left} ${this.left===1?'vez':'veces'}`:'te quedaste en la página todo el rato'",
'<div class="label">Tiempo</div>','⏱ Con tiempo<small>','Sin tiempo<small>Tómate tu tiempo</small>',
"const fmt=n=>n.toLocaleString('en-US').replace(/,/g,'\\u202f');const dec=(x,d)=>x.toFixed(d);",
"function wales(a){const w=a/UNIT;if(Math.abs(w-1)<.005)return 'exactamente 1 El Salvador';if(w>=100)return '≈ '+fmt(Math.round(w))+' veces El Salvador';if(w>=1)return '≈ '+dec(w,1)+' veces El Salvador';return '≈ '+dec(w,w<.1?2:1)+' de El Salvador'}",
"function multTxt(r){return r>=10?Math.round(r)+'×':r>=.1?dec(r,1)+'×':r>=.01?dec(r,2)+'×':dec(r,3)+'×'}",
'aria-label="Silueta del país"',
"const MODES={names:{t:'Modo 1 — Silueta + nombre',s:'Ver la forma y el nombre'},hidden:{t:'Modo 2 — Solo silueta',s:'Solo la forma. Los nombres se revelan al final'}};",
"const DIFFS3T={easy:{t:'Fácil',s:'Gigantes y enanos'},medium:{t:'Medio',s:'De 1.3 a 3 veces el objetivo'},hard:{t:'Difícil',s:'Cerca del tamaño del objetivo'}};",
"const DIFFS={easy:{t:'Fácil',s:'De 2 a 8 veces más grande',lo:2,hi:8},medium:{t:'Medio',s:'De 1.3 a 2.2 veces más grande',lo:1.3,hi:2.2},hard:{t:'Difícil',s:'Menos de un 35 % de diferencia',lo:1.03,hi:1.35}};",
"const REGIONS={world:{t:'Todo el mundo',s:'Mezcla de todos los continentes'},home:{t:'Países hispanohablantes',s:'El mundo hispano contra el resto del mundo'},Europe:{t:'Europa'},Asia:{t:'Asia'},Africa:{t:'África'},Americas:{t:'América y Oceanía'}};",
"const LAYOUTS={auto:'Auto',phone:'Teléfono',tablet:'Tableta',desktop:'Escritorio'};",
'<b>Natural Wonders</b> · Juego 8 de 10 · <a href="https://twominute.games/wonders/">Todos los juegos</a>',
'<h1>¿Cuál es más grande?</h1>',
'¿Cuál ocupa más territorio? Haz todas tus apuestas y descubre los tamaños reales al final. Prepárate para sorprenderte.',
'<div class="label">Modo de juego</div>','<div class="label">Número de rondas</div>','<div class="label">Número de parejas</div>',
'${n} rondas<small>${n*5} respuestas</small>','${n} parejas</button>',"TM.menuRow('30 segundos por ronda')",
'<div class="label">Dificultad</div>','<div class="label">Países</div>',
"¡A jugar! — ${S.mode==='bigger'?S.rounds3+' rondas':S.count+' parejas'}",
'<p class="foot">Vista <span class="lay">',
'${COUNTRIES.length} países · superficie total en km² (tierra y aguas interiores) · Natural Wonders: ¿Cuál es más grande? ${VERSION} · <button class="srclink" onclick="openSources()">Fuentes</button>',
"toast('No hay suficientes países para esa combinación. Prueba otra región.')",
"toast('No hay suficientes países para esa combinación. Prueba con menos parejas u otra región.')",
'aria-label="Elegir ${named?esc(c.n):\'el país \'+k}"',
"${side?'→':'←'} tecla</span>",
'<button class="link" onclick="back()">← Pareja anterior</button>','<button class="link" onclick="back()">← Ronda anterior</button>',
'<button class="link" onclick="quit()">Salir</button>',
'¿Cuál es más grande?<span>Pareja ${S.cur+1} de ${S.pairs.length}</span>',
'Las formas no están a escala. Cada una se amplía para llenar su recuadro.',
"${ok?'✓ Acertaste':S.picks[i]==null?'⏱ Se acabó el tiempo':'✗ Elegiste '+esc(p[S.picks[i]].n)}",
'<span class="tstat">${dec(S.times[i],1)} s</span>',
'<b>${esc(big.n)}</b> es ${rtxt} que <b>${esc(small.n)}</b>',
"' · capital '+esc(",
'😲 <b>La mayor sorpresa:</b> ${esc(surprise.c.n)} mide ${surprise.r>1?\'\':\'solo \'}${multTxt(surprise.r)} el tamaño de ${esc(surprise.t.n)}.',
'<h1>Resultados</h1>','onclick="startGame()">Jugar otra vez</button>','onclick="quit()">Cambiar ajustes</button>','>Compartir puntuación</button>',
'<button class="btn ghost" onclick="openSources()">Fuentes</button>','href="https://twominute.games/wonders/">Más juegos</a>',
'Las respuestas a la misma escala (el país más grande en negro)','aria-label="Los dos países a la misma escala"',
'Superficies: CIA World Factbook (última edición, superficie total); Inglaterra, Escocia, Gales e Irlanda del Norte: Office for National Statistics. Contornos: Natural Earth. <button class="srclink" onclick="openSources()">Ver todas las fuentes</button>',
'<div class="slabel">Ronda ${ri+1}</div><h3>¿Más grande que ${esc(t.n)}?</h3>',
"'Se acabó el tiempo: tus marcas se guardaron tal cual':'Respondido en '+dec(R.secs,1)+' s'",
'aria-label="Los seis países a la misma escala"','Los seis a la misma escala',
'${S.game3.length} rondas ·','<div class="label" style="margin-top:28px">Ronda a ronda</div>',
"' Teclas A–E para marcar, Intro para confirmar.'",'>Confirmar respuesta<','>Confirmar<','>El país a superar<','>Tu respuesta<',"'Nada marcado'",
'Ronda ${S.cur+1} de ','Marca todos los que correspondan. Puede que ninguno, puede que los cinco.',
'¿Cuáles son más grandes que <em>','¿Cuáles de estos son más grandes que <em>',
"const t=`Natural Wonders: ¿Cuál es más grande? Saqué ${r}/${n} (${S.mode==='bigger'?'Más grande que…, ':''}${DIFFS[S.diff].t}, ${REGIONS[S.region].t}). ¿Puedes superarme?`;",
"toast('Puntuación copiada. Pásasela a un amigo.')",
'aria-label="Fuentes"><button class="srcx" onclick="closeSources()">Cerrar</button>','<h2>Fuentes</h2>',
'<h3>Todos los países y su superficie</h3><details><summary>${COUNTRIES.length} países</summary>',
"setAttribute('aria-label','Cambiar de juego')",'<a class="home" href="/wonders/">← Todos los juegos</a>',
"{n:'¿Cuál es más grande?',slug:'where-is-bigger',ic:'bigger',t:'Dos países lado a lado. ¿Cuál ocupa más territorio? Los mapas llevan años engañándote.'}",
'/^Jugar otra vez$/',"Prueba ahora${rec.games[n.slug]?' · tu puntuación más baja':' · aún sin jugar'} · en inglés",
'<span class="go">Jugar →</span>','<b>${done} de ${GAMES.length}</b>',
'</b> Natural Wonders explorados</span><a href="/wonders/#record">Tus récords →</a>']
V=["'¡Puntuación perfecta! Nivel cartógrafo.'","'Excelente. Conoces bien los mapas.'","'Buen intento. Hubo algunas sorpresas.'","'El mapa te ha engañado un poco.'","'¡Las formas engañan mucho!'"]
SRC=['Las cifras de este juego se tomaron de buena fe de las fuentes publicadas que aparecen abajo, en octubre de 2026, y se muestran tal como las dan esas fuentes. Distintas fuentes fiables miden la superficie de formas algo diferentes (por ejemplo, si incluyen o no lagos, ríos y aguas costeras), así que puede que encuentres otras cifras en otros sitios, y alguna fuente puede equivocarse. Si crees que una cifra está mal, aquí ves de dónde salió.',
'<h3>Superficie de los países</h3>',', superficie total (tierra y aguas interiores), de su última edición. La CIA dejó de publicar el Factbook en febrero de 2026; sus datos se conservan en el archivo público',
'factbook.json</a>',
'Para Francia se usa la cifra del Factbook de la Francia metropolitana (551 500 km²), para que coincida con el contorno, que no incluye regiones de ultramar como la Guayana Francesa.',
'Marruecos no está incluido: la cifra del Factbook incluye el territorio en disputa del Sáhara Occidental, así que la cifra y el contorno no coincidirían.',
'<h3>Inglaterra, Escocia, Gales e Irlanda del Norte</h3>',', Standard Area Measurements, según',
': Inglaterra 130 462 km², Escocia 78 803 km², Gales 20 782 km², Irlanda del Norte 14 333 km².</li><li>Las comparaciones con El Salvador usan 21 041 km² (CIA World Factbook).',
'<h3>Capitales</h3>','El conjunto de datos abierto «world-countries» de Mohammed Le Doze (',
'<h3>Mapas</h3>','Contornos de los países:',' (1:10m, dominio público). Los territorios de ultramar lejanos no aparecen en los contornos.']
FB=["[['idea','💡 Idea','¿Qué lo haría mejor?'],['like','👍 Me gusta','¿Qué te ha gustado?'],['wrong','🐞 Algo falla','¿Qué ha fallado y dónde?']]",
'aria-label="Opinión o informar de un problema"><h2>Cuéntanos qué te parece</h2>',
'Ideas, cosas que te gustan, quejas o algo roto. Llega en privado a Two Minute Games; nadie más puede leerlo.',
'aria-label="Tu mensaje"',
'placeholder="Nombre o correo, solo si quieres respuesta (opcional)" aria-label="Nombre o correo (opcional)"',
'También enviamos en qué juego estabas y tu tipo de dispositivo, nada más.',
'<button type="button" class="tmgfb-b">Cancelar</button><button type="submit" class="tmgfb-b go">Enviar</button>',
"m.textContent='Enviando…'","m.textContent='¡Gracias! Enviado.'","m.textContent='No se pudo enviar ahora. Inténtalo de nuevo en un momento.'",
"p.setAttribute('aria-label','Opinión o informar de un problema');p.innerHTML=ICON+'Opinión o error'"]
HEAD='''<meta name="description" content="¿Qué país es más grande? Dos minutos, gratis, sin registrarte.">
<meta property="og:title" content="¿Cuál es más grande? · Natural Wonders">
<meta property="og:description" content="¿Qué país es más grande? Dos minutos, gratis, sin registrarte.">
<meta property="og:image" content="https://twominute.games/es/card-v1.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="https://twominute.games/natural-wonders-where-is-bigger/es/">
<meta property="og:locale" content="es_ES"><meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="en" href="https://twominute.games/natural-wonders-where-is-bigger/">
<link rel="alternate" hreflang="es" href="https://twominute.games/natural-wonders-where-is-bigger/es/">'''
langkit.build(dict(code='es',names=NAMES,caps=CAPS,T=T,V=V,SRC=SRC,FB=FB,head=HEAD,see='Ver también',sources_end='<h3>Todos los países y su superficie</h3>'))
