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
    # jump de test tmp ci après
    jump choix_discipline
    # sélection de la compétence de combat de base
    "En tant que Samouraï, vous êtes passé maître dans une des quatre disciplines décrites ci-après."
    "Au cours de l'aventure, il vous sera précisé, en temps voulu, d'utiliser la discipline dans laquelle vous excellez ou de prendre en considération les effets de cette discipline sur le déroulement d'un combat."
    "{b}Kyujutsu{/b} (Tir à l'Arc)"
    "Cette discipline vous permet d'ajouter un arc à votre équipement de Samouraï, ainsi qu'un jeu de 12 flèches de différentes sortes :"
    "trois flèches en bois de saule (infligeant à l'adversaire une perte de 2 points d'ENDURANCE),"
    "trois flèches-harpons (infligeant une perte de 3 points d'ENDURANCE),"
    "trois flèches perforantes (indispensables pour lutter contre certains adversaires et infligeant une perte de 2 points d'ENDURANCE)"
    "et trois flèches hurleuses (ne faisant perdre qu'un point d'ENDURANCE, mais produisant un sifflement effrayant)."
    "Pour savoir si vous avez atteint votre cible, jetez deux dés. Si le résultat obtenu est inférieur à votre HABILETE, vous avez touché votre adversaire."

    "{b}Iaijutsu{/b} (Art de dégainer le sabre et de frapper dans le même mouvement)"
    "Cette discipline vous permet de dégainer votre sabre et de porter un coup avec une rapidité fulgurante."
    "Cela signifie que vous blesserez automatiquement votre ennemi, quel que soit son niveau d'HABlLETÉ."
    "Votre victime perdra 3 points d'ENDURANCE à cette occasion, mais vous ne pourrez utiliser cette technique que lors du premier Assaut d'un combat."

    "{b}Karumijutsu{/b} (Saut Acrobatique)"
    "Cette discipline vous permet d'effectuer des bonds prodigieux avec une adresse et une facilité déconcertantes."
    "Vous serez informé des occasions où vous pourrez pratiquer cet art au cours de l'aventure."

    "{b}Ni-to-Kenjutsu{/b} combat à deux mains"
    "A la différence de l'escrime occidentale, l'escrime orientale se pratique avec un sabre que l'on manie à deux mains."
    "C'est une escrime de taille et non de pointe, telle qu'on l'exerce à l'épée."
    "Néanmoins, la maîtrise du Ni-to-Kenjutsu permet de se battre simultanément avec deux sabres : un katana (sabre long) et un wakizashi (sabre court)."
    "Grâce à cette discipline, si vous attaquez un adversaire et que vous obteniez 9 (ou plus) aux dés, vous aurez la possibilité d'enchaîner immédiatement sur une autre attaque, avant même que votre ennemi n'ait le temps de riposter"
    "(si vous obtenez 9 — ou plus — lors de cette seconde attaque, vous n'aurez toutefois pas le droit de passer à une troisième attaque !)."

label choix_discipline:
    menu:
        "Quelle discipline choisissez vous ?"
        "{b}Kyujutsu{/b} (Tir à l'Arc)":
            $ Kyujutsu()
            show screen fleches
        "{b}Iaijutsu{/b} (Art de dégainer le sabre et de frapper dans le même mouvement)":
            $ Iaijutsu()
        "{b}Karumijutsu{/b} (Saut Acrobatique)":
            $ Karumijutsu()
        "{b}Ni-to-Kenjutsu{/b} (Combat à deux mains)":
            $ NitoKenjutsu()

label description_honneur:
    "Discipline : [discipline]"











    return
