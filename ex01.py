"""
Exercice 1 : Renverser l’ordre des éléments d’une liste
Créez un programme qui change l’ordre des éléments d’une liste en les 
renversant.
"""

#definition de la fonction renverserListe avec liste en parametre 
def renverserListe(liste):
    #retourne la liste dans l'ordre inverse avec [::-1]
    return liste[::-1]
    
#exemple d'utilisation
maListe = [1, 2, 3, 4, 5]
listeInverse = renverserListe(maListe)
print(listeInverse)