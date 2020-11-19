label numero41:
    if discipline.m_Valeur == disciplineKarumijutsu:
        menu:
            "Si vous utilisez l'art du Karumijutsu pour sauter par-dessus vos agresseurs":
                jump numero35
            "Sinon":
                jump numero41_suite
label numero41_suite:
    "[discipline.m_Valeur]"
    "Vous vous voyez contraint de vous mettre en position de défense pour parer leurs redoutables attaques."
    "Fouettant rageusement l'air à grands coups de sabre, vous parvenez à résister pendant quelque temps, comme si une barrière magique, formée d'un millier de lames tournoyantes, faisait écran entre vous et vos adversaires."
    "Mais hélas ! l'ennemi arrive de tous côtés ; l'un deux réussit à percer votre garde et à vous donner un violent coup de griffe."
    $ PerteEndurance(2)
    jump numero129

label numero42:
    "Le dragon tombe à la renverse en agonisant. Puis son corps se volatilise sous vos yeux, comme s'il n'avait jamais existé."
    "Autour de vous, la forêt semble avoir perdu son aura de sorcellerie."
    "Sans perdre un instant, vous vous remettez en marche et vous traversez la clairière pour continuer à suivre le sentier."
    jump numero82

label numero43:
    "La déférence que l'on marque en général aux gens de votre caste semble malheureusement faire défaut aux habitants de ces hauts plateaux."
    "Ce sont pour la plupart des charbonniers au visage noirci par la suie."
    "L'un d'eux, sensiblement plus jeune que les autres, reconnaît le fanion qui flotte dans votre dos et lance ironiquement à la cantonade :"
    ch "-Regardez, les amis, voilà le Senseï du faux Shogun ! Où est donc passée l'Épée de ton maître, et que fait-il donc sans elle ?"
    ch "Hasekawa — que dieu bénisse son crâne d'oeuf ! — n'est plus Shogun ; et toi, tu n'as donc plus de maître : tu n'es qu'un ronin !"
    "Les ronins sont des samouraïs qui ne sont plus au service d'aucun seigneur et qui ont, par conséquent, perdu leur statut."
    "En proférant de telles ignominies, ce paysan vous a bafoués, vous et votre Shogun."
    "Conscients de la gravité de l'insulte, les autres charbonniers s'empressent de lui dire de se calmer."
    menu:
        "Si vous désirez punir ce jeune insolent":
            jump numero59
        "Si vous préférez passer votre chemin comme si de rien n'était":
            jump numero77

label numero44:
    "Vous interpellez le cavalier et, au nom de Kihei Hasekawa, vous le sommez de vous dire de quoi il retourne."
    "Le samouraï amène son cheval au petit galop et vous crie :"
    "-Ce n'étaient que des pillards ! A présent, je dois m'en retourner à la forteresse du seigneur Tsietsin."
    "Mais soudain, alors qu'il n'est plus qu'à quelques mètres de vous, le cavalier éperonne à nouveau sa monture et se rue sur vous en brandissant sa lance."
    "Cette attaque inopinée vous prend au dépourvu : la lance vous transperce le bras et vous perdez 3 points d'ENDURANCE. Combattez ce traître :"
    $ PerteEndurance(3)
    $ nouveauCombat(True)
    $ AjouterEnnemi("CAVALIER SAMOURAÏ", 8, 9)
    $ CommencerCombat("numero72")

label numero45:
    "Vous parvenez à gagner le bout du village, mais vous vous trouvez bloqué dans une impasse, juste en face d'une petite maison."
    "Celle-ci ne semble pas très solide et, d'un formidable coup d'épaule, vous ouvrez une brèche dans le mur."
    "Cela vous permet de gagner du temps sur les têtes ennemies qui continuent à voler par-dessus les toits."
    "Lorsque vous ressortez de l'autre côté de la masure, vous ne trouvez que quelques Rokuro-Kubi pour vous accueillir, mais il vous faut en finir avec eux :"
    $ nouveauCombat(True)
    $ AjouterEnnemi("ROKURO-KUBI", 8, 8)
    $ CommencerCombat("numero9")

label numero46:
    "Vous chargez votre arc d'une flèche-harpon, puis vous visez avec une extrême précision, afin de tuer les Shikomes le plus vite possible."
    menu:
        "Testez votre habileté."
        "Jetez deux dés.":
            $ texteResultatHabilete = TentezVotreHabilete()
    "[texteResultatHabilete]"
    if habile_:
        jump numero236
    else:
        jump numero248

