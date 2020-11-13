# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define s = Character('Shogun', color="#580404")
define t = Character('Tatsu', color="#e30909")
define d = Character('Dai-Oni', color="#2b1323")

label start:

# mise en place des caractéristiques et des objets
# la vraie initialisation du perso est dans perso_ldoelh.rpy
    scene bg campagne_japonaise
    show screen profil_joueur
    # jump de test tmp ci après
    jump numero13
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
    "En tant que Samouraï du Shogun, l'Honneur est pour vous une vertu primordiale."
    "Vous commencez votre aventure avec 3 points d'Honneur."
    "Certains actes vous permettront d'augmenter votre Honneur, d'autres le réduiront."
    "De plus, votre Honneur aura une influence sur le déroulement des événements ;"
    "selon son niveau, vous serez à même d'entreprendre ou non certaines actions."
    "Si votre Honneur se trouve réduit à 0 au cours de votre mission, rendez-vous immédiatement au 99, et cela quels que soient les événements en cours."

label resume_debut_histoire:
    "L'empire du Titan se compose de trois continents principaux : l'Allansia, le Balkabad et le Khâl."
    "C'est sur la côte est du Khâl que s'étend le Tochimin ;"
    "cet état, bordé d'un côté par la mer et de l'autre par les montagnes, se trouve complètement isolé du reste du continent."
    "Le Tochimin a pour capitale Konichi et est gouverné par le Shogun Kihei Hasekawa."
    "Vous êtes un jeune Samouraï et vous avez fidèlement suivi l'enseignement du Bushido, la Voie du Guerrier, ainsi que le Kenjutsu, la Voie du Sabre."
    "Au Tochimin, nombreux sont ceux qui vous considèrent comme le sujet le plus habile et le plus valeureux de toute la garde du Shogun."
    "Cela vous a valu le titre de « Senseï », ou Maître du Sabre. Un jour, le Shogun vous convoque et vous informe d'une terrible nouvelle :"
    show shogun at right
    with moveinright
    s "Le Tochimin court un grand danger !"
    s "Je suis en train de perdre peu à peu le contrôle du pays, car certains seigneurs cherchent à se détacher de mon royaume afin de former des états indépendants ;"
    s "ceux qui ont rompu l'alliance complotent déjà contre moi."
    s "Par ailleurs, des hordes de bandits parcourent le pays en toute liberté et les envahisseurs barbares, connaissant notre faiblesse et notre isolement, ont déjà fait une incursion à nos frontières."
    s "Pourquoi en sommes-nous arrivés à cette dramatique situation ?"
    s "Eh bien, tout simplement parce que la Dai-Katana, la grande Épée connue sous le nom de Mort Joyeuse, m'a été dérobée !"
    s "Mort Joyeuse est une arme magique, réputée pour conférer de grands pouvoirs à son possesseur."
    s "On dit qu'elle est l'âme du Tochimin."
    s "Celui qui brandira Mort Joyeuse et saura en percer le secret pourra s'emparer du pays."
    s "Plusieurs seigneurs savent que je n'ai plus le droit de gouverner sans cette épée."
    s "Certains d'entre eux cherchent à s'en emparer pour eux-mêmes, mais d'autres ont déjà fait serment d'allégeance à celui qui la détient abusivement."
    s "En l'occurrence, le détenteur en question ne pourrait être pire : il s'agit d'Ikiru, Maître des Ombres ;"
    s "un chien sans âme qui se tapit au fin fond des montagnes, dans un repaire connu sous le nom d'Onikaru : le Gouffre des Démons."
    s "Maintenant que l Epée est en sa possession, les Bakemono-Sho et les Shikomes — deux races de guerriers sans foi ni loi — sont en train de se rassembler sous sa bannière."
    s "Je sais également qu'il a convoqué les Shuras, de redoutables guerriers-fantômes qui se cachent au plus profond du Gouffre, afin d'obtenir leur aide."
    s "Bientôt, s'il découvre le secret de l'Épée, Ikiru envahira notre beau pays, royaume de la douceur de vivre et des cerisiers en fleurs."
    s "Tu es animé du Senki, l'esprit de guerre, et c'est à toi, mon Senseï, que je confie cette mission : va à Onikaru, emporte la victoire sur Ikiru et rapporte-moi Mort Joyeuse."
    s "Cela sera loin d'être facile, car pour vaincre Ikiru et anéantir ses alliés sortis tout droit de Fenfer, il te faudra découvrir le secret de Mort Joyeuse."
    s "Je ne puis te le révéler moi-même, car il est écrit que celui qui dévoilera le mystère de son plein gré sera damné pour l'éternité, et Mort Joyeuse disparaîtrait à tout jamais du monde des hommes."
    s "Tu devras donc résoudre seul cette énigme."
    s "Je prierai les dieux pour qu'ils accordent le succès à ton entreprise et je m'adresserai tout particulièrement à Hotei, dieu de la Chance !"
    s "À présent, prends ceci : c'est le Sceau du Shogun, qui te permettra de traverser, sain et sauf, les régions qui me sont encore fidèles et loyales."
    hide shogun
    with Dissolve(.5)
    jump numero1

label mort:
    "Vous êtes mort."









    return
