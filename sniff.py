#####################################################
# Date : 21/06/2023
# Author : Amandine
#
# Descritption : script d'analyse des paquet reçus sur le réseau
######################################################

from scapy.all import *


def f_icmp_detect(paquet):
    if paquet.haslayer(ICMP):
        print("paquet ICMP détecté !")
        print(paquet[IP].src)
conf.iface="lo"
sniff(prn=f_icmp_detect)