label numero47:
    "Le Tatsu semble fort déconcerté."
    t "-Un oeuf. Oui, c'est exact, mortel, vous dit-il d'une voix contrariée."
    "Puis son regard s'anime à nouveau d'une lueur vorace : Mais seras-tu assez malin pour trouver la bonne réponse deux fois de suite ? Ecoute donc la seconde énigme :"
    t "Quand on ne sait pas ce que c'est, \nC'est quelque chose ; Mais quand\non sait ce que c'est, Alors ce n'est\n plus rien."
    $ reponseTatsu = renpy.input("Votre réponse ?")
    if reponseTatsu == "énigme" or reponseTatsu == "Énigme" or reponseTatsu == "Enigme":
        jump numero52
    else:
        jump numero26

label numero48:
    "L'étrange femme vous regarde d'un air narquois."
    menu:
        "Quel objet allez-vous choisir pour tenter de la gagner à votre cause ?"
        "Un cor ?":
            jump numero86
        "Une fiole d'eau provenant de la source du Grand Savoir ?":
            jump numero96
        "Un Casque de Confusion ?":
            jump numero114
        "Si vous ne possédez aucun de ces objets":
            jump numero130

label numero49:
    "Vous vous jetez dans la blancheur écumeuse de la rivière pour apercevoir — hélas ! un peu tard — que les monstres ont eu la malignité de disposer des pieux acérés, juste sous la surface des eaux."
    "Vous vous empalez dessus et vous perdez 7 points d'ENDURANCE."
    $ PerteEndurance(7)
    "Si vous êtes toujours en vie, vous réussissez à vous extirper péniblement des pieux et vous gagnez la rive opposée, le corps transpercé en de multiples endroits."
    jump numero395

label numero50:
    show screen fleches
    "La puanteur devient de plus en plus forte."
    "Vous débouchez finalement dans une grande caverne baignée d'une lumière blafarde, sans que vous puissiez toutefois en déceler l'origine."
    "Le sol est jonché d'ossements, de vêtements en lambeaux et d'armes rongées par la rouille."
    "Soudain, vous repérez d'où vient la lumière : une silhouette phosphorescente avance sur vous !"
    "Vous apercevez tout d'abord une gueule béante, bordée de dents tranchantes qui s'entrechoquent nerveusement."
    "D'énormes yeux, tels deux disques noirs inscrutables, vous fixent méchamment."
    "Le corps de la créature, quant à lui, est formé de segments osseux portés par de multiples pattes qui s'agitent frénétiquement."
    "La peau du monstre est d'une blancheur laiteuse et malsaine : c'est elle qui diffuse la lumière qui vous avait tant intrigué."
    "Vous êtes en présence d'un Mukade, une espèce de mille-pattes géant de plusieurs mètres de long."
    "Il avance inexorablement vers vous, et il est évident que vous représentez pour lui un mets de choix !"

    $ enduranceMukade = 20
    $ tirsArcPossibles = 2
label numero50_tir_arc:
    if disciplineKyujutsu == discipline.m_Valeur and tirsArcPossibles > 0 and ADesFleches():
        $ degatsFleche = 2
        menu:
            "Décocher une flèche de saule au monstre" if flechesSaule.m_Valeur > 0:
                $ flechesSaule.m_Valeur = flechesSaule.m_Valeur - 1
                $ degatsFleche = 2
            "Décocher une flèche-harpon au monstre" if flechesHarpon.m_Valeur > 0:
                $ flechesHarpon.m_Valeur = flechesHarpon.m_Valeur - 1
                $ degatsFleche = 3
            "Décocher une flèche perforante au monstre" if flechesPerforantes.m_Valeur > 0:
                $ flechesPerforantes.m_Valeur = flechesPerforantes.m_Valeur - 1
                $ degatsFleche = 2
            "Décocher une flèche hurleuse au monstre" if flechesHurleuses.m_Valeur > 0:
                $ flechesHurleuses.m_Valeur = flechesHurleuses.m_Valeur - 1
                $ degatsFleche = 1

        $ tirArc1 = LancerDeuxDes()
        "Vous obtenez [tirArc1]."
        if tirArc1 < habilete.m_Valeur:
            "C'est inférieur à votre habileté de [habilete.m_Valeur]. La créature est blessée."
            $ enduranceMukade = enduranceMukade - degatsFleche
        else:
            "C'est supérieur à votre habileté de [habilete.m_Valeur].Vous l'avez ratée."

        $ tirsArcPossibles = tirsArcPossibles - 1
        jump numero50_tir_arc

    $ nouveauCombat(True)
    $ AjouterEnnemi("MUKADE", 7, enduranceMukade)
    $ CommencerCombat("numero62")






















# --------------youpi
