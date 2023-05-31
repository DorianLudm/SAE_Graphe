# SAE 2.02 : Exploration algorithmique d'un problème informatique
# A la conquête d'Hollywood

## Exercice 2 : Collaborateurs communs

a. Comment exprimeriez-vous cette notion (ensemble de collaborateurs en commun) en termes de théorie des graphes ?

b. Pouvez-vous donner une borne inférieure sur le temps nécessaire à l'exécution de votre fonction ?

## Exercice 3 : Collaborateurs proches

a. Reconnaissez-vous l'algorithme classique en théorie des graphes qui est au coeur de ce programme ?

b. Grâce à la fonction précédente, comment pouvez-vous déterminer si un acteur se trouve à distance k d'un autre acteur ?

c. Tentons maintenant de déterminer la distance entre deux acreurs. Est-ce que réutiliser la fonction précédente vous semble intéressant ? Donnez la complexité d'un tel algorithme.

d. Comment pouvez-vous maintenant modifier la fonction qui vous a été fournie afin de trouver la distance entre deux acteurs ?

e. Donnez la complexité d'un tel algorithme.

## Exercice 4 : Qui est au centre d'Hollywood ?
On cherche maintenant à déterminer la centralité d'un acteur. Pour cela, on veut déterminer la plus grande distance qui le sépare d'un autre acteur dans le graphe.


a. Quelle notion de théorie des graphes permet de modéliser cela ? Proposez une fonction qui calcule la centralité d'un acteur dans Gc.
    Le parcours en profondeur pourrait aider à modéliser la plus grande distance entre deux acteurs dans un graphe.


b. A l'aide de la fonction précédente, écrivez une autre fonction qui va déterminer l'acteur le plus central du graphe Gc.

Plus formellement notons $c(G,v)$ la centralité d'un acteur v. Dans ce cas, le centre du graphe est un sommet s tel que $c(G,s)= \min{c(G,v)}, v \in V(G)$


## Exercice 5 : Une petite famille
Nous allons maintenant tenter de déterminer si deux acteurs peuvent être très éloignés dans Gc. Plus précisément, vous fournirez une fonction permettant de déterminer la distance maximum dans Gc entre toute pare d'acteurs/actrices.

- Est-ce que ce nombre est bien inférieur ou égal à 6 pour le jeu de données fourni ?

## Exercice 6 : (Bonus)

a. Proposez une méthode similaire à celle calculant le centre du graphe mais qui se restrint ici à déterminer le centre d'un groupe d'acteur (On remarquera qu'un tel sommet ne fait nécessairement partie du groupe en question).

b. Faites en sorte, queand cela a du sens, que vos fonctions renvoient un sous-graphe de Gc plutôt qu'une simple liste d'acteurs. Par exemple, proposer une vatiante de la fonction déterminant les collaborateurs proches d'un sommet $v$ qui renverra le sous-graphe induit par $v$ et par tous les sommets à distance $k$ de $v$.

## Exercice 7 : Un peu d'efficacité
L'efficacité de l'ensemble de vos méthodes, tant sur le temps d'exécution que sur la mémoire utilisée, est bien entendu essentielle. Par exemple, calculer la distance entre 2 sommets peut se faire de différentes manières, comme évoqué précédemment, impliquant des temps de calcul différents. Il est égaliement possible de pré-calculer un certain nombre de distance et d'utiliser ces informations pour calculer des distances entre des paires de sommets plus éloignés. Pour cette dernière partie du travail, vous vous attacherez donc à proposer différentes implémentations du calcul de distance et à évaluer ces différentes propositions. La description de vos évaluations expérimentales ainsi que vos conclusions devront apparaître dans votre rapport.