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
    $ PerteEndurance(2)
    "En poussant un cri de douleur mêlé de rage, vous passez à l'offensive et vous décapitez votre agresseur d'un coup net et précis."
    "Vous vous préparez ensuite à attaquer ses compagnons, mais ces derniers se dispersent précipitamment et courent se réfugier au fond des bois."
    "Après avoir rapidement éteint les dernières flammes menaçantes, vous reprenez votre chemin."
    "Vous avez vaillamment défendu l'honneur du Shogun lors de cet affrontement, et vous pouvez par conséquent ajouter 1 point à votre propre Honneur."
    $ honneur.m_Valeur = honneur.m_Valeur + 1
    jump numero195

label numero8:
    "Alors que vous escaladez lentement le flanc de la montagne, une curieuse sensation, comme un picotement au cerveau, vous fait arrêter net."
    "En levant les yeux, vous voyez soudain un être impressionnant se dresser devant vous."
    show daioni at right
    with moveinright
    "C'est une créature d'apparence humaine, grande, musclée, revêtue d'une somptueuse armure d'or et d'argent."
    "Son visage est beau, les traits en sont purs et fins, mais c'est l'image même de la beauté du diable."
    "Dans ses yeux brille une flamme violette et il se dégage de tout son être une puissance et une malveillance insignes."
    "Vous êtes en présence d'un Dai-Oni, ou Grand Démon."
    d "Ainsi donc, mortel, vous voulez pénétrer au royaume d'Ikiru, Maître des Ombres ?"
    d "Pour y parvenir, il vous faudra tout d'abord me vaincre au Tournoi de l'Espace."
    hide daioni
    with moveoutright
    "Sur ces mots, le Dai-Oni disparaît brusquement dans un tonnerre de rires moqueurs et cruels."
    scene bg espace
    "Un étrange phénomène se produit alors : vous vous retrouvez subitement dans l'espace !"
    "Des myriades d'étoiles s'étendent à perte de vue, et la tête vous tourne à contempler cette immensité sans fin."
    "Vous avez l'impression d'être à la limite de la folie."
    "Lorsque vous reprenez vos esprits, vous constatez que vous êtes entouré de huit portes s'ouvrant sur chaque panneau d'une pièce octogonale ;"
    "le sol et le plafond, quant à eux, sont complètement transparents. La voix du Dai-Oni retentit à nouveau dans votre tête."
    d "Cet endroit s'appelle le Centre des Univers. Derrière chaque porte se trouve une puissante créature."
    d "Vous devrez essayer de gagner à votre cause le plus grand nombre de ces créatures afin de vous en faire des alliées car, lorsque vous serez prêt, vous devrez m'affronter, moi et mes propres alliés, en un combat mortel qui se déroulera dans l'Arène Hors du Temps."
    d "Si toutefois vous en sortez vainqueur, vous pourrez alors pénétrer dans le gouffre des Démons et accomplir votre destin au royaume d'Ikiru."
    d "A présent, que l'épreuve commence ! Puisse la malchance vous sourire et un millier de fléaux s'abattre sur vous !"
    "La voix tonitruante du Dai-Oni s'évanouit peu à peu dans l'espace, et vous vous retrouvez seul, égaré dans cette immensité silencieuse."
    "De toute évidence, vous n'avez pas le choix : il vous faudra, tôt ou tard, prendre part au Tournoi de l'Espace."
    "En inspectant les portes, vous remarquez qu'elles comportent toutes une inscription."
    menu:
        "Laquelle allez-vous ouvrir en premier :"
        "Le Pinacle des Hauteurs Suprêmes ?":
            jump numero30
        "Les-Anciennes plaines ?":
            jump numero68
        "Les Montagnes-de l'Ineffable Sainteté ?":
            jump numero66
        "le Désert-Eterne d akhon?":
            jump numero78
        "Le Marécage du Bourbier Originel ?":
            jump numero98
        "La Tour Eternelle ?":
            jump numero110
        "La Forêt Enchantée ?":
            jump numero126
        "L'Arène Hors du Temps ?":
            jump numero138

label numero9:
    "Battant rageusement l'air de vos bras, vous vous frayez un chemin hors du village et vous vous enfoncez rapidement dans les ténèbres."
    "Après la cuisante défaite que vous venez de leur infliger, les quelques survivants parmi les Rokuro-Kubi décident de vous laisser aller sans plus insister."
    "Vous avez survécu au village des Morts Vivants, c'est un exploit exceptionnel qui vous permet de gagner 1 point de CHANCE."
    $ GainDeChance(1)
    jump numero397

label numero10:
    "De village en village, vous poursuivez votre route à travers les diverses contrées du Tochimin."
    "Partout où vous passez, les gens s'inclinent avec respect en reconnaissant sur vous le sceau du Shogun — mais peut-être ont-ils également reconnu en vous l'illustre Senseï ?"
    "A cette distance de la capitale, le pays est encore tel qu'il l'a toujours été : calme et serein."
    "Après quelques jours de voyage, les habitations se font plus rares. Vous êtes maintenant sur les terres du seigneur Tsietsin et vous voyez dans le lointain s'élever une colonne de fumée."
    "En vous rapprochant, vous constatez qu'il s'agit d'un village incendié."
    "Cette vision éveille en vous une triste et amère réflexion : le Tochimin est décidément dans une bien pénible situation pour que des brigands puissent ainsi frapper impunément au coeur même du pays !"
    "Une piste poussiéreuse part de la route pour conduire au village."
    menu:
        "Si vous souhaitez aller inspecter le village de plus près":
            jump numero34
        "Si vous estimez que votre mission est trop urgente pour vous arrêter":
            jump numero24

label numero11:
    "Prétextant avoir oublié votre équipement à la sortie du village, vous annoncez aux anciens que vous devez vous absenter, mais que vous reviendrez dans un instant."
    "Les vieillards semblent contrariés de vous voir partir ; ils insistent pour vous retenir, à tel point qu'il vous faut les repousser et vous démener comme un beau diable pour parvenir à leur échapper."
    "Vous vous faufilez prestement derrière les maisons basses afin d'échapper à leurs regards inquisiteurs et, une fois hors de vue, vous vous dirigez furtivement vers l'enceinte du village."
    jump numero15

label numero12:
    # jouter un perso affiché "Tatsu!"
    t "Ainsi, s'exclame le Tatsu d'une voix tonitruante, tu as réussi à tenir bon jusqu'au Tournoi de l'Espace !"
    t "Je te félicite d'un tel exploit, mortel, et j'ai décidé de t'aider à combattre le Dai-Oni, car je souhaite moi aussi la défaite d'Ikiru, Maître des Ombres."
    t "Lorsque tu franchiras la porte de l'Arène Hors du Temps, je serai donc là pour me battre à tes côtés."
    "Sur ces mots, le Tatsu s'évanouit dans les airs. Il ne vous reste plus maintenant qu'à retourner au Centre des Univers en passant par la porte qui se trouve derrière vous."
    # N'oubliez pas de noter que vous avez gagné le Tatsu à votre cause
    # avant de revenir au 8 pour y choisir une nouvelle option
