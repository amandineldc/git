
from random import randrange
just_number = randrange(0, 50)
import math
wallet = 500
mise = 0
arret = "n"
print("Bienvenu au CASINO !\nVotre porte-monnaie est composé de " + str(wallet) + "euros")

while just_number in range(0, 50) and arret == "n":
    number = int(input("Quel numéro choisissez-vous entre 0 et 49 ? "))
    if number not in range(0, 50):
        print("choisi entre 0 et 49 !")
    else:
        mise = int(input("Quelle est votre mise ? "))
        wallet = wallet - mise
        print("Le numéro gagnant est le :" + str(just_number))
        if number == just_number:
             wallet = wallet + mise + mise*3
             print("Bravo vous avez trouvé le bon numéro, vous avez gagné " + str(mise*3) + "votre porte-monnaie est de " + str(wallet))
             arret = input(print("voulez vous arrêter o/n ? "))
        elif (just_number % 2 == 0) and (number % 2 == 0):
             wallet = math.ceil(wallet + mise + mise/2)
             print("Votre numéro est de la même couleur que le numéro gagnant. Vous avez gagné " + str(mise/2) + " Votre porte-monnaie est de " + str(wallet))
             arret = input(print("voulez vous arrêter o/n ? "))
        else:
             print(("Vous avez perdu votre mise. Votre porte-monnaie est de " + str(wallet)))
             if wallet == 0:
                 break
             arret = input(print("voulez vous arrêter o/n ? "))

if arret == "o":
    print("Merci, à la prochaine fois")





