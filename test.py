from main.py import *


def main():
    print("#############")
    print("VOORBEELD 1")
    print("#############")

    print("-- ontmoetingen registreren --")

    contact_tracing_datastructuur = initialiseer_contacttracing()

    registreer_ontmoeting(contact_tracing_datastructuur,("Pieter","Koen"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Bart","Koen", "Kim"))

    print("-- vraag ontmoetingen op --")

    if geef_alle_namen(contact_tracing_datastructuur) != {'Bart', 'Kim', 'Koen', 'Pieter'}:
        print("geef_alle_namen(contact_tracing_datastructuur) :", "expected: ","{'Bart', 'Kim', 'Koen', 'Pieter'}", "- Returned: ", geef_alle_namen(contact_tracing_datastructuur))

    if sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Koen")) != ['Bart', 'Kim', 'Pieter']:
        print("sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, Koen)):", "expected: ","['Bart', 'Kim', 'Pieter']", "- Returned: ", sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Koen")))

    print("-- contact gehad --")

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Pieter", 0): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Pieter", 0)!=True')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Koen", 0): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Koen", 0)!=True')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Kim", "Pieter", 1): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Kim", "Pieter", 1)!=True')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Pieter", "Kim", 1): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Pieter", "Kim", 1)!=True')

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Pieter", "Kim", 0): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Pieter", "Kim", 0)!=True')

    ## UITBREIDING 1

    print("## UITBREIDING 1: groter netwerk ##")
    print("-- extra ontmoetingen registreren --")

    registreer_ontmoeting(contact_tracing_datastructuur,("Pieter","Tom"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Bart", "Yana"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Yana","Wouter"))
    registreer_ontmoeting(contact_tracing_datastructuur, ("Wouter", "Bert"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Koen", "Koen")) #ontmoeting met zichzelf

    print("-- vraag ontmoetingen op --")

    if geef_alle_namen(contact_tracing_datastructuur) != {'Bart', 'Bert', 'Kim', 'Koen', 'Pieter', 'Tom', 'Wouter', 'Yana'}:
        print("geef_alle_namen(contact_tracing_datastructuur) :", "expected: ","{'Bart', 'Bert', 'Kim', 'Koen', 'Pieter', 'Tom', 'Wouter', 'Yana'}", "- Returned: ", geef_alle_namen(contact_tracing_datastructuur))

    if sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Koen")) != ['Bart', 'Kim', 'Pieter']: #geen rechtstreekse contacten bijgekomen voor Koen
        print("sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, 'Koen')):", "expected: ","['Bart', 'Kim', 'Pieter']", "- Returned: ", sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Koen")))

    if sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Pieter")) != ['Koen', 'Tom']: #geen rechtstreekse contacten bijgekomen voor Koen
        print("sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, 'Pieter')):", "expected: ","['Koen', 'Tom']", "- Returned: ", sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Pieter")))

    print("-- contact gehad --")

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Wouter", 1): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Wouter", 1)!=False')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Wouter",2): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Wouter", 2)!=True')

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert", 2): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert", 2)!=False')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert", 3): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert", 3)!=True')


    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert"): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert")!=True')

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Beyonce"): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Beyonce")!=False')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Koen", 0): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Koen")!=True')

    print("-- rechtstreekse besmettingen --")

    if kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Koen", "Wouter"]): #False
        print('kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Koen", "Wouter"])!=False')

    if not kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Tom", "Bart", "Bert"]): #True
        print('kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Tom", "Bart", "Bert"])!=True')

    print("-- hops --")

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"])!=3:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"])!=3', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Kim"])!=3:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Kim"])!=3', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Kim"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Tom"])!=5:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Tom"])!=5', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Tom"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bart"])!=2:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bart"])==2', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bart"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert"])!=5:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert"])!=5', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Yana"])!=3:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Yana"])!=3', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Yana"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pieter"])!=4:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pieter"])!=4', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pieter"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter"])!=4:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter"])!=4', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Pieter"])!=1:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Pieter])!=1', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Pieter"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Tom"])!=2:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Tom"])!=2', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Tom"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Pieter"])!=1:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Pieter"])!=1', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Pieter"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Tom"])!=2:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Tom"])!=2', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Tom"]))

    (hops, superspreaders)=hops_nodig_voor_volledig_geinfecteerde_populatie(contact_tracing_datastructuur) #(2,{'Bart'})
    if hops != 2:
        print('hops!=2', ' - output: ', hops)

    if superspreaders!={'Bart'}:
        print("superspreaders!={'Bart'}", ' - output: ', superspreaders)

    ## UITBREIDING 2 ##

    print("## UITBREIDING 2: vrijstaande ontmoeting ##")
    print("-- extra ontmoeting registreren --")
    registreer_ontmoeting(contact_tracing_datastructuur,("Ronald", "Stefan"))

    print("-- vraag ontmoetingen op --")

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Ronald"): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Ronald")!=False')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Stefan", "Ronald"): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Stefan", "Ronald")!=True')

    print("-- hops --")
    # geen volledige infectie mogelijk

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"])!=-1:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"])!=-1', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen", "Stefan"])!=3:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen", "Stefan])!=3', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen", "Stefan"]))

    (hops, superspreaders)=hops_nodig_voor_volledig_geinfecteerde_populatie(contact_tracing_datastructuur)
    if hops != -1:
        print('hops!= -1', ' - output: ', hops)

    if superspreaders!= set():
        print("superspreaders!=set()", ' - output: ', superspreaders)

    print("#############")
    print("VOORBEELD 2")
    print("#############")

    print("-- ontmoetingen registreren --")

    contact_tracing_datastructuur = initialiseer_contacttracing()

    registreer_ontmoeting(contact_tracing_datastructuur,("Mickey","Minnie"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Pluto","Mickey","Goofy"))
    registreer_ontmoeting(contact_tracing_datastructuur, ("Goofy","Donald"))
    registreer_ontmoeting(contact_tracing_datastructuur, ("Donald","Chip","Dale"))

    print("-- vraag ontmoetingen op --")

    if geef_alle_namen(contact_tracing_datastructuur) != {"Mickey","Minnie","Pluto","Goofy","Donald","Chip","Dale"}:
        print("geef_alle_namen(contact_tracing_datastructuur) :", "expected: ","{'Mickey','Minnie','Pluto','Goofy','Donald','Chip','Dale'}", "- Returned: ", geef_alle_namen(contact_tracing_datastructuur))

    if sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Mickey")) != ['Goofy','Minnie','Pluto']:
        print("sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, Mickey)):", "expected: ","['Goofy','Minnie','Pluto']", "- Returned: ", sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Mickey")))

    print("-- contact gehad --")

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Mickey", "Minnie", 0): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Mickey", "Minnie", 0)!=True')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Donald", "Donald", 0): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Donald", "Donald", 0)!=True')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Mickey", "Donald", 1): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Mickey", "Donald", 1)!=True')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Pluto", "Minnie", 1): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Pluto", "Minnie", 1)!=True')

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Dale", "Goofy", 0): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Pieter", "Kim", 0)!=True')

    ## UITBREIDING 1

    print("## UITBREIDING 1: groter netwerk ##")
    print("-- extra ontmoetingen registreren --")

    registreer_ontmoeting(contact_tracing_datastructuur,("Minnie","Daisy"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Dale", "Dale")) #ontmoeting met zichzelf

    print("-- vraag ontmoetingen op --")

    if geef_alle_namen(contact_tracing_datastructuur) != {"Mickey","Minnie","Pluto","Goofy","Donald","Chip","Dale","Daisy"}:
        print("geef_alle_namen(contact_tracing_datastructuur) :", "expected: ","{'Mickey','Minnie','Pluto','Goofy','Donald','Chip','Dale','Daisy}", "- Returned: ", geef_alle_namen(contact_tracing_datastructuur))

    if sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Mickey")) != ['Goofy', 'Minnie', 'Pluto']: #geen rechtstreekse contacten bijgekomen voor Koen
        print("sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, 'Mickey')):", "expected: ","['Goofy', 'Minnie', 'Pluto']", "- Returned: ", sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Mickey")))

    if sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Donald")) != ['Chip', 'Dale', 'Goofy']:
        print("sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, 'Donald')):", "expected: ","['Chip', 'Dale', 'Goofy']", "- Returned: ", sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Donald")))

    print("-- contact gehad --")

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Daisy", "Pluto", 1): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Daisy", "Pluto", 1)!=False')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Dale", "Pluto",2): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Dale", "Pluto", 2)!=True')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Dale", "Pluto",3): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Dale", "Pluto", 3)!=True')

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Daisy", "Chip", 2): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Daisy", "Chip", 2)!=False')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Chip", "Minnie", 3): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Chip", "Minnie", 3)!=True')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Daisy", "Dale"): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Daisy", "Dale")!=True')

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Mickey", "Assepoester"): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Mickey", "Assepoester")!=False')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Chip", "Chip", 0): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Chip", "Chip")!=True')

    print("-- rechtstreekse besmettingen --")

    if kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Donald", "Daisy"]): #False
        print('kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Donald", "Daisy"])!=False')

    if not kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Chip", "Pluto", "Daisy"]): #True
        print('kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Chip", "Pluto", "Daisy"])!=True')

    print("-- hops --")

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Mickey"])!=2:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Mickey"])!=2', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Mickey"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pluto"])!=2:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pluto"])!=2', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pluto"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Daisy"])!=4:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Daisy"])!=4', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Daisy"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Chip"])!=4:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Chip"])==4', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Chip"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Donald"])!=3:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter"])!=3', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Donald"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Minnie", "Donald"])!=1:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Minnie", "Donald"])!=1', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Minnie", "Donald"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Dale", "Minnie"])!=1:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Dale", "Minnie"])!=1', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Dale", "Minnie"]))

    (hops, superspreaders)=hops_nodig_voor_volledig_geinfecteerde_populatie(contact_tracing_datastructuur) #(2,{'Mickey', 'Goofy', 'Pluto'})
    if hops != 2:
        print('hops!=2', ' - output: ', hops)

    if superspreaders!={'Mickey', 'Goofy', 'Pluto'}:
        print("superspreaders!={'Mickey', 'Goofy', 'Pluto'}", ' - output: ', superspreaders)

    ## UITBREIDING 2 ##

    print("## UITBREIDING 2: vrijstaande ontmoeting ##")
    print("-- extra ontmoeting registreren --")
    registreer_ontmoeting(contact_tracing_datastructuur,("Tom", "Jerry"))

    print("-- vraag ontmoetingen op --")

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Donald", "Jerry"): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Donald", "Jerry")!=False')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Tom", "Jerry"): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Tom", "Jerry")!=True')

    print("-- hops --")
    # geen volledige infectie mogelijk

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Mickey"])!=-1:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Mickey"])!=-1', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Mickey"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pluto", "Tom"])!=2:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pluto", "Tom"])!=2', ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pluto", "Tom"]))

    (hops, superspreaders)=hops_nodig_voor_volledig_geinfecteerde_populatie(contact_tracing_datastructuur)
    if hops != -1:
        print('hops!= -1', ' - output: ', hops)

    if superspreaders!= set():
        print("superspreaders!=set()", ' - output: ', superspreaders)

# VOEG EVENTUELE EXTRA TESTEN TOE BOVEN DEZE LIJN
if __name__ == "__main__":
    main()