# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")

init -10 python:
    from despin.abs import carac

    caracTest = carac.Carac("monId", "MaValeur")

label start:

# mise en place des caractéristiques et des objets
# la vraie initialisation du perso est dans perso_ldoelh.rpy
    show screen profil_joueur
    "Prends ça !"
    $ endurance.m_Valeur = endurance.m_Valeur - 5
    "Ouille"

    return
