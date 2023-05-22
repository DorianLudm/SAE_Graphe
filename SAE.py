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

def draw_Graph(dic, nb_film ,dir_Included=False):
    G = nx.Graph()
    i = 0
    for value in dic.values():
        if i < nb_film:
            i += 1
        else:
            break
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
        
    nx.draw(G)

draw_Graph(dic_Bacon, 50, True)
# %%
