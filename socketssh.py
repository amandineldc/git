#####################################################
# Date : 17/03/2023
# Author : Amandine
#
# Descritption : Script permettant de découvrir des hôtes sur le réseau avec le port SSH ouvert
######################################################
import socket

############################################
# Descrition fonction f_connect : Dans ce script, la fonction f_connect prend en paramètres l'adresse IP et le port à scanner, et tente de se connecter au service SSH en utilisant la bibliothèque socket de Python.
# Si une connexion est établie avec succès, la fonction récupère la bannière SSH et la renvoie sous forme de chaîne de caractères, avec le port et l'adresse IP correspondants.
############################################

def f_connect(ip, port):
    s = socket.socket()
    s.settimeout(5)
    try:
        s.connect((ip, port))
        banner = sock.recv(1024)
        return banner, port, ip
    except:
        return None
    s.close()
############################################
# Description fonction scan_ports : La fonction scan_ports utilise la fonction f_connect pour scanner plusieurs ports et récupérer les bannières SSH correspondantes.
# Elle renvoie une liste de tuples (=liste d'éléments entouré de parenthèses) contenant les bannières, les ports et les adresses IP correspondants.
############################################

def scan_ports(ip, ports):
    banners = []
    for port in ports:
        banner = f_connect(ip, port)
        if banner:
            banners.append(banner)
    return banners

#############################################
# VARIABLES
############################################

ip = "192.168.56.103"
ports = [22, 21]
banners = []
p = 0

#############################################
# Description boucles while et for : Dans la boucle while, nous parcourons la liste des ports à scanner, en appelant la fonction get_ssh_banner pour chaque port.
# Si une bannière SSH est trouvée, elle est ajoutée à la liste des bannières.
# Enfin, le script affiche la liste des bannières SSH trouvées avec les ports correspondants en utilisant une boucle for.
#############################################

while p < len(ports):
    banner = f_connect(ip, ports[p])
    if banner:
        banners.append(banner)
    p += 1
print("[X] - IP : " + ip + " - port " + str(ports) + " : " + str(f_connect(ip, ports)))

print(f"SSH banners found on {ip}:")
for banner in banners:
    print(f"Port {banner[1]}: {banner[0]}")
    print("[X] - IP : " + ip + " - port " + str(ports) + " : " + str(f_connect(ip, ports)) + str(banner))