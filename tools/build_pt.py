#!/usr/bin/env python3
"""Portuguese (Brazilian) page pt/index.html. Run from the repo folder: python3 tools/build_pt.py"""
import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));import langkit
S="""AFG=Afeganistão;ALB=Albânia;DZA=Argélia;AGO=Angola;ARG=Argentina;ARM=Armênia;AUS=Austrália;AUT=Áustria;AZE=Azerbaijão;BGD=Bangladesh;BLR=Belarus;BEL=Bélgica;BLZ=Belize;BEN=Benin;BTN=Butão;BOL=Bolívia;BIH=Bósnia e Herzegovina;BWA=Botsuana;BRA=Brasil;BRN=Brunei;BGR=Bulgária;BFA=Burkina Faso;BDI=Burundi;KHM=Camboja;CMR=Camarões;CAN=Canadá;CAF=República Centro-Africana;TCD=Chade;CHL=Chile;CHN=China;COL=Colômbia;CRI=Costa Rica;CIV=Costa do Marfim;HRV=Croácia;CUB=Cuba;CYP=Chipre;CZE=Tchéquia;DNK=Dinamarca;DJI=Djibuti;DOM=República Dominicana;COD=RD do Congo;ECU=Equador;EGY=Egito;SLV=El Salvador;ENG=Inglaterra;GNQ=Guiné Equatorial;ERI=Eritreia;EST=Estônia;SWZ=Essuatíni;ETH=Etiópia;FIN=Finlândia;FRA=França;GAB=Gabão;GMB=Gâmbia;GEO=Geórgia;DEU=Alemanha;GHA=Gana;GRC=Grécia;GTM=Guatemala;GIN=Guiné;GNB=Guiné-Bissau;GUY=Guiana;HTI=Haiti;HND=Honduras;HUN=Hungria;ISL=Islândia;IND=Índia;IDN=Indonésia;IRN=Irã;IRQ=Iraque;IRL=Irlanda;ISR=Israel;ITA=Itália;JAM=Jamaica;JPN=Japão;JOR=Jordânia;KAZ=Cazaquistão;KEN=Quênia;KWT=Kuwait;KGZ=Quirguistão;LAO=Laos;LVA=Letônia;LBN=Líbano;LSO=Lesoto;LBR=Libéria;LBY=Líbia;LTU=Lituânia;LUX=Luxemburgo;MDG=Madagascar;MWI=Malawi;MYS=Malásia;MLI=Mali;MLT=Malta;MRT=Mauritânia;MEX=México;MDA=Moldávia;MNG=Mongólia;MNE=Montenegro;MOZ=Moçambique;MMR=Mianmar;NAM=Namíbia;NPL=Nepal;NLD=Países Baixos;NZL=Nova Zelândia;NIC=Nicarágua;NER=Níger;NGA=Nigéria;PRK=Coreia do Norte;MKD=Macedônia do Norte;NIR=Irlanda do Norte;NOR=Noruega;OMN=Omã;PAK=Paquistão;PAN=Panamá;PNG=Papua-Nova Guiné;PRY=Paraguai;PER=Peru;PHL=Filipinas;POL=Polônia;PRT=Portugal;QAT=Catar;COG=República do Congo;ROU=Romênia;RUS=Rússia;RWA=Ruanda;WSM=Samoa;SAU=Arábia Saudita;SCT=Escócia;SEN=Senegal;SRB=Sérvia;SLE=Serra Leoa;SVK=Eslováquia;SVN=Eslovênia;SOM=Somália;ZAF=África do Sul;KOR=Coreia do Sul;SSD=Sudão do Sul;ESP=Espanha;LKA=Sri Lanka;SDN=Sudão;SUR=Suriname;SWE=Suécia;CHE=Suíça;SYR=Síria;TJK=Tajiquistão;TZA=Tanzânia;THA=Tailândia;TLS=Timor-Leste;TGO=Togo;TTO=Trinidad e Tobago;TUN=Tunísia;TUR=Turquia;TKM=Turcomenistão;ARE=Emirados Árabes Unidos;UGA=Uganda;UKR=Ucrânia;GBR=Reino Unido;USA=Estados Unidos;URY=Uruguai;UZB=Uzbequistão;VEN=Venezuela;VNM=Vietnã;WLS=País de Gales;YEM=Iêmen;ZMB=Zâmbia;ZWE=Zimbábue"""
NAMES=dict(x.split('=',1) for x in S.split(';'))
CAPS={"Kabul":"Cabul","Algiers":"Argel","Yerevan":"Erevan","Vienna":"Viena","Brussels":"Bruxelas","Beijing":"Pequim","Nicosia":"Nicósia","Prague":"Praga","Copenhagen":"Copenhague","Cairo":"Cairo","London":"Londres","Athens":"Atenas","Guatemala City":"Cidade da Guatemala","New Delhi":"Nova Délhi","Jakarta":"Jacarta","Tehran":"Teerã","Baghdad":"Bagdá","Jerusalem":"Jerusalém","Rome":"Roma","Kuwait City":"Cidade do Kuwait","Beirut":"Beirute","Tripoli":"Trípoli","Luxembourg":"Luxemburgo","Mexico City":"Cidade do México","Chișinău":"Chisinau","Kathmandu":"Katmandu","Muscat":"Mascate","Panama City":"Cidade do Panamá","Warsaw":"Varsóvia","Lisbon":"Lisboa","Bucharest":"Bucareste","Moscow":"Moscou","Riyadh":"Riad","Edinburgh":"Edimburgo","Belgrade":"Belgrado","Mogadishu":"Mogadíscio","Seoul":"Seul","Khartoum":"Cartum","Stockholm":"Estocolmo","Bern":"Berna","Damascus":"Damasco","Dushanbe":"Duchambé","Tunis":"Túnis","Ashgabat":"Asgabate","Kyiv":"Kiev","Washington D.C.":"Washington","Hanoi":"Hanói","Sana'a":"Sanaa","Tokyo":"Tóquio","Addis Ababa":"Adis Abeba","Valletta":"Valeta","Reykjavik":"Reykjavík","Amman":"Amã","Singapore":"Singapura","Cape Town":"Cidade do Cabo","Port of Spain":"Porto de Espanha","Brasília":"Brasília"}
HOME=['PRT','BRA','AGO','MOZ','GNB','TLS']
T=['${right}/${total} em ${this.fmt(secs)}',
"const WALES=20782;\nconst HOME=new Set("+json.dumps(HOME)+");const UNIT=92090; /* Portugal, CIA World Factbook */",
'COUNTRIES.filter(c=>HOME.has(c.id))','COUNTRIES.filter(c=>!HOME.has(c.id))',
"const rtxt=r<1.1?`só ${dec((r-1)*100,1)}% maior`:`${dec(r,r<10?1:0)} vezes maior`;",
'${i+1}. ${esc(a.n)} – ${esc(b.n)}',
'😲 <b>Maior surpresa:</b> ${esc(surprise.big.n)} é ${dec(surprise.r,1)} vezes maior que ${esc(surprise.small.n)}.',
'🎯 <b>Por um triz:</b> ${esc(closest.big.n)} supera ${esc(closest.small.n)} por apenas ${fmt(closest.big.a-closest.small.a)} km².',
"'<span class=\"st ok\">✓ Marcado — certo</span>':'<span class=\"st no\">✗ Marcado — mas é menor</span>'",
"'<span class=\"st ok\">✓ Em branco — certo</span>':'<span class=\"st no\">✗ Passou batido — é maior</span>'",
'🎯 <b>Por um triz:</b> ${esc(closest.c.n)} tem ${multTxt(closest.r)} o tamanho de ${esc(closest.t.n)}, e mesmo assim você acertou.',
"COUNTRIES.slice().sort((a,b)=>a.n.localeCompare(b.n,'pt'))",
'<html lang="pt">','<title>Natural Wonders · Qual é maior?</title>',
"'Tempo restante para esta pergunta'",
"`${s} segundo${s===1?'':'s'}`:`${Math.floor(s/60)} min ${s%60} s`",
"`saiu da página ${this.left} ${this.left===1?'vez':'vezes'}`:'ficou na página o tempo todo'",
'<div class="label">Tempo</div>','⏱ Com tempo<small>','Sem tempo<small>Sem pressa</small>',
"const fmt=n=>n.toLocaleString('pt-BR');const dec=(x,d)=>x.toFixed(d).replace('.',',');",
"function wales(a){const w=a/UNIT;if(Math.abs(w-1)<.005)return 'exatamente 1 Portugal';if(w>=100)return '≈ '+fmt(Math.round(w))+' vezes Portugal';if(w>=1)return '≈ '+dec(w,1)+' vezes Portugal';return '≈ '+dec(w,w<.1?2:1)+' de Portugal'}",
"function multTxt(r){return r>=10?Math.round(r)+'×':r>=.1?dec(r,1)+'×':r>=.01?dec(r,2)+'×':dec(r,3)+'×'}",
'aria-label="Silhueta do país"',
"const MODES={names:{t:'Modo 1 — Silhueta + nome',s:'Veja a forma e o nome'},hidden:{t:'Modo 2 — Só a silhueta',s:'Só a forma. Os nomes aparecem no final'}};",
"const DIFFS3T={easy:{t:'Fácil',s:'Gigantes e nanicos'},medium:{t:'Médio',s:'De 1,3 a 3 vezes o alvo'},hard:{t:'Difícil',s:'Perto do tamanho do alvo'}};",
"const DIFFS={easy:{t:'Fácil',s:'De 2 a 8 vezes maior',lo:2,hi:8},medium:{t:'Médio',s:'De 1,3 a 2,2 vezes maior',lo:1.3,hi:2.2},hard:{t:'Difícil',s:'Menos de 35% de diferença',lo:1.03,hi:1.35}};",
"const REGIONS={world:{t:'Mundo todo',s:'Uma mistura de todos os continentes'},home:{t:'Países lusófonos',s:'O mundo lusófono contra o resto do mundo'},Europe:{t:'Europa'},Asia:{t:'Ásia'},Africa:{t:'África'},Americas:{t:'Américas e Oceania'}};",
"const LAYOUTS={auto:'Auto',phone:'Celular',tablet:'Tablet',desktop:'Computador'};",
'<b>Natural Wonders</b> · Jogo 8 de 10 · <a href="https://twominute.games/wonders/">Todos os jogos</a>',
'<h1>Qual é maior?</h1>',
'Qual ocupa mais terra? Faça todos os seus palpites e veja os tamanhos reais no final. Prepare-se para se surpreender.',
'<div class="label">Modo de jogo</div>','<div class="label">Número de rodadas</div>','<div class="label">Número de pares</div>',
'${n} rodadas<small>${n*5} respostas</small>','${n} pares</button>',"TM.menuRow('30 segundos por rodada')",
'<div class="label">Dificuldade</div>','<div class="label">Países</div>',
"Começar — ${S.mode==='bigger'?S.rounds3+' rodadas':S.count+' pares'}",
'<p class="foot">Visualização <span class="lay">',
'${COUNTRIES.length} países · área total em km² (terra e águas interiores) · Natural Wonders: Qual é maior? ${VERSION} · <button class="srclink" onclick="openSources()">Fontes</button>',
"toast('Não há países suficientes para essa combinação. Tente outra região.')",
"toast('Não há países suficientes para essa combinação. Tente menos pares ou outra região.')",
'aria-label="Escolher ${named?esc(c.n):\'o país \'+k}"',
"${side?'→':'←'} tecla</span>",
'<button class="link" onclick="back()">← Par anterior</button>','<button class="link" onclick="back()">← Rodada anterior</button>',
'<button class="link" onclick="quit()">Sair</button>',
'Qual é maior?<span>Par ${S.cur+1} de ${S.pairs.length}</span>',
'As formas não estão em escala. Cada uma foi ampliada para preencher o quadro.',
"${ok?'✓ Acertou':S.picks[i]==null?'⏱ O tempo acabou':'✗ Você escolheu '+esc(p[S.picks[i]].n)}",
'<span class="tstat">${dec(S.times[i],1)} s</span>',
'<b>${esc(big.n)}</b> é ${rtxt} que <b>${esc(small.n)}</b>',
"' · capital '+esc(",
'😲 <b>Maior surpresa:</b> ${esc(surprise.c.n)} tem ${surprise.r>1?\'\':\'só \'}${multTxt(surprise.r)} o tamanho de ${esc(surprise.t.n)}.',
'<h1>Resultado</h1>','onclick="startGame()">Jogar de novo</button>','onclick="quit()">Mudar configurações</button>','>Compartilhar pontuação</button>',
'<button class="btn ghost" onclick="openSources()">Fontes</button>','href="https://twominute.games/wonders/">Mais jogos</a>',
'As respostas na mesma escala (o país maior em preto)','aria-label="Os dois países na mesma escala"',
'Áreas: CIA World Factbook (última edição, área total); Inglaterra, Escócia, País de Gales e Irlanda do Norte: Office for National Statistics. Contornos: Natural Earth. <button class="srclink" onclick="openSources()">Ver todas as fontes</button>',
'<div class="slabel">Rodada ${ri+1}</div><h3>Maior que ${esc(t.n)}?</h3>',
"'O tempo acabou: suas marcações foram salvas como estavam':'Respondido em '+dec(R.secs,1)+' s'",
'aria-label="Os seis países na mesma escala"','Os seis na mesma escala',
'${S.game3.length} rodadas ·','<div class="label" style="margin-top:28px">Rodada a rodada</div>',
"' Teclas A–E marcam, Enter confirma.'",'>Confirmar resposta<','>Confirmar<','>O país a superar<','>Sua resposta<',"'Nada marcado'",
'Rodada ${S.cur+1} de ','Marque todos que valem. Pode ser nenhum, pode ser os cinco.',
'Quais são maiores que <em>','Quais destes são maiores que <em>',
"const t=`Natural Wonders: Qual é maior? Fiz ${r}/${n} (${S.mode==='bigger'?'Maior que…, ':''}${DIFFS[S.diff].t}, ${REGIONS[S.region].t}). Consegue me superar?`;",
"toast('Pontuação copiada. Mande para um amigo.')",
'aria-label="Fontes"><button class="srcx" onclick="closeSources()">Fechar</button>','<h2>Fontes</h2>',
'<h3>Todos os países e suas áreas</h3><details><summary>${COUNTRIES.length} países</summary>',
"setAttribute('aria-label','Trocar de jogo')",'<a class="home" href="/wonders/">← Todos os jogos</a>',
"{n:'Qual é maior?',slug:'where-is-bigger',ic:'bigger',t:'Dois países lado a lado. Qual ocupa mais terra? Os mapas enganam você há anos.'}",
'/^Jogar de novo$/',"Experimente${rec.games[n.slug]?' · sua pontuação mais baixa':' · ainda não jogado'} · em inglês",
'<span class="go">Jogar →</span>','<b>${done} de ${GAMES.length}</b>',
'</b> Natural Wonders explorados</span><a href="/wonders/#record">Seus recordes →</a>']
V=["'Pontuação perfeita. Nível cartógrafo.'","'Excelente. Você conhece seus mapas.'","'Bom trabalho. Teve algumas surpresas.'","'O mapa te enganou um pouco.'","'As formas enganam muito!'"]
SRC=['Os números deste jogo foram tirados de boa-fé das fontes publicadas abaixo, em outubro de 2026, e aparecem exatamente como essas fontes os informam. Fontes confiáveis medem áreas de formas um pouco diferentes (por exemplo, incluindo ou não lagos, rios e águas costeiras), então você pode encontrar outros números por aí, e uma fonte pode errar de vez em quando. Se achar que um número está errado, aqui está de onde ele veio.',
'<h3>Áreas dos países</h3>',', área total (terra e águas interiores), da sua última edição. A CIA deixou de publicar o Factbook em fevereiro de 2026; os dados estão preservados no arquivo público',
'factbook.json</a>',
'Para a França, usa-se o número do Factbook para a França metropolitana (551.500 km²), para combinar com o contorno, que não inclui regiões ultramarinas como a Guiana Francesa.',
'O Marrocos não está incluído: o número do Factbook inclui o território disputado do Saara Ocidental, então o número e o contorno não combinariam.',
'<h3>Inglaterra, Escócia, País de Gales e Irlanda do Norte</h3>',', Standard Area Measurements, conforme',
': Inglaterra 130.462 km², Escócia 78.803 km², País de Gales 20.782 km², Irlanda do Norte 14.333 km².</li><li>As comparações com Portugal usam 92.090 km² (CIA World Factbook).',
'<h3>Capitais</h3>','O conjunto de dados aberto “world-countries” de Mohammed Le Doze (',
'<h3>Mapas</h3>','Contornos dos países:',' (1:10m, domínio público). Territórios ultramarinos distantes ficam de fora dos contornos.']
FB=["[['idea','💡 Ideia','O que deixaria melhor?'],['like','👍 Curti','Do que você gostou?'],['wrong','🐞 Algo errado','O que deu errado, e onde?']]",
'aria-label="Opinião ou relatar um problema"><h2>Conte o que você achou</h2>',
'Ideias, elogios, reclamações ou algo quebrado. Vai em particular para a Two Minute Games; ninguém mais pode ler.',
'aria-label="Sua mensagem"',
'placeholder="Nome ou e-mail, só se quiser resposta (opcional)" aria-label="Nome ou e-mail (opcional)"',
'Também enviamos em qual jogo você estava e o tipo de aparelho, nada mais.',
'<button type="button" class="tmgfb-b">Cancelar</button><button type="submit" class="tmgfb-b go">Enviar</button>',
"m.textContent='Enviando…'","m.textContent='Obrigado. Enviado!'","m.textContent='Não deu para enviar agora. Tente de novo daqui a pouco.'",
"p.setAttribute('aria-label','Opinião ou relatar um problema');p.innerHTML=ICON+'Opinião ou erro'"]
HEAD='''<meta name="description" content="Qual país é maior? Dois minutos, grátis, sem cadastro.">
<meta property="og:title" content="Qual é maior? · Natural Wonders">
<meta property="og:description" content="Qual país é maior? Dois minutos, grátis, sem cadastro.">
<meta property="og:image" content="https://twominute.games/pt/card-v1.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="https://twominute.games/natural-wonders-where-is-bigger/pt/">
<meta property="og:locale" content="pt_BR"><meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="en" href="https://twominute.games/natural-wonders-where-is-bigger/">
<link rel="alternate" hreflang="pt" href="https://twominute.games/natural-wonders-where-is-bigger/pt/">'''
langkit.build(dict(code='pt',names=NAMES,caps=CAPS,T=T,V=V,SRC=SRC,FB=FB,head=HEAD,see='Veja também',sources_end='<h3>Todos os países e suas áreas</h3>'))
