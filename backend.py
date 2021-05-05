def initialiseer_contacttracing():
    return {}

def registreer_ontmoeting(ontmoetingen, personen):
    for i in personen:
        ontmoetingen.setdefault(i, {})
        ontmoetingen[i].update({j:0 for j in set(personen) - {i}})
    for i in geef_alle_namen(ontmoetingen):
        ontmoetingen[i] = persoon_dict(ontmoetingen, i)

def geef_rechtstreekse_contacten(ontmoetingen, persoon_X):
    return [i for i in ontmoetingen[persoon_X] if ontmoetingen[persoon_X][i] == 0]

def is_lid_van_populatie(ontmoetingen, persoon):
    return persoon in geef_alle_namen(ontmoetingen)

def geef_alle_namen(ontmoetingen):
    return set(ontmoetingen)

def heeft_contact_gehad_met(ontmoetingen, persoon_X, persoon_Y, afstand=-1):
    if persoon_X == persoon_Y:
        return True
    if not is_lid_van_populatie(ontmoetingen, persoon_X) or not is_lid_van_populatie(ontmoetingen, persoon_Y) or persoon_Y not in ontmoetingen[persoon_X]:
        return False
    return ontmoetingen[persoon_X][persoon_Y]<=afstand if afstand!=-1 else True

def kan_iedereen_rechtstreeks_besmetten(ontmoetingen, geinfecteerd_by_start):
    return set(geinfecteerd_by_start).union(*[set(geef_rechtstreekse_contacten(ontmoetingen, i)) for i in set(geinfecteerd_by_start) & geef_alle_namen(ontmoetingen)]) == (geef_alle_namen(ontmoetingen) | set(geinfecteerd_by_start))

def hops_nodig_voor_geinfecteerde_populatie(ontmoetingen, geinfecteerd):
    hops = 0
    while geinfecteerd != (geinfecteerd:=set(geinfecteerd).union(*[set(geef_rechtstreekse_contacten(ontmoetingen, i)) for i in set(geinfecteerd) & geef_alle_namen(ontmoetingen)])):
        if geinfecteerd == geef_alle_namen(ontmoetingen):
            return hops
        hops += 1
    return -1

def hops_nodig_voor_volledig_geinfecteerde_populatie(ontmoetingen):
    hops_dic = {i:hops for i in geef_alle_namen(ontmoetingen) if (hops:=hops_nodig_voor_geinfecteerde_populatie(ontmoetingen, [i]))!=-1}
    return (min_hops:=(min(hops_dic.values()) if len(hops_dic)!=0 else -1), set([persoon for persoon, hop in hops_dic.items() if hop==min_hops]))

def persoon_dict(ontmoetingen, persoon):
    dic = {i:(0 if i in geef_rechtstreekse_contacten(ontmoetingen, persoon) else -1) for i in geef_alle_namen(ontmoetingen)}
    gezien = set()
    hops = 0
    while (hops:=hops+1)<=len(geef_alle_namen(ontmoetingen)):
        for i in [i for i in dic if dic[i]==hops-1 and i not in gezien]:
            gezien.add(i)
            for j in geef_rechtstreekse_contacten(ontmoetingen, i):
                dic[j] = min(dic[j], hops) if dic[j]!=-1 else hops
    return {l:m for l,m in dic.items() if (l!=persoon and m!=-1)}