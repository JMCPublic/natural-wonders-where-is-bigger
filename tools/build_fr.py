#!/usr/bin/env python3
"""French page fr/index.html. Run from the repo folder: python3 tools/build_fr.py"""
import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));import langkit
NB=' '
F="""AFG=Afghanistan|l'Afghanistan;ALB=Albanie|l'Albanie;DZA=Algérie|l'Algérie;AGO=Angola|l'Angola;ARG=Argentine|l'Argentine;ARM=Arménie|l'Arménie;AUS=Australie|l'Australie;AUT=Autriche|l'Autriche;AZE=Azerbaïdjan|l'Azerbaïdjan;BGD=Bangladesh|le Bangladesh;BLR=Biélorussie|la Biélorussie;BEL=Belgique|la Belgique;BLZ=Belize|le Belize;BEN=Bénin|le Bénin;BTN=Bhoutan|le Bhoutan;BOL=Bolivie|la Bolivie;BIH=Bosnie-Herzégovine|la Bosnie-Herzégovine;BWA=Botswana|le Botswana;BRA=Brésil|le Brésil;BRN=Brunei|le Brunei;BGR=Bulgarie|la Bulgarie;BFA=Burkina Faso|le Burkina Faso;BDI=Burundi|le Burundi;KHM=Cambodge|le Cambodge;CMR=Cameroun|le Cameroun;CAN=Canada|le Canada;CAF=Centrafrique|la Centrafrique;TCD=Tchad|le Tchad;CHL=Chili|le Chili;CHN=Chine|la Chine;COL=Colombie|la Colombie;CRI=Costa Rica|le Costa Rica;CIV=Côte d'Ivoire|la Côte d'Ivoire;HRV=Croatie|la Croatie;CUB=Cuba|Cuba;CYP=Chypre|Chypre;CZE=Tchéquie|la Tchéquie;DNK=Danemark|le Danemark;DJI=Djibouti|Djibouti;DOM=République dominicaine|la République dominicaine;COD=RD Congo|la RD Congo;ECU=Équateur|l'Équateur;EGY=Égypte|l'Égypte;SLV=Salvador|le Salvador;ENG=Angleterre|l'Angleterre;GNQ=Guinée équatoriale|la Guinée équatoriale;ERI=Érythrée|l'Érythrée;EST=Estonie|l'Estonie;SWZ=Eswatini|l'Eswatini;ETH=Éthiopie|l'Éthiopie;FIN=Finlande|la Finlande;FRA=France|la France;GAB=Gabon|le Gabon;GMB=Gambie|la Gambie;GEO=Géorgie|la Géorgie;DEU=Allemagne|l'Allemagne;GHA=Ghana|le Ghana;GRC=Grèce|la Grèce;GTM=Guatemala|le Guatemala;GIN=Guinée|la Guinée;GNB=Guinée-Bissau|la Guinée-Bissau;GUY=Guyana|le Guyana;HTI=Haïti|Haïti;HND=Honduras|le Honduras;HUN=Hongrie|la Hongrie;ISL=Islande|l'Islande;IND=Inde|l'Inde;IDN=Indonésie|l'Indonésie;IRN=Iran|l'Iran;IRQ=Irak|l'Irak;IRL=Irlande|l'Irlande;ISR=Israël|Israël;ITA=Italie|l'Italie;JAM=Jamaïque|la Jamaïque;JPN=Japon|le Japon;JOR=Jordanie|la Jordanie;KAZ=Kazakhstan|le Kazakhstan;KEN=Kenya|le Kenya;KWT=Koweït|le Koweït;KGZ=Kirghizistan|le Kirghizistan;LAO=Laos|le Laos;LVA=Lettonie|la Lettonie;LBN=Liban|le Liban;LSO=Lesotho|le Lesotho;LBR=Liberia|le Liberia;LBY=Libye|la Libye;LTU=Lituanie|la Lituanie;LUX=Luxembourg|le Luxembourg;MDG=Madagascar|Madagascar;MWI=Malawi|le Malawi;MYS=Malaisie|la Malaisie;MLI=Mali|le Mali;MLT=Malte|Malte;MRT=Mauritanie|la Mauritanie;MEX=Mexique|le Mexique;MDA=Moldavie|la Moldavie;MNG=Mongolie|la Mongolie;MNE=Monténégro|le Monténégro;MOZ=Mozambique|le Mozambique;MMR=Myanmar|le Myanmar;NAM=Namibie|la Namibie;NPL=Népal|le Népal;NLD=Pays-Bas|les Pays-Bas;NZL=Nouvelle-Zélande|la Nouvelle-Zélande;NIC=Nicaragua|le Nicaragua;NER=Niger|le Niger;NGA=Nigeria|le Nigeria;PRK=Corée du Nord|la Corée du Nord;MKD=Macédoine du Nord|la Macédoine du Nord;NIR=Irlande du Nord|l'Irlande du Nord;NOR=Norvège|la Norvège;OMN=Oman|Oman;PAK=Pakistan|le Pakistan;PAN=Panama|le Panama;PNG=Papouasie-Nouvelle-Guinée|la Papouasie-Nouvelle-Guinée;PRY=Paraguay|le Paraguay;PER=Pérou|le Pérou;PHL=Philippines|les Philippines;POL=Pologne|la Pologne;PRT=Portugal|le Portugal;QAT=Qatar|le Qatar;COG=Congo|le Congo;ROU=Roumanie|la Roumanie;RUS=Russie|la Russie;RWA=Rwanda|le Rwanda;WSM=Samoa|les Samoa;SAU=Arabie saoudite|l'Arabie saoudite;SCT=Écosse|l'Écosse;SEN=Sénégal|le Sénégal;SRB=Serbie|la Serbie;SLE=Sierra Leone|la Sierra Leone;SVK=Slovaquie|la Slovaquie;SVN=Slovénie|la Slovénie;SOM=Somalie|la Somalie;ZAF=Afrique du Sud|l'Afrique du Sud;KOR=Corée du Sud|la Corée du Sud;SSD=Soudan du Sud|le Soudan du Sud;ESP=Espagne|l'Espagne;LKA=Sri Lanka|le Sri Lanka;SDN=Soudan|le Soudan;SUR=Suriname|le Suriname;SWE=Suède|la Suède;CHE=Suisse|la Suisse;SYR=Syrie|la Syrie;TJK=Tadjikistan|le Tadjikistan;TZA=Tanzanie|la Tanzanie;THA=Thaïlande|la Thaïlande;TLS=Timor oriental|le Timor oriental;TGO=Togo|le Togo;TTO=Trinité-et-Tobago|Trinité-et-Tobago;TUN=Tunisie|la Tunisie;TUR=Turquie|la Turquie;TKM=Turkménistan|le Turkménistan;ARE=Émirats arabes unis|les Émirats arabes unis;UGA=Ouganda|l'Ouganda;UKR=Ukraine|l'Ukraine;GBR=Royaume-Uni|le Royaume-Uni;USA=États-Unis|les États-Unis;URY=Uruguay|l'Uruguay;UZB=Ouzbékistan|l'Ouzbékistan;VEN=Venezuela|le Venezuela;VNM=Viêt Nam|le Viêt Nam;WLS=Pays de Galles|le pays de Galles;YEM=Yémen|le Yémen;ZMB=Zambie|la Zambie;ZWE=Zimbabwe|le Zimbabwe"""
P=[x.split('=',1) for x in F.split(';')]
NAMES={k:v.split('|')[0] for k,v in P}; ART={k:v.split('|')[1] for k,v in P}
CAPS={"Kabul":"Kaboul","Algiers":"Alger","Yerevan":"Erevan","Vienna":"Vienne","Baku":"Bakou","Dhaka":"Dacca","Brussels":"Bruxelles","Beijing":"Pékin","Havana":"La Havane","Nicosia":"Nicosie","Copenhagen":"Copenhague","Cairo":"Le Caire","London":"Londres","Tbilisi":"Tbilissi","Athens":"Athènes","Guatemala City":"Guatemala","Tehran":"Téhéran","Baghdad":"Bagdad","Jerusalem":"Jérusalem","Kuwait City":"Koweït","Beirut":"Beyrouth","Mexico City":"Mexico","Ulan Bator":"Oulan-Bator","Kathmandu":"Katmandou","Muscat":"Mascate","Panama City":"Panama","Warsaw":"Varsovie","Lisbon":"Lisbonne","Bucharest":"Bucarest","Moscow":"Moscou","Riyadh":"Riyad","Edinburgh":"Édimbourg","Mogadishu":"Mogadiscio","Seoul":"Séoul","Bern":"Berne","Damascus":"Damas","Dushanbe":"Douchanbé","Ashgabat":"Achgabat","Abu Dhabi":"Abou Dabi","Washington D.C.":"Washington","Tashkent":"Tachkent","Hanoi":"Hanoï","Sana'a":"Sanaa","Valletta":"La Valette","Bishkek":"Bichkek","Addis Ababa":"Addis-Abeba","Manila":"Manille","Santo Domingo":"Saint-Domingue","N'Djamena":"N'Djaména","Singapore":"Singapour"}
HOME=['FRA','BEL','CHE','LUX','CAN','HTI','SEN','CIV','MLI','BFA','NER','TCD','GIN','CMR','GAB','COG','COD','BEN','TGO','MDG','BDI','RWA','DJI','CAF']
T=['${right}/${total} en ${this.fmt(secs)}',
"const WALES=20782;\nconst HOME=new Set("+json.dumps(HOME)+");const UNIT=8680;\n/* country names with their article (la France, le Brésil, les États-Unis) for the sentences; que becomes qu' before a vowel */\nconst ART="+json.dumps(ART,ensure_ascii=False)+";\nfunction que(c){const a=ART[c.id]||c.n;return (/^[AEIOUYÉÈÊÎÔ]/.test(a)?\"qu'\":'que ')+'<b>'+esc(a)+'</b>'}",
'COUNTRIES.filter(c=>HOME.has(c.id))','COUNTRIES.filter(c=>!HOME.has(c.id))',
"const rtxt=r<1.1?`à peine ${dec((r-1)*100,1)}"+NB+"% plus vaste`:`${dec(r,r<10?1:0)} fois plus vaste`;",
'${i+1}. ${esc(a.n)} – ${esc(b.n)}',
'😲 <b>La plus grosse surprise'+NB+':</b> ${esc(surprise.big.n)}, ${dec(surprise.r,1)} fois plus vaste ${que(surprise.small)}.',
'🎯 <b>Au coude-à-coude'+NB+':</b> ${esc(closest.big.n)}, seulement ${fmt(closest.big.a-closest.small.a)} km² de plus ${que(closest.small)}.',
"'<span class=\"st ok\">✓ Coché — juste</span>':'<span class=\"st no\">✗ Coché — mais c’est plus petit</span>'",
"'<span class=\"st ok\">✓ Laissé vide — juste</span>':'<span class=\"st no\">✗ Oublié — c’est plus grand</span>'",
'🎯 <b>Au coude-à-coude'+NB+':</b> ${esc(closest.c.n)} fait ${multTxt(closest.r)} la superficie de ${esc(closest.t.n)}, et tu as quand même trouvé.',
"COUNTRIES.slice().sort((a,b)=>a.n.localeCompare(b.n,'fr'))",
'<html lang="fr">','<title>Natural Wonders · Lequel est le plus grand'+NB+'?</title>',
"'Temps restant pour cette question'",
"`${s} seconde${s===1?'':'s'}`:`${Math.floor(s/60)} min ${s%60} s`",
"`page quittée ${this.left} fois`:'resté sur la page tout du long'",
'<div class="label">Chrono</div>','⏱ Chronométré<small>','Sans chrono<small>Prends ton temps</small>',
"const fmt=n=>n.toLocaleString('fr-FR');const dec=(x,d)=>x.toFixed(d).replace('.',',');",
"function wales(a){const w=a/UNIT;if(Math.abs(w-1)<.005)return 'exactement 1 Corse';if(w>=100)return '≈ '+fmt(Math.round(w))+' fois la Corse';if(w>=1)return '≈ '+dec(w,1)+' fois la Corse';return '≈ '+dec(w,w<.1?2:1)+' Corse'}",
"function multTxt(r){return r>=10?Math.round(r)+'×':r>=.1?dec(r,1)+'×':r>=.01?dec(r,2)+'×':dec(r,3)+'×'}",
'aria-label="Silhouette du pays"',
"const MODES={names:{t:'Mode 1 — Silhouette + nom',s:'Voir la forme et le nom'},hidden:{t:'Mode 2 — Silhouette seule',s:'Juste la forme. Les noms sont révélés à la fin'}};",
"const DIFFS3T={easy:{t:'Facile',s:'Géants et lilliputiens'},medium:{t:'Moyen',s:'1,3 à 3 fois la cible'},hard:{t:'Difficile',s:'Proche de la taille de la cible'}};",
"const DIFFS={easy:{t:'Facile',s:'2 à 8 fois plus vaste',lo:2,hi:8},medium:{t:'Moyen',s:'1,3 à 2,2 fois plus vaste',lo:1.3,hi:2.2},hard:{t:'Difficile',s:'Moins de 35"+NB+"% d’écart',lo:1.03,hi:1.35}};",
"const REGIONS={world:{t:'Monde entier',s:'Un mélange de tous les continents'},home:{t:'Pays francophones',s:'La francophonie contre le reste du monde'},Europe:{t:'Europe'},Asia:{t:'Asie'},Africa:{t:'Afrique'},Americas:{t:'Amériques et Océanie'}};",
"const LAYOUTS={auto:'Auto',phone:'Téléphone',tablet:'Tablette',desktop:'Ordinateur'};",
'<b>Natural Wonders</b> · Jeu 8 sur 10 · <a href="https://twominute.games/wonders/">Tous les jeux</a>',
'<h1>Lequel est le plus grand'+NB+'?</h1>',
'Lequel couvre le plus de terre'+NB+'? Fais tous tes choix, puis découvre les vraies superficies à la fin. Prépare-toi à être surpris.',
'<div class="label">Mode de jeu</div>','<div class="label">Nombre de manches</div>','<div class="label">Nombre de paires</div>',
'${n} manches<small>${n*5} réponses</small>','${n} paires</button>',"TM.menuRow('30 secondes par manche')",
'<div class="label">Difficulté</div>','<div class="label">Pays</div>',
"C’est parti — ${S.mode==='bigger'?S.rounds3+' manches':S.count+' paires'}",
'<p class="foot">Affichage <span class="lay">',
'${COUNTRIES.length} pays · superficies totales en km² (terres et eaux intérieures) · Natural Wonders'+NB+': Lequel est le plus grand'+NB+'? ${VERSION} · <button class="srclink" onclick="openSources()">Sources</button>',
"toast('Pas assez de pays pour cette combinaison. Essaie une autre région.')",
"toast('Pas assez de pays pour cette combinaison. Essaie moins de paires ou une autre région.')",
'aria-label="Choisir ${named?esc(c.n):\'le pays \'+k}"',
"${side?'→':'←'} touche</span>",
'<button class="link" onclick="back()">← Paire précédente</button>','<button class="link" onclick="back()">← Manche précédente</button>',
'<button class="link" onclick="quit()">Quitter</button>',
'Lequel est le plus grand'+NB+'?<span>Paire ${S.cur+1} sur ${S.pairs.length}</span>',
'Les formes ne sont pas à l’échelle. Chacune est agrandie pour remplir sa case.',
"${ok?'✓ Trouvé':S.picks[i]==null?'⏱ Temps écoulé':'✗ Tu as choisi '+esc(p[S.picks[i]].n)}",
'<span class="tstat">${dec(S.times[i],1)} s</span>',
'<b>${esc(big.n)}</b>'+NB+': ${rtxt} ${que(small)}',
"' · capitale '+esc(",
'😲 <b>La plus grosse surprise'+NB+':</b> ${esc(surprise.c.n)} fait ${surprise.r>1?\'\':\'seulement \'}${multTxt(surprise.r)} la superficie de ${esc(surprise.t.n)}.',
'<h1>Résultats</h1>','onclick="startGame()">Rejouer</button>','onclick="quit()">Modifier les réglages</button>','>Partager mon score</button>',
'<button class="btn ghost" onclick="openSources()">Sources</button>','href="https://twominute.games/wonders/">Plus de jeux</a>',
'Les réponses à la même échelle (le plus grand pays en noir)','aria-label="Les deux pays à la même échelle"',
'Superficies'+NB+': CIA World Factbook (dernière édition, superficie totale)'+NB+'; Angleterre, Écosse, pays de Galles et Irlande du Nord'+NB+': Office for National Statistics. Contours'+NB+': Natural Earth. <button class="srclink" onclick="openSources()">Voir toutes les sources</button>',
'<div class="slabel">Manche ${ri+1}</div><h3>Plus grand que ${esc(t.n)}'+NB+'?</h3>',
"'Temps écoulé"+NB+": tes coches ont été validées telles quelles':'Répondu en '+dec(R.secs,1)+' s'",
'aria-label="Les six pays à la même échelle"','Les six à la même échelle',
'${S.game3.length} manches ·','<div class="label" style="margin-top:28px">Manche par manche</div>',
"' Touches A–E pour cocher, Entrée pour valider.'",'>Valider ma réponse<','>Valider<','>Le pays à battre<','>Ta réponse<',"'Rien de coché'",
'Manche ${S.cur+1} sur ','Coche tous ceux qui conviennent. Il peut n’y en avoir aucun, ou les cinq.',
'Lesquels sont plus grands que <em>','Lesquels de ceux-ci sont plus grands que <em>',
"const t=`Natural Wonders"+NB+": Lequel est le plus grand"+NB+"? J’ai fait ${r}/${n} (${S.mode==='bigger'?'Plus grand que…, ':''}${DIFFS[S.diff].t}, ${REGIONS[S.region].t}). Tu fais mieux"+NB+"?`;",
"toast('Score copié. Envoie-le à un ami.')",
'aria-label="Sources"><button class="srcx" onclick="closeSources()">Fermer</button>','<h2>Sources</h2>',
'<h3>Tous les pays et leur superficie</h3><details><summary>${COUNTRIES.length} pays</summary>',
"setAttribute('aria-label','Changer de jeu')",'<a class="home" href="/wonders/">← Tous les jeux</a>',
"{n:'Lequel est le plus grand"+NB+"?',slug:'where-is-bigger',ic:'bigger',t:'Deux pays côte à côte. Lequel couvre le plus de terre"+NB+"? Les cartes te trompent depuis des années.'}",
'/^Rejouer$/',"À essayer${rec.games[n.slug]?' · ton score le plus bas':' · pas encore joué'} · en anglais",
'<span class="go">Jouer →</span>','<b>${done} sur ${GAMES.length}</b>',
'</b> Natural Wonders explorés</span><a href="/wonders/#record">Tes records →</a>']
V=["'Score parfait. Niveau cartographe.'","'Excellent. Tu connais tes cartes.'","'Bel effort. Quelques surprises au passage.'","'La carte t’a un peu trompé.'","'Les formes peuvent être très trompeuses"+NB+"!'"]
SRC=['Les chiffres de ce jeu ont été repris de bonne foi des sources publiées ci-dessous en octobre 2026 et sont présentés tels que ces sources les donnent. Des sources sérieuses mesurent les superficies de façon un peu différente (par exemple en incluant ou non les lacs, les fleuves et les eaux côtières)'+NB+': tu trouveras peut-être d’autres chiffres ailleurs, et une source peut parfois se tromper. Si un chiffre te semble faux, voici d’où il vient.',
'<h3>Superficies des pays</h3>',', superficie totale (terres et eaux intérieures), de sa dernière édition. La CIA a cessé de publier le Factbook en février 2026'+NB+'; ses données sont conservées dans l’archive publique',
'factbook.json</a>',
'Pour la France, c’est le chiffre du Factbook pour la France métropolitaine (551'+NB+'500 km²) qui est utilisé, pour correspondre au contour affiché, sans les régions d’outre-mer comme la Guyane.',
'Le Maroc n’est pas inclus'+NB+': le chiffre du Factbook comprend le territoire disputé du Sahara occidental, le chiffre et le contour ne correspondraient donc pas.',
'<h3>Angleterre, Écosse, pays de Galles et Irlande du Nord</h3>',', Standard Area Measurements, tels qu’indiqués sur',
NB+': Angleterre 130'+NB+'462 km², Écosse 78'+NB+'803 km², pays de Galles 20'+NB+'782 km², Irlande du Nord 14'+NB+'333 km².</li><li>Les comparaisons avec la Corse utilisent 8'+NB+'680 km² (Insee).',
'<h3>Capitales</h3>','Le jeu de données libre «'+NB+'world-countries'+NB+'» de Mohammed Le Doze (',
'<h3>Cartes</h3>','Contours des pays'+NB+':',' (1:10m, domaine public). Les territoires d’outre-mer éloignés ne figurent pas sur les contours.']
FB=["[['idea','💡 Idée','Qu’est-ce qui le rendrait meilleur"+NB+"?'],['like','👍 J’aime','Qu’as-tu aimé"+NB+"?'],['wrong','🐞 Un problème','Qu’est-ce qui n’a pas marché, et où"+NB+"?']]",
'aria-label="Avis ou signaler un problème"><h2>Dis-nous ce que tu en penses</h2>',
'Idées, coups de cœur, reproches ou quelque chose de cassé. Ton message va en privé à Two Minute Games'+NB+'; personne d’autre ne peut le lire.',
'aria-label="Ton message"',
'placeholder="Nom ou e-mail, seulement si tu veux une réponse (facultatif)" aria-label="Nom ou e-mail (facultatif)"',
'Nous envoyons aussi le jeu sur lequel tu étais et ton type d’appareil, rien d’autre.',
'<button type="button" class="tmgfb-b">Annuler</button><button type="submit" class="tmgfb-b go">Envoyer</button>',
"m.textContent='Envoi…'","m.textContent='Merci. Envoyé"+NB+"!'","m.textContent='Envoi impossible pour le moment. Réessaie dans un instant.'",
"p.setAttribute('aria-label','Avis ou signaler un problème');p.innerHTML=ICON+'Avis ou bug'"]
HEAD='''<meta name="description" content="Quel pays est le plus grand ? Deux minutes, gratuit, sans inscription.">
<meta property="og:title" content="Lequel est le plus grand ? · Natural Wonders">
<meta property="og:description" content="Quel pays est le plus grand ? Deux minutes, gratuit, sans inscription.">
<meta property="og:image" content="https://twominute.games/fr/card-v1.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="https://twominute.games/natural-wonders-where-is-bigger/fr/">
<meta property="og:locale" content="fr_FR"><meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="en" href="https://twominute.games/natural-wonders-where-is-bigger/">
<link rel="alternate" hreflang="fr" href="https://twominute.games/natural-wonders-where-is-bigger/fr/">'''
EXTRA=[('${esc(big.n)}: <b>','${esc(big.n)}'+NB+': <b>',1),('${esc(small.n)}: <b>','${esc(small.n)}'+NB+': <b>',1)]
langkit.build(dict(code='fr',names=NAMES,caps=CAPS,T=T,V=V,SRC=SRC,FB=FB,head=HEAD,see='Voir aussi',sources_end='<h3>Tous les pays et leur superficie</h3>',extra=EXTRA))
