from backend import *

def main():
    contact_tracing_datastructuur = initialiseer_contacttracing()
    registreer_ontmoeting(contact_tracing_datastructuur,("Pieter","Koen"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Bart","Koen", "Kim"))

    assert geef_alle_namen(contact_tracing_datastructuur) == {'Bart', 'Kim', 'Koen', 'Pieter'}
    assert sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Koen")) == ['Bart', 'Kim', 'Pieter']
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Pieter", 0)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Koen", 0)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Kim", "Pieter", 1)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Pieter", "Kim", 1)
    assert not heeft_contact_gehad_met(contact_tracing_datastructuur, "Pieter", "Kim", 0)


    registreer_ontmoeting(contact_tracing_datastructuur,("Pieter","Tom"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Bart", "Yana"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Yana","Wouter"))
    registreer_ontmoeting(contact_tracing_datastructuur, ("Wouter", "Bert"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Koen", "Koen"))

    assert geef_alle_namen(contact_tracing_datastructuur) == {'Bart', 'Bert', 'Kim', 'Koen', 'Pieter', 'Tom', 'Wouter', 'Yana'}
    assert sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Koen")) == ['Bart', 'Kim', 'Pieter']
    assert sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Pieter")) == ['Koen', 'Tom']
    assert not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Wouter", 1)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Wouter",2)
    assert not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert", 2)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert", 3)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert")
    assert not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Beyonce")
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Koen", 0)
    assert not kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Koen", "Wouter"])
    assert kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Tom", "Bart", "Bert"])
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"]) == 3
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Kim"]) == 3
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Tom"]) == 5
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bart"]) == 2
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert"]) == 5
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Yana"]) == 3
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pieter"]) == 4
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter"]) == 4
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Pieter"]) == 1
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Tom"]) == 2
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Pieter"]) == 1
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Tom"]) == 2
    (hops, superspreaders) = hops_nodig_voor_volledig_geinfecteerde_populatie(contact_tracing_datastructuur)
    assert hops == 2
    assert superspreaders == {'Bart'}


    registreer_ontmoeting(contact_tracing_datastructuur,("Ronald", "Stefan"))

    assert not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Ronald")
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Stefan", "Ronald")
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"]) == -1
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen", "Stefan"]) == 3
    (hops, superspreaders)=hops_nodig_voor_volledig_geinfecteerde_populatie(contact_tracing_datastructuur)
    assert hops == -1
    assert superspreaders == set()



    contact_tracing_datastructuur = initialiseer_contacttracing()
    registreer_ontmoeting(contact_tracing_datastructuur,("Mickey","Minnie"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Pluto","Mickey","Goofy"))
    registreer_ontmoeting(contact_tracing_datastructuur, ("Goofy","Donald"))
    registreer_ontmoeting(contact_tracing_datastructuur, ("Donald","Chip","Dale"))

    assert geef_alle_namen(contact_tracing_datastructuur) == {"Mickey","Minnie","Pluto","Goofy","Donald","Chip","Dale"}
    assert sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Mickey")) == ['Goofy','Minnie','Pluto']
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Mickey", "Minnie", 0)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Donald", "Donald", 0)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Mickey", "Donald", 1)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Pluto", "Minnie", 1)
    assert not heeft_contact_gehad_met(contact_tracing_datastructuur, "Dale", "Goofy", 0)
 

    registreer_ontmoeting(contact_tracing_datastructuur,("Minnie","Daisy"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Dale", "Dale"))

    assert geef_alle_namen(contact_tracing_datastructuur) == {"Mickey","Minnie","Pluto","Goofy","Donald","Chip","Dale","Daisy"} 
    assert sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Mickey")) == ['Goofy', 'Minnie', 'Pluto']
    assert sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Donald")) == ['Chip', 'Dale', 'Goofy']
    assert not heeft_contact_gehad_met(contact_tracing_datastructuur, "Daisy", "Pluto", 1)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Dale", "Pluto",2)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Dale", "Pluto",3)
    assert not heeft_contact_gehad_met(contact_tracing_datastructuur, "Daisy", "Chip", 2)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Chip", "Minnie", 3)
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Daisy", "Dale")
    assert not heeft_contact_gehad_met(contact_tracing_datastructuur, "Mickey", "Assepoester")
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Chip", "Chip", 0)
    assert not kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Donald", "Daisy"])
    assert kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Chip", "Pluto", "Daisy"])
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Mickey"]) == 2
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pluto"]) == 2
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Daisy"]) == 4
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Chip"]) == 4
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Donald"]) == 3
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Minnie", "Donald"]) == 1
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Dale", "Minnie"]) == 1
    (hops, superspreaders) = hops_nodig_voor_volledig_geinfecteerde_populatie(contact_tracing_datastructuur)
    assert hops == 2
    assert superspreaders == {'Mickey', 'Goofy', 'Pluto'}


    registreer_ontmoeting(contact_tracing_datastructuur,("Tom", "Jerry"))

    assert not heeft_contact_gehad_met(contact_tracing_datastructuur, "Donald", "Jerry")
    assert heeft_contact_gehad_met(contact_tracing_datastructuur, "Tom", "Jerry")
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Mickey"]) == -1
    assert hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pluto", "Tom"]) == 2
    (hops, superspreaders) = hops_nodig_voor_volledig_geinfecteerde_populatie(contact_tracing_datastructuur)
    assert hops == -1
    assert superspreaders == set()
       
main()