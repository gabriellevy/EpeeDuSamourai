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

label numero51:
    "Vous observez attentivement Ikiru. Celui-ci appelle d'autres créatures diaboliques à la rescousse puis, sur un signe, il les lance à l'attaque."
    "Chacune d'elles est une masse informe et ténébreuse qui tentera de vous étouffer."
    "Vous allez devoir affronter, l'une après l'autre, dix de ces abominables entités."
    "Cependant, chaque fois que vous en frapperez une avec succès, Mort Joyeuse l'irradiera de son éclat magique et la détruira immédiatement."
    $ nouveauCombat(True)
    $ AjouterEnnemi("Première Ombre", 9, 1)
    $ AjouterEnnemi("Deuxième Ombre", 9, 1)
    $ AjouterEnnemi("Troisième Ombre", 9, 1)
    $ AjouterEnnemi("Quatrième Ombre", 9, 1)
    $ AjouterEnnemi("Cinquième Ombre", 9, 1)
    $ AjouterEnnemi("Sixième Ombre", 9, 1)
    $ AjouterEnnemi("Septième Ombre", 9, 1)
    $ AjouterEnnemi("Huitième Ombre", 9, 1)
    $ AjouterEnnemi("Neuvième Ombre", 9, 1)
    $ AjouterEnnemi("Dixième Ombre", 9, 1)
    $ CommencerCombat("numero121")

label numero52:
    "En entendant votre réponse, le Tatsu se raidit de sur-prise, puis il laisse exploser sa fureur :"
    t "-Une énigme, oui ! Maudit sois-tu, mortel !"
    "Pendant un instant, vous croyez qu'il va vous attaquer, mais il parvient à surmonter son courroux et reprend d'un ton plus calme :"
    t "-Tu as passé l'épreuve avec succès et tu es libre, maintenant, de t'en aller."
    t "Cependant, avant de partir, écoute bien ce que je vais te dire."
    t "Si tu participes un jour au Tournoi de l'Espace, et s'il advenait, par extraordinaire, que tu l'emportes sur le Dai-Oni, invoque le Jizo des Démons en prononçant cette incantation :"
    t "« Un Shura est là, O Jizo ! Viens pour exécuter ton dessein »."
    "Vous laissant sur ces paroles laconiques, le Tatsu reprend les airs et disparaît."
    hide tatsu
    with moveouttop
    "À sa place, vous trouvez un talisman en jade représentant un dragon."
    "Vous vous baissez pour le ramasser, puis vous l'examinez attentivement : c'est un Talisman de Circonstances Fortuites qui vous permet d'ajouter 2 points à votre total de CHANCE."
    $ GainChance(2)
    "Satisfait de votre trouvaille, vous reprenez votre marche à travers les bois"
    jump numero82

label numero53:
    "Tournant le dos aux eaux écumeuses, vous levez votre sabre, mais, ce faisant, vous perdez l'équilibre et vous glissez sur le limon."
    "Votre lame frôle de peu la tête du monstre et celui-ci vous plante ses crocs dans le bras."
    "Vous perdez 4 points d'ENDURANCE."
    $ PerteEndurance(4)
    "La créature écailleuse se jette sur vous et, d'un violent coup de patte, vous précipite dans l'eau comme si vous n'étiez qu'une vulgaire poupée de son."
    "Malheureusement pour vous, des pieux acérés affleurent à la surface !"
    "Vous vous empalez dessus et vous perdez de nouveau 4 points d'ENDURANCE."
    $ PerteEndurance(4)
    "Vous vous extirpez tant bien que mal de ces pieux et, porté par le courant, vous gagnez péniblement la rive opposée, le corps meurtri et le moral à zéro."
    jump numero395

label numero54:
    "Vous avez vaincu le Dai-Oni ! Ce dernier gît à vos pieds et sa vie ne tient plus qu'à un fil."
    "Peu à peu, les ombres fantomatiques quittent l'Arène."
    "Quand vous restez seul à seul avec votre adversaire, vous l'entendez murmurer avec peine :"
    d "— Tu as gagné, mortel, et je suis tenu, par les lois célestes qui régissent le Tournoi de l'Espace, de t'accorder une seule et unique question."
    menu:
        "Qu'allez-vous demander au Dai-Oni :"
        "Quel est le secret de Mort Joyeuse ?":
            jump numero206
        "Comment vaincre Ikiru, Maître des Ténèbres ?":
            jump numero188
        "Pouvez-vous m'aider à accomplir ma mission et anéantir Ikiru ?":
            jump numero150

label numero55:
    "Le magicien se dresse encore sur votre chemin et vous dit, le visage rayonnant de joie :"
    m "-Vous avez fait le bon choix, jeune samouraï, et vous serez bientôt au bout de vos peines."
    "En vous voyant avancer vers la gueule béante et les ailerons aciculaires du Dragon des Mers, la prêtresse se met à trembler d'effroi et le magicien, quant à lui, disparaît de nouveau."
    "Le monstre rejette la tête en arrière et crache un torrent d'eau bouillante sur la prêtresse et vous."
    "La brûlure est intolérable et, avant que vous ne perdiez conscience, vous entendez la jeune femme hurler de terreur à l'approche du monstre qui va tous deux vous dévorer."

label numero56:
    "Le cavalier samouraï sursaute en vous apercevant, puis il s'écrie :"
    "-Mais voilà cette chiffe molle, le laquais du soi-disant Shogun Kihei Hasekawa ! Longue vie au nouveau Shogun, Tsietsin-Sama !"
    "Sur ce, il passe à l'attaque et vous charge en brandissant sa lance."
    "Ainsi donc, le seigneur Tsietsin a rejoint le camp des traîtres..."
    if PeutTirerALArc():
        menu:
            "Si vous voulez décocher une flèche à cet insultant personnage":
                jump numero80
            "Sinon, il va falloir subir l'assaut.":
                jump numero92
    jump numero92

label numero57:
    "Les têtes désincarnées commencent à s'entrechoquer en hurlant et en proférant d'ignobles malédictions, puis elles se jettent sur vous et vous frappent à grands coups de crânes."
    "Vous résistez pendant un moment à cette terrifiante attaque, mais vous finissez par être à moitié assommé et totalement incapable de vous défendre plus longtemps."
    "Alors que vous vous affalez mollement sur le sol, les Rokuro-Kubi commencent à vous arracher des lambeaux de chair, sans même attendre votre mort."
    "Quel festin, ce soir, pour eux !"

label numero58:
    "Le mort vivant fait un nouveau bond qui le porte, cette fois, de l'autre côté du pont."
    "Là, il pousse un hululement à vous glacer le sang, puis il redevient visible."
    "C'est alors que se produit une chose plus épouvantable encore : les cadavres squelettiques qui flottaient au fil de la rivière sanglante se dressent hors de l'eau et commencent à s'animer."
    "Six d'entre eux envahissent le pont."
    if PeutTirerALArc():
        menu:
            "Si vous voulez tenter de tirer sur le samouraï mort vivant":
                jump numero134
            "Sinon.":
                jump numero242
    jump numero242

























# --------------youpi
