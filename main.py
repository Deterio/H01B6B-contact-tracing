import networkx as nx
import matplotlib.pyplot as plt
from backend import initialiseer_contacttracing, registreer_ontmoeting, geef_alle_namen, geef_rechtstreekse_contacten, hops_nodig_voor_geinfecteerde_populatie

def main():
    contact_tracing_datastructuur = initialiseer_contacttracing()
    G = nx.Graph()

    registreer_ontmoeting(contact_tracing_datastructuur,("Pieter","Koen"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Bart","Koen", "Kim"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Pieter","Tom"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Bart", "Yana"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Yana","Wouter"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Wouter", "Bert"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Koen", "Koen"))

    for i in geef_alle_namen(contact_tracing_datastructuur):
        G.add_node(i)
        for j in geef_rechtstreekse_contacten(contact_tracing_datastructuur, i):
            G.add_edge(i, j)

    hops_list = {i:hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur, [i]) for i in geef_alle_namen(contact_tracing_datastructuur)}
    hops = min([i for i in hops_list.values() if i!=-1]) if len(hops_list)!=0 else -1
    superverspreiders = set([persoon for persoon, hop in hops_list.items() if hop==hops])

    color_map_1 = []
    for i in G:
        if i in superverspreiders:
            color_map_1.append('red')
        elif hops_list[i] >= hops-1: 
            color_map_1.append('green')
        else:
            color_map_1.append('orange')

    nx.draw(G, node_color=color_map_1, with_labels=True, node_size=[(2.3**abs(hops_list[i]-max(hops_list.values()))) * 200 for i in G], style='dashdot')
    plt.savefig('foo.png')

main()