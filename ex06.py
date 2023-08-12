"""
Exercice 6 : Modifier l'élément d'une liste imbriquée dans la liste suivante
"""

#definition de la fonction modifierElementDeListe avec ces parametres
def modifierElementDeListe(liste, ancienneValeur, nouvelleValeur):
    for i, element in enumerate(liste):
        #pour chaque element de la liste (position et element)
        if element == ancienneValeur:
            #si element egal à ancienne valeur devient alors nouvelle valeur
            liste[i] = nouvelleValeur
        elif isinstance(element, list):
            #sinon si element est sous-liste alors appelle de la fonction
            modifierElementDeListe(element, ancienneValeur, nouvelleValeur)
            
#exemple d'utilisation
maListe = [5, [10, 15, [20, 25, [30, 58], 40], 45], 50]
modifierElementDeListe(maListe, 58, 5800)
print(maListe)