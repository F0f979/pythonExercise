"""
Exercice 4 : Afficher un mot en alternant entre majuscules et minuscules
"""

#definition de la fonction alternerMajusculesMinuscules avec le mot en param
def alternerMajusculesMinuscules(mot):
    resultat = ""
    #pour chaque element du mot(position, lettre)
    for i, lettre in enumerate(mot):
        if i % 2 == 0:
            #si la position de la lettre est divisble par 2 alors lettre en maj
            resultat += lettre.upper()
        else:
            #sinon lettre en minus
            resultat += lettre.lower()
    #return resultat
    return resultat
    
#exemple d'utilisation :
mot = "fofana"
motAlterne = alternerMajusculesMinuscules(mot)
print(motAlterne)