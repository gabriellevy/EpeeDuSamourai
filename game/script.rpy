# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")

init python:
    from despin.abs import *

    testInitUn = "hahahaha"
    caracTest = carac.Carac("monId", "MaValeur")

# Le jeu commence ici
label start:

    python:
        testUn = 8

    e "On commence : [testUn]"
    e "Suite init : [testInitUn]"
    e "Suite carac : [caracTest.m_Valeur]"

    return
