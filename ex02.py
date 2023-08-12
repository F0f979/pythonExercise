"""
Exercice 2 : Calculer la factorielle d’un nombre
Codez un programme qui donne la factorielle d’un nombre.
"""

#definition de la fonction calculerFactoriel ave n pour nombre
def calculerFactoriel(n):
    if n == 0 or n == 1:
        #retourne 1 si le nombre est 1 ou 0
        return 1
    else:
        #retourne nombre multiplie par le factoriel du nombre qui le precede
        return n * calculerFactoriel(n - 1)
        
# exemple d'utilisation :
nombre = 5
resultat = calculerFactoriel(nombre)
print("Le factoriel de {} est {}".format(nombre, resultat))