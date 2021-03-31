import random
liste_animaux = ['lapin', 'chat', 'chien', 'chiot', 'dragon', 'ornithorynque']
print(liste_animaux)
# liste inversé
liste_animaux.reverse()
print(liste_animaux)
liste_animaux.sort()
print(liste_animaux)
liste_animaux.append('troll')
print(liste_animaux)

animdom = ['lapin', 'chat', 'chien', 'chiot']

for i in animdom:
    liste_animaux.remove(i)
    print(liste_animaux)
tableau_jeu=[]
for i in range(0,10):tableau_jeu.append(random.randint(1,10))
number = int(input("choisi un numéro entre 1 et 10 :"))
print(tableau_jeu)
if number in tableau_jeu:
    print("Gagné")
else:
    print("Perdu")
tableau_jeu=[]
for i in range(0,10):tableau_jeu.append(random.randint(1,10))
tableau_jeu.sort()
number = int(input("choisi un numéro entre 1 et 10 :"))
print(tableau_jeu)
if number in tableau_jeu:
    print("gagné")
elif i > number:
    print("Perdu")
else:
    print("perdu")