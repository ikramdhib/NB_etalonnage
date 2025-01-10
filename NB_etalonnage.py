import re

def calculerSommeValeurs(file_path):
    somme = 0
    with open(file_path, 'r') as fichier:
        for l in fichier:
           
            chiffres = re.findall(r'\d', l)
            if len(chiffres) >= 2:
                
                premierChiffre = int(chiffres[0])
                dernierChiffre = int(chiffres[-1])
                valeur = premierChiffre * 10 + dernierChiffre
                somme += valeur
    return somme

# Chemin du fichier
file_path = "D:\\TEST_TECH\\document.txt"

# Calcul et affichage du résultat
sommeTotale = calculerSommeValeurs(file_path)
print("Somme totale des valeurs d'étalonnage :", sommeTotale)