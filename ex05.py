"""
Exercice 5 : Afficher les nombres d’une liste qui sont divisibles par 5
"""

#definition de la fonction afficherNombreDivisiblesPar5 avec liste en param
def afficherNombreDivisiblesPar5(liste):
    for nombre in liste:
        #pour tout nombre de la liste
        if nombre % 5 == 0:
            #si nombre modulo 5 egal à 0 alors afficher nombre divisible par 5
            print(nombre)

#exemple d'utilisation :
maListe = [1, 15, 20, 27, 30, 36, 40]
afficherNombreDivisiblesPar5(maListe)