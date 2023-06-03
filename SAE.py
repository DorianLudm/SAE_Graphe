#%%
import networkx as nx
import json

def charger_resultats(nom_fichier):
    """charge un fichier de résultats au DNB donné au format CSV en une liste de résultats

    Args:
        nom_fichier (str): nom du fichier CSV contenant les résultats au DNB

    Returns:
        list: la liste des résultats contenus dans le fichier
    """
    #Initialisation
    liste_resultats = {}
    fic = open(nom_fichier, 'r')
    fic.readline()
    #Pour chaque ligne du fichier
    for ligne in fic:
        titrePresent = False
        dic_ligne = json.loads(ligne)
        dic_translated_ligne = {}
        #Pour chaque clé et valeur associé au dictionnaire de la ligne
        for(key,value) in dic_ligne.items():
            if key == "title":
                title_value = value
                titrePresent = True
            elif key != "year":
                value2 = []
                for elem in value:
                    elem2 = elem.replace("]]","").replace("[[","")
                    value2.append(elem2)
                dic_translated_ligne[key] = value2
            else:
                dic_translated_ligne[key] = value
        #Ajout au dictionnaire si et seulement si un titre a été identifier
        if titrePresent:
            liste_resultats[title_value] = dic_translated_ligne
    return liste_resultats

dic_Bacon = charger_resultats("data.json")



def getGraph(dic ,dir_Included=False):
    G = nx.Graph()
    i = 0
    bool = False
    for value in dic.values():
        if dir_Included:
            ensemble = set()
            for(key,item) in value.items():
                if key == "cast" or key == "directors":
                    for personne in item:
                        ensemble.add(personne)    
            for elem1 in ensemble:
                for elem2 in ensemble:
                    if elem1 != elem2:
                        G.add_edge(elem1,elem2)
        else:
            for elem1 in value["cast"]:
                for elem2 in value["cast"]:
                    if elem1 != elem2:
                        G.add_edge(elem1,elem2)
        
    return(G)

G = getGraph(dic_Bacon)



def collaborateurCommun(G, personne1, personne2):
    res = []
    for collab in G[personne1]:
        if collab in G[personne2] and collab != personne1:
            res.append(collab)
    return res

print(collaborateurCommun(G, "Joe Turkel", "Harrison Ford"))



def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    print(collaborateurs)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs

# def distance_acteur(G, act1, act2):
#     distance = 0
#     if act1 not in G.nodes() or act2 not in G.nodes():
#         return "Cette acteur est inconnu"
#     acteur = set()
#     acteur.add(act1)
#     while act2 not in acteur:
#         collaborateurs_directs = set()
#         for c in acteur:
#             for voisin in G[c]:
#                 if voisin not in acteur:
#                     collaborateurs_directs.add(voisin)
#         acteur = acteur.union(collaborateurs_directs)
#         distance += 1
#     return distance

# print(distance_acteur(G, 'Michael Caine','Brandon Maggart'))



def centralite_acteur(graph, acteur):
    visited = []
    queue = [acteur]
    i = -1
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            i += 1         
            for edge in graph.edges:
                if edge[0] == node:
                    queue.append(edge[1])
                elif edge[1] == node:
                    queue.append(edge[0])
    return i

def centralite(graph):
    ppc = 0
    acteur_res = ""
    centralite_a = 0
    for acteur in G.nodes():
        ppc = centralite_acteur(graph, acteur)
        break
    for acteur in G.nodes():
        centralite_a = centralite_acteur(graph, acteur)
        if centralite_a < ppc:
            ppc = centralite_a
             
lePlusAuCentre = centralite(G)



def plusGrandeDistanceEntreActeurs(graph):
    visited = []
    for acteur in G.nodes():
        depart = acteur
        break
    #On cherche un acteur sur l'extremite du graphe
    queue = [depart]
    node = depart
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)       
            for edge in graph.edges:
                if edge[0] == node:
                    queue.append(edge[1])
                elif edge[1] == node:
                    queue.append(edge[0])
    #On cherche la distance avec l'extremite la plus eloignee
    # queue2 = [node]
    # i = -1
    # while queue2:
    #     node2 = queue2.pop(0)
    #     if node2 not in visited:
    #         visited.append(node2)
    #         i += 1         
    #         for edge in graph.edges:
    #             if edge[0] == node2:
    #                 queue2.append(edge[1])
    #             elif edge[1] == node2:
    #                 queue2.append(edge[0])
    # return i
    return centralite_acteur(G, node)
# %%