#exercice1 :

def est_bissextile(annee):
    if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
        return f"L'année {annee} est bissextile."
    else:
        return f"L'année {annee} n'est pas bissextile."


print(est_bissextile(2008))  # Résultat : L'année 2008 est bissextile.
print(est_bissextile(1900))  # Résultat : L'année 1900 n'est pas bissextile.
print(est_bissextile(2000))  # Résultat : L'année 2000 est bissextile.
 

#exercice2 :
import random

def lancer_deux_des():
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
    somme = de1 + de2
    return somme

def lancer_des(nombre_des):
    somme = 0
    for _ in range(nombre_des):
        resultat = random.randint(1, 6)
        somme += resultat
    return somme

# Question 2.1
resultat_deux_des = lancer_deux_des()
print("Résultat du lancer de deux dés :", resultat_deux_des)

# Question 2.2
resultat_deux_des2 = lancer_des(2)
print("Résultat du lancer de deux dés :", resultat_deux_des2)

resultat_trois_des = lancer_des(3)
print("Résultat du lancer de trois dés :", resultat_trois_des)

#exercice3
def afficher_suite_carres(n):
    carres = [str(i**2) for i in range(n+1)]
    suite_carres = " − ".join(carres)
    print(suite_carres)

n = int(input("Entrez un entier n : "))
afficher_suite_carres(n)

#exercice4
def produit(n1, n2):
    resultat = 1
    for i in range(n1, n2+1):
        resultat *= i
    return resultat

n1 = int(input("Entrez la valeur de n1 : "))
n2 = int(input("Entrez la valeur de n2 : "))
resultat = produit(n1, n2)
print("Le produit des entiers de", n1, "à", n2, "est :", resultat)

#exercice5
def nbPairImpair(tableau):
    nb_pair = 0
    nb_impair = 0

    for element in tableau:
        if element % 2 == 0:
            nb_pair += 1
        else:
            nb_impair += 1

    return nb_pair, nb_impair

tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15]
resultat = nbPairImpair(tableau)
print("Nombre d'éléments pairs :", resultat[0])
print("Nombre d'éléments impairs :", resultat[1])

#exercice6
def decaleCircDroite(tableau):
    dernier_element = tableau[-1]
    decalage = [dernier_element] + tableau[:-1]
    return decalage

tableau = [12, 21, 10, 11, 0, 1, 4, 9, 25]
print("Avant décalage circulaire à droite :", tableau)
resultat = decaleCircDroite(tableau)
print("Après décalage circulaire à droite :", resultat)

#Exercice 7
#7.1
def bin2Dec(nBin):
    nDec = int(nBin, 2)
    return nDec

nBin = '10000001'
nDec = bin2Dec(nBin)
print('Le nombre binaire (code entier naturel) ' + str(nBin) + ' se convertit en base 10 : ' + str(nDec))

#7.2
def dec2Bin(nDec):
    nBin = bin(nDec)[2:]
    return nBin

nDec = 126
nBin = dec2Bin(nDec)
print('Le nombre décimal ' + str(nDec) + ' se convertit en base 2 : ' + str(nBin))

#exercice8
def calculerSomme(n):
    if n == 1:
        return 1
    else:
        return n + calculerSomme(n-1)

# Exemple d'utilisation de la fonction
n = int(input("Entrez la valeur de n : "))
resultat = calculerSomme(n)
print("La somme des", n, "premiers entiers est :", resultat)

#exercice 9
def calculerPuissance(x, n):
    if n == 0:
        return 1
    else:
        return x * calculerPuissance(x, n-1)

# Exemple d'utilisation de la fonction
x = float(input("Entrez la valeur de x : "))
n = int(input("Entrez la valeur de n : "))
resultat = calculerPuissance(x, n)
print(x, "élevé à la puissance", n, "est égal à :", resultat)

#exercice 10
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Entrez la valeur de n : "))
resultat = fibonacci(n)
print("Le terme de la suite de Fibonacci à l'indice", n, "est :", resultat)

#exercice 11
tableau = list(range(1, 51))
resultat = ';'.join(map(str, tableau))
print(resultat)

#exercice 12
import random

def echang(tableau, index1, index2):
    temp = tableau[index1]
    tableau[index1] = tableau[index2]
    tableau[index2] = temp

def tri_tab(tableau):
    n = len(tableau)
    for i in range(n-1):
        for j in range(n-i-1):
            if tableau[j] > tableau[j+1]:
                echang(tableau, j, j+1)

tableau = [random.randint(1, 100) for _ in range(10)]

print("Tableau initial :", tableau)

tri_tab(tableau)

resultat = ', '.join(map(str, tableau))
print("Tableau trié :", resultat)

#exercice 13
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

nbr = 20
result = factorielle(nbr)
print("La factorielle de", nbr, "est :", result)

#exercice14
import random

def gnrphrase(tableau):
    random.shuffle(tableau)
    phrase = ' '.join(tableau)
    print(phrase)

mots = ['Bonjour', 'à', 'tous', 'les', 'amis']
gnrphrase(mots)