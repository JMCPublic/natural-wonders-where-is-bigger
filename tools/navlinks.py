"""Game switcher on the translated pages: other Natural Wonders games that exist in the same language get a
translated name and blurb, and their links go to that language. Add a game here when it is translated."""
import json
TRANSLATED = {
 'rivers': {
  'es': ('Ríos', 'Ordena los grandes ríos del mundo por longitud. ¿El Nilo o el Amazonas? Las respuestas pueden sorprenderte.'),
  'pt': ('Rios', 'Coloque os grandes rios do mundo em ordem de comprimento. O Nilo ou o Amazonas? As respostas podem surpreender.'),
  'fr': ('Fleuves', 'Classez les grands fleuves du monde par longueur. Le Nil ou l’Amazone ? Les réponses pourraient vous surprendre.'),
  'de': ('Flüsse', 'Bring die großen Flüsse der Welt nach Länge in die richtige Reihenfolge. Nil oder Amazonas? Die Antworten könnten dich überraschen.'),
  'tr': ('Nehirler', 'Dünyanın büyük nehirlerini uzunluklarına göre sırala. Nil mi, Amazon mu? Cevaplar seni şaşırtabilir.')},
}
EN = {'rivers': "{n:'Rivers',slug:'rivers',ic:'rivers',t:'Put the world’s great rivers in order of length. The Nile or the Amazon? The answers might surprise you.'}"}
ICON = {'rivers': 'rivers'}
def patch(s, code):
    slugs = ['where-is-bigger']
    for slug, by in TRANSLATED.items():
        if code not in by: continue
        n, t = by[code]
        if s.count(EN[slug]) != 1: raise SystemExit(f'navlinks: {slug} entry not found once')
        s = s.replace(EN[slug], "{n:" + json.dumps(n, ensure_ascii=False) + ",slug:'" + slug + "',ic:'" + ICON[slug] + "',t:" + json.dumps(t, ensure_ascii=False) + "}")
        slugs.append(slug)
    old = "const url=g=>'/natural-wonders-'+g.slug+'/';"
    if s.count(old) != 1: raise SystemExit('navlinks: url line not found once')
    trl = '{' + ','.join(f"'{x}':1" for x in slugs) + '}'
    s = s.replace(old, f"const TRL={trl};const url=g=>'/natural-wonders-'+g.slug+'/'+(TRL[g.slug]?'{code}/':'');")
    # "in English" on the Try next card only for games that aren't in this language
    import re as _re
    m=_re.search(r"'\}( · [^<'`]+)</span><h3>\$\{n\.n\}</h3>",s)
    if not m: raise SystemExit('try-next label not found')
    s=s.replace(m.group(0),"'}${TRL[n.slug]?'':'"+m.group(1)+"'}</span><h3>${n.n}</h3>",1)
    return s
