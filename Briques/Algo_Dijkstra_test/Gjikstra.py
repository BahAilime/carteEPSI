import random
import heapq

# Fonction pour générer un graphe aléatoire
def generer_graphe(n, max_edges=4, max_poids=10):
    """
    Générer un graphe sous forme de dictionnaire avec des arêtes aléatoires et des poids aléatoires.
    - n: Nombre de nœuds du graphe
    - max_edges: Nombre maximum d'arêtes sortantes par nœud
    - max_poids: Poids maximum pour une arête
    Retourner un dictionnaire représentant le graphe.
    """
    graphe = {}  # Initialiser un dictionnaire vide pour stocker le graphe

    # Boucle pour chaque nœud
    for i in range(n):
        voisins = {}  # Créer un dictionnaire pour stocker les voisins d'un nœud

        # Déterminer le nombre aléatoire de voisins pour chaque nœud
        nb_voisins = random.randint(1, min(max_edges, n - 1))

        # Boucle pour ajouter des voisins aléatoires
        for _ in range(nb_voisins):
            voisin = random.randint(0, n - 1)
            while voisin == i or voisin in voisins:  # Éviter les boucles sur soi-même ou doublons
                voisin = random.randint(0, n - 1)

            # Assigner un poids aléatoire à l'arête
            poids = random.randint(1, max_poids)
            voisins[voisin] = poids  # Ajouter l'arête avec son poids

        # Assigner les voisins au nœud dans le graphe
        graphe[i] = voisins

    # Retourner le graphe généré
    return graphe


# Fonction pour implémenter l'algorithme de Dijkstra
def dijkstra(graphe, depart):
    """
    Trouver le plus court chemin depuis un nœud de départ vers tous les autres nœuds.
    - graphe: Dictionnaire représentant le graphe
    - depart: Nœud de départ
    Retourner les distances minimales de chaque nœud depuis le nœud de départ.
    """
    distances = {n: float('inf') for n in graphe}  # Initialiser les distances à l'infini pour tous les nœuds
    distances[depart] = 0  # Initialiser la distance du départ à 0

    # Créer une file de priorité pour gérer les nœuds à explorer
    file_priorite = [(0, depart)]

    # Boucle tant que la file n'est pas vide
    while file_priorite:
        distance_actuelle, noeud_actuel = heapq.heappop(file_priorite)  # Extraire le nœud avec la plus petite distance

        # Ignorer les distances non optimales
        if distance_actuelle > distances[noeud_actuel]:
            continue

        # Boucle à travers les voisins du nœud actuel
        for voisin, poids in graphe[noeud_actuel].items():
            distance_via_noeud_actuel = distance_actuelle + poids  # Calculer la distance via le nœud actuel

            # Si cette distance est plus courte, mettre à jour
            if distance_via_noeud_actuel < distances[voisin]:
                distances[voisin] = distance_via_noeud_actuel  # Mettre à jour la distance minimale
                heapq.heappush(file_priorite, (distance_via_noeud_actuel, voisin))  # Ajouter le voisin dans la file

    # Retourner les distances finales
    return distances


# Fonction principale pour exécuter le programme
def main():
    """
    Exécuter l'algorithme de Dijkstra sur un graphe généré aléatoirement.
    """
    n = 6  # Nombre de nœuds dans le graphe
    depart = 0  # Nœud de départ pour Dijkstra

    # Générer un graphe aléatoire
    graphe = generer_graphe(n)
    print("Graphe généré :", graphe)

    # Appliquer l'algorithme de Dijkstra
    distances = dijkstra(graphe, depart)
    print(f"Distances depuis le nœud {depart} : {distances}")


# Exécuter le programme principal
if __name__ == "__main__":
    main()
