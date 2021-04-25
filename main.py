def initialiseer_contacttracing():
    return {}

def registreer_ontmoeting(ontmoetingen, personen):
    for i in personen:
        ontmoetingen.setdefault(i, {})
        ontmoetingen[i] |= {j:0 for j in set(personen) - {i}}
    lengteUpdater(ontmoetingen, personen)

def geef_rechtstreekse_contacten(ontmoetingen, persoon_X):
    return [i for i in ontmoetingen[persoon_X] if ontmoetingen[persoon_X][i] == 0]

def is_lid_van_populatie(ontmoetingen, persoon):
    return persoon in geef_alle_namen(ontmoetingen)

def geef_alle_namen(ontmoetingen):
    return set(ontmoetingen)

def heeft_contact_gehad_met(ontmoetingen, persoon_X, persoon_Y, afstand=-1):
    if persoon_X == persoon_Y:
        return True
    if not is_lid_van_populatie(ontmoetingen, persoon_X) or not is_lid_van_populatie(ontmoetingen, persoon_Y):
        return False
    return (ontmoetingen[persoon_X][persoon_Y]<=afstand and ontmoetingen[persoon_X][persoon_Y]!=-1) if afstand!=-1 else ontmoetingen[persoon_X][persoon_Y]!=-1

def kan_iedereen_rechtstreeks_besmetten(ontmoetingen, geinfecteerd_by_start):
    return set(geinfecteerd_by_start).union(*[set(geef_rechtstreekse_contacten(ontmoetingen, i)) for i in set(geinfecteerd_by_start) & geef_alle_namen(ontmoetingen)]) == geef_alle_namen(ontmoetingen)

def hops_nodig_voor_geinfecteerde_populatie(ontmoetingen, geinfecteerd):
    hops = 0
    while hops <= len(geef_alle_namen(ontmoetingen)):
        if (geinfecteerd:=set(geinfecteerd).union(*[set(geef_rechtstreekse_contacten(ontmoetingen, i)) for i in set(geinfecteerd) & geef_alle_namen(ontmoetingen)])) == geef_alle_namen(ontmoetingen):
            return hops
        hops += 1
    return -1

def hops_nodig_voor_volledig_geinfecteerde_populatie(ontmoetingen):
    hops_dic = {i:hops for i in geef_alle_namen(ontmoetingen) if (hops:=hops_nodig_voor_geinfecteerde_populatie(ontmoetingen, [i]))!=-1}
    return (min_hops:=(min(hops_dic.values()) if len(hops_dic)!=0 else -1), set([persoon for persoon, hop in hops_dic.items() if hop==min_hops]))

def lengteUpdater(ontmoetingen, personen):
    def kortste_lengte(ontmoetingen, persoon_X, persoon_Y):
        def kortste_pad_vinder(ontmoetingen, persoon_X, persoon_Y, pad=[], lengte=-1):
            pad = pad + [persoon_X]
            if persoon_X == persoon_Y:
                return pad
            kortste_pad = None
            for buur in geef_rechtstreekse_contacten(ontmoetingen, persoon_X):
                if buur not in pad and (lengte==-1 or len(pad)<(lengte-1)):
                    nieuw_pad = kortste_pad_vinder(ontmoetingen, buur, persoon_Y, pad, lengte)
                    if nieuw_pad and (not kortste_pad or len(nieuw_pad) < len(kortste_pad)):
                        kortste_pad = nieuw_pad
                        lengte = len(nieuw_pad)
            return kortste_pad
        if (kortste_pad:=kortste_pad_vinder(ontmoetingen, persoon_X, persoon_Y)) == None:
            return -1
        return len(kortste_pad)-2
    for i in personen:
        for j in (geef_alle_namen(ontmoetingen) - set(personen)):
            ontmoetingen[i][j] = ontmoetingen[j][i] = kortste_lengte(ontmoetingen, i, j)
