#exo1 : Write a Python program to convert temperatures to and from celsius, fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
print("---MENU---\n1) °C en °F\n2) °F en °C\nPour quitter tape 0")
menu=int(input("Fais un choix :"))
if menu == 1:
    C = int(input(print("Entre une température en °C : ")))
    F = (C*1.8)+32
    print("ça équivaut à " + str(F))
    print("---MENU---\n1) °C en °F\n2) °F en °C")
    menu = int(input("Fais un choix :"))
elif menu == 2:
    F = int(input(print("Entre une température en °F : ")))
    C = (F - 32) / 1.8
    print("ça équivaut à " + str(C))
    print("---MENU---\n1) °C en °F\n2) °F en °C")
    menu = int(input("Fais un choix :"))
elif menu == 0:
    print("EXIT")
else:
    print("choisi 1 ou 2")
    menu = int(input("Fais un choix :"))

#exo2
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dictot = {**dic1, **dic2, **dic3}
print(dictot)

#exo3

from datetime import datetime

dt = datetime.now()
print("current date and time :" + str(dt))

#exo4
color_list = input("Entre une liste : ")
#color_list = ["Red", "Green", "White", "Black"]
print("la première couleur est " + color_list[0] + ". La dernière couleur est " + color_list[-1])

#exo5



