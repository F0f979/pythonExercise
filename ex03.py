"""
Exercise 3: Lire un fichier texte dans une variable et remplacer toutes les 
nouvelles lignes par des espaces
"""

#definition de la fontion remplacerLignesParEspaces avec nomFichier en arg
def remplacerLignesParEspaces(nomFichier):
    contenu = ""
    try:
        #ouvrir le fichier en lecture si trouve
        with open(nomFichier, 'r') as fichier:
            #lire le fichier dans contenu et remplace ligne par espace 
            contenu = fichier.read()
            contenu = contenu.replace("\n", " ")
        fichier.close()
    except FileNotFoundError:
        #ecris message si fichier pas trouve
        print(f"Le fichier '{nomFichier}' n'a pas été trouvé.")
    #reourne le contenu du fichier
    return contenu
    
#exemple d'utilisation
nomFichier = 'fichier.txt'
contenuRemplace = remplacerLignesParEspaces(nomFichier)
print(contenuRemplace)