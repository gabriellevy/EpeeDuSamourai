label numero1:
    "Peu avant votre départ, vous rassemblez vos armes : votre katana (un long sabre) et votre wakizashi (un sabre court), puis vous revêtez votre armure et vous prenez soin d'emporter quelques Provisions."
    "Les gardes du Shogun vous saluent avec respect lorsque vous franchissez les portes de la ville."
    "Vous vous engagez ensuite sur la route du nord. Après avoir traversé les riantes contrées qui entourent la capitale, vous parvenez à un croisement."
    menu:
        "Désirez-vous aller"
        "vers l'ouest, puis au nord, en direction de la forêt des Ombres, du pont de Hagakure et ensuite vers les monts Shios'ii":
            jump numero10
        "vers l'est, en passant par les marais de Mizokumo, pour atteindre ensuite la montagne":
            jump numero29

label numero2:
    t "— A présent, mortel, écoute la première énigme :"
    t "Dans une forteresse sans porte ni fenêtre, Aux murs de marbre blanc comme neige, Tapissés d'une peau douce comme la soie, Au milieu d'une fontaine d'eau pure comme le cristal, Une pomme d'or, soudain,apparaît."
    t "De quoi s'agit-il donc ?"
    "Sur ces mots, le Tatsu vous contemple avidement, savourant à l'avance votre échec."
    $ reponseTatsu = renpy.input("De quoi s'agit-il donc ?")
    if reponseTatsu == "oeuf" or reponseTatsu == "Oeuf":
        jump numero47
    else:
        jump numero26

label numero3:
    "Les yeux jaunes du monstre le plus proche s'animent soudain d'une lueur d'intelligence quand vous vous inclinez en signe de rémission."
    "La créature s'empare alors de votre sabre sans que vous opposiez la moindre résistance, car vous savez pertinemment qu'il vous reste votre wakizashi."
    "Néanmoins, le katana était l'arme dans laquelle vous étiez le plus habile ; déduisez 1 point de votre total d'HABlLETÉ jusqu'à ce que vous trouviez un autre katana, ou bien Mort Joyeuse elle-même."
    $ aUnKatana = False
    $ CalculerHabilete()
    "Apparemment satisfaite de son acquisition, la créature vous fait signe de passer le gué."
    jump numero245

label numero4:
    "Vous dévalez l'escalier aussi vite que vous le pouvez."
    "Derrière vous, vous entendez les gardes lancés à votre poursuite, mais leurs pas s'arrêtent brusquement en haut des marches."
    "L'écho d'une voix accompagnée d'un rire moqueur vous parvient par la cage d'escalier :"
    "— Encore un que nous ne reverrons jamais ! Le Mukade s'en occupera, ha, ha, ha !..."
    "Malgré cette sinistre prédiction, vous repartez en courant ; puisqu'il vous est impossible de rebrousser chemin, autant affronter ce que le sort vous réserve."
    "Tout en bas des marches, un souterrain sombre et suintant d'humidité s'enfonce dans les ténèbres."
    menu:
        "Tentez votre Chance."
        "Lancer deux dés":
            $ texteResultatChance = TentezVotreChance()
    "[texteResultatChance]"
    if chanceux:
        jump numero16
    else:
        jump numero38

label numero5:
    "Intrigué par ce qui a pu causer la mort du vieux charbonnier, vous contournez le village avec circonspection, mais tout semble normal et paisible."
    "La nuit va bientôt tomber et les paysans rentrent des champs, fourbus de leur journée de labeur."
    "Sur la petite place du village, les anciens sont rassemblés devant la maison du chef."
    menu:
        "Si vous voulez aller demander l'hospitalité aux paysans":
            jump numero71
        "Si vous préférez vous joindre au groupe des vieux villageois":
            jump numero319

label numero6:
    "C'est pour vous un jeu d'enfant que de vous cacher dans la paille sans que le conducteur s'en aperçoive."
    "Peu après, vous entendez le garde s'adresser à lui, et les grandes portes de chêne commencent à s'ouvrir en gémissant."
    menu:
        "Tentez votre Chance."
        "Lancer deux dés":
            $ texteResultatChance = TentezVotreChance()
    "[texteResultatChance]"
    if chanceux:
        jump numero14
    else:
        jump numero28

label numero7:
    "Vous protégeant la tête de votre wakizashi, vous reculez prestement en recevant une pluie de brandons enflammés."
    "Malheureusement pour vous, une flammèche vient s'immiscer sous l'agrafe de votre armure et vous êtes gravement brûlé (vous perdez 2 points d'ENDURANCE)."
    $ endurance.m_Valeur = endurance.m_Valeur - 2
    "En poussant un cri de douleur mêlé de rage, vous passez à l'offensive et vous décapitez votre agresseur d'un coup net et précis."
    "Vous vous préparez ensuite à attaquer ses compagnons, mais ces derniers se dispersent précipitamment et courent se réfugier au fond des bois."
    "Après avoir rapidement éteint les dernières flammes menaçantes, vous reprenez votre chemin."
    "Vous avez vaillamment défendu l'honneur du Shogun lors de cet affrontement, et vous pouvez par conséquent ajouter 1 point à votre propre Honneur."
    $ honneur.m_Valeur = honneur.m_Valeur + 1
    jump numero195
