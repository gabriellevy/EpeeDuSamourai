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
label numero8_choix:
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
    show tatsu at right
    t "Ainsi, s'exclame le Tatsu d'une voix tonitruante, tu as réussi à tenir bon jusqu'au Tournoi de l'Espace !"
    t "Je te félicite d'un tel exploit, mortel, et j'ai décidé de t'aider à combattre le Dai-Oni, car je souhaite moi aussi la défaite d'Ikiru, Maître des Ombres."
    t "Lorsque tu franchiras la porte de l'Arène Hors du Temps, je serai donc là pour me battre à tes côtés."
    hide tatsu
    with dissolve
    "Sur ces mots, le Tatsu s'évanouit dans les airs. Il ne vous reste plus maintenant qu'à retourner au Centre des Univers en passant par la porte qui se trouve derrière vous."
    $ soutienTatsu = True
    jump numero8_choix

label numero13:
    "Trois des monstres écailleux passent soudain à l'offensive et se précipitent sur vous toutes griffes dehors. Affrontez-les l'un après l'autre :"
    $ nouveauCombat(True)
    $ AjouterEnnemi("Premier KAPPA", 8, 14)
    $ AjouterEnnemi("Deuxième KAPPA", 8, 12)
    $ AjouterEnnemi("Troisième KAPPA", 7, 13)
    $ SetFinCombatTesterEnduranceRestanteEnnemi(4)
    $ CommencerCombat("numero31")

label numero14:
    "Le conducteur se dirige vers les écuries pour y garer sa charrette, puis il s'éloigne à pas lourds, marmonnant dans sa barbe qu'il se sent la gorge sèche après cette longue journée de labeur."
    "Après son départ, vous vous glissez rapidement hors de votre cachette et vous inspectez les alentours."
    "Au bout de la grande cour carrée se dresse un édifice en pierre orné de pignons finement sculptés et surmonté d'un toit en pagode."
    "Il s'agit vraisemblablement du palais du seigneur Tsietsin."
    "En continuant votre observation, vous remarquez que les portes de cette riche demeure sont flanquées de deux gardes qui retiennent immédiatement toute votre attention."
    "Ce sont des Shikomes, d'abominables humanoïdes, poilus comme des singes, pourvus de griffes acérées et affligés d'un gros groin épaté."
    "Ils portent des cuirasses sales et déchirées — de mauvaises imitations de tenue de samouraï— mais leurs armes, en revanche, semblent en parfait état."
    "La présence de telles créatures en ces lieux prouve évidemment que Tsietsin s'est allié à Ikiru, Maître des Ombres."
    "Tsietsin devant être dans son palais en ce moment, il est primordial de vous débarrasser de lui avant toute chose."
    "Vous attendez que la nuit tombe avant d'entrer en action."
    menu:
        "Grâce à l'art du Kyujutsu, vous pouvez tenter de supprimer les deux Shikomes en leur portant à chacun un seul coup mortel" if disciplineKyujutsu == discipline.m_Valeur:
            jump numero46
        "vous pouvez essayer de vous approcher furtivement afin de les attaquer par surprise":
            jump numero64
        "avancer ouvertement vers eux et prétendre que vous avez un message important pour le seigneur Tsietsin":
            jump numero84
        "vous pouvez marcher d'un pas décidé vers le palais et passer d'un air autoritaire, comme si les gardes n'existaient pas":
            jump numero100

label numero15:
    "Vous sortez à l'autre bout du village, à l'opposé du chemin que vous aviez pris pour y entrer."
    "Personne ne semble avoir remarqué votre fuite, et vous en éprouvez un vif soulagement : il y avait décidément quelque chose d'inquiétant chez ces villageois..."
    "Mais soudain, à votre grande stupéfaction, vous apercevez le vieux charbonnier que vous aviez rencontré de l'autre côté du village."
    "Vous l'avez laissé pour mort, il n'y a pas si longtemps, et le voilà maintenant qui vous observe en grimaçant derrière un mur !"
    "N'en croyant pas vos yeux, vous faites un pas en avant, mais vous vous arrêtez net en voyant soudain la tête de l'homme se détacher de son corps et se mettre à planer dans les airs !"
    "Vous poussez un cri d'effroi en comprenant qu'il s'agit d'un Rokuro-Kubi, un mort vivant dont la tête se détache la nuit venue, afin d'aller chasser."
    "Vous sentez une salive brûlante vous éclabousser le visage lorsque la tête passe en crachant et sifflant au-dessus de vous."
    "La douleur provoquée par ce poison corrosif est atroce ; vous perdez 2 points d'ENDURANCE."
    $ PerteEndurance(2)
    "Le Rokuro-Kubi continue à tournoyer au-dessus de votre tête et vous devez l'affronter en un combat mortel :"
    $ nouveauCombat(True)
    $ AjouterEnnemi("ROKURO-KUBI", 7, 8)
    $ CommencerCombat("numero153")

label numero16:
    "Il se produit un craquement assourdissant et une lourde herse en fer rouillé s'abat brutalement dans votre dos, à quelques centimètres de l'endroit où vous étiez un instant auparavant !"
    "Il vous est désormais impossible de rebrousser chemin, aussi vous hâtez-vous de continuer à avancer."
    "Une odeur fétide vous frappe les narines et vous voyez briller, devant vous, une lumière blafarde."
    jump numero50

label numero17:
    "Il vous faut trois jours entiers pour traverser les étendues sauvages et désolées qui vous séparent du marais des Brouillards."
    "Au cours de ce voyage, vous prenez à peine le temps de vous reposer, ne vous accordant que de brèves haltes afin de ne pas être surpris en terrain découvert par les cavaliers samouraïs au service d'Ikiru."
    "Quand vous atteignez enfin le marais des Brouillards, l'air semble s'être anormalement rafraîchi, mais vous vous consolez en pensant que cet itinéraire peu recommandé vous permettra d'atteindre le coeur du royaume d'Ikiru avant même que celui-ci n'ait eu vent de votre intrusion."
    "Peu après, une route pavée vous conduit plein nord vers le delta, ce qui vous arrange parfaitement."
    "La route court sur une longue chaussée surélevée, entourée de part et d'autre par des lacs et des marécages."
    "Au fur et à mesure que vous progressez, le brouillard s'épaissit et, bientôt, vous n'y voyez plus qu'à quelques pas devant vous. Finalement, vous arrivez à un croisement."
    "La route pavée s'enfonce dans le brouillard en obliquant vers le nord-est, et un sentier en terre battue part vers le nord, en direction du puits des Ames, ainsi que l'indique un panneau fléché sur le bord du chemin."
    "Par ailleurs, une autre digue s'avance, à l'ouest, vers un lac nappé de brume."
    menu:
        "vous possédez une carte indiquant la route de la Pagode Écarlate" if cartePagodeEcarlate_:
            jump numero107
        "vous n'en avez pas, vous pouvez choisir d'aller soit vers le nord":
            jump numero285
        "soit vers l'ouest":
            jump numero125
        "ou bien vers le nord-est":
            jump numero249

label numero18:
    "Vous montez l'escalier quatre à quatre et vous débouchez dans une petite salle de garde."
    "Le seul homme qui s'y trouve vous regarde avec une surprise non dissimulée, et vous profitez de sa stupéfaction pour filer comme une flèche sous ses yeux et vous engager dans les longs couloirs du palais."
    "Mais l'alarme a été donnée ! Pendant un moment, vous offrez une belle course poursuite aux gardes, mais il est impossible de s'échapper de la forteresse de Tsietsin avec tant d'hommes sur vos talons."
    "Vous vous faites finalement capturer et, après une résistance héroïque mais hélas ! de courte durée —, vous êtes finalement écrasé sous le nombre de vos adversaires et sauvagement mis en pièces."

label numero19:
    "Le pouvoir du sabre noir incrusté de runes épuise peu à peu vos forces vitales : vous perdez 1 point d'HABlLETÉ et 1 point de CHANCE."
    $ PerteHabilete(1)
    $ PerteChance(1)
    jump numero199

label numero20:
    "Le geôlier s'approche de vous en grommelant d'un air ennuyé."
    menu:
        "Tentez votre Chance."
        "Lancer deux dés":
            $ texteResultatChance = TentezVotreChance()
    "[texteResultatChance]"
    if chanceux:
        jump numero282
    else:
        jump numero296

label numero21:
    "La flèche fend l'air en filant droit vers la poitrine d'un des deux monstres, mais le sifflement menaçant qu'elle produit dans sa course ne paraît pas les impressionner le moins du monde."
    "L'autre se jette sur vous et parvient à vous lacérer de ses griffes palmées, tandis que vous vous efforcez désespérément de reculer tout au bout de la jetée en pierre."
    "Vous perdez 3 points d'ENDURANCE. La démarche entravée par le harcèlement du monstre, vous glissez maladroitement et vous perdez l'équilibre."
    $ PerteEndurance(3)
    "En désespoir de cause, vous décidez de plonger dans les eaux blanches et écumeuses qui rugissent sous le gué."
    jump numero49

label numero22:
    "Éléonore avance d'un pas et un violent éclair bleu jaillit de ses mains tendues en avant."
    "La décharge vient frapper Gargantus en plein visage, et ses yeux de rubis explosent comme deux billes de verre."
    "Dans un hurlement de douleur retentissant, le monstre s'effondre sur le sol où il reste inerte, aussi raide et immobile qu'une statue de bronze."
    "Eléonore se tourne alors vers vous et dit : -J'ai payé ma dette envers vous, mais maintenant je dois partir."
    "Je vous souhaite bonne chance, guerrier ! Sur un dernier signe de la main, elle s'éloigne et dis-paraît pour s'en retourner d'où elle était mystérieusement venue."
    "C'est alors que le Dai-Oni s'adresse à vous :"
    show daioni at right
    with moveinright
    d "Tu t'en es bien sorti, mortel, mais à présent, pré- pare-toi à mourir de ma propre main !"
    "Sur ces mots, il avance sur vous en faisant tournoyer un tetsubo, redoutable fléau d'arme hérissé de pointes tranchantes."
    menu:
        "envoyer le Ki-Rin combattre le Dai-Oni" if soutienKiRin:
            jump numero394
        "affronter, seul, le Dai-Oni":
            jump numero292

label numero23:
    "Tout en vous protégeant la tête de votre wakizashi, vous reculez vivement tandis qu'une pluie de brandons enflammés s'abat autour de vous."
    "L'un deux se coince dans une articulation de votre armure et un autre ébranle votre heaume. Vous êtes gravement brûlé et sévèrement commotionné (vous perdez 5 points d'ENDURANCE."
    $ PerteEndurance(5)
    "Si vous êtes toujours en vie, vous laissez libre cours à votre rage et, d'un coup net et précis, vous décapitez votre agresseur à l'aide de votre katana."
    "Vous vous précipitez ensuite sur les autres assaillants, mais ceux-ci s'enfuient sans demander leur reste et se réfugient au fond des bois."
    "Après avoir éteint les quelques flammes qui vous menaçaient encore, vous vous remettez en marche."
    "Vous avez vaillamment défendu l'honneur du Shogun, ce qui vous permet d'ajouter 1 point à votre propre Honneur."
    $ GainHonneur(1)
    jump numero195

label numero24:
    "Vous pressez le pas et, laissant le village loin derrière vous, vous traversez l'étendue onduleuse des terres labourées."
    "Quelque temps après, la grand-route passe au pied d'une colline. En la contournant, vous voyez se dresser un château fortifié non loin de la route."
    "Vous reconnaissez l'étendard qui flotte en haut des remparts : ce sont les couleurs du seigneur Tsietsin, puissant daïmyo local."
    menu:
        "Si vous avez déjà rencontré des soldats de Tsietsin":
            jump numero314
        "Si tel n'est pas le cas":
            jump numero326

label numero25:
    "Alourdi par le poids de votre armure, vous vous enfoncez profondément dans les eaux glacées du puits."
    "En vous débarrassant de votre lourde cuirasse, peut-être parviendrez-vous à remonter vers la surface à temps ?"
    "Hélas ! vos poumons sont sur le point d'exploser et vos forces vous abandonnent peu à peu."
    if endurance.m_Valeur <= 12:
        jump numero353
    else:
        jump numero313

label numero26:
    t "-Non, mortel, ce n'est pas la bonne réponse"
    "dit le Tatsu en se pourléchant d'avance les babines."
    t "Et maintenant... je vais te dévorer !"
    "Dans un grognement vorace, le dragon s'élance vers vous en faisant claquer ses mâchoires. Si vous ne voulez pas être mangé tout cru, il vous faut affronter sans délai cet adversaire gargantuesque :"
    $ nouveauCombat(True)
    $ AjouterEnnemi("TATSU", 11, 13)
    $ CommencerCombat("numero42")

# ------------------------------------------------------------------------------> plein de numéros pas faits :

label numero34:
    "Vous avancez d'un pas résolu sur la piste poussiéreuse, mais vous accélérez l'allure en entendant des hurlements de terreur en provenance du village."
    "C'est alors que vous apercevez une bande de cavaliers — probablement des bandits — en train de charger des villageois en proie à la panique la plus totale."
    "Pendant un instant, un bosquet d'arbres vous empêche de suivre la scène."
    "A peine l'avez-vous contourné que vous voyez un cavalier galoper à bride abattue dans votre direction."
    "C'est un samouraï armé d'une longue lance et portant l'armure en laque bleu et vert du daïmyo Tsietsin, un seigneur des environs."
    menu:
        "Qu'allez-vous faire :"
        "vous précipiter à sa rencontre en exhibant le sceau du Shogun, et lui ordonner de vous expliquer ce qui se passe":
            jump numero44
        "ou attendre de pied ferme qu'il arrive à votre hauteur":
            jump numero56

label numero35:
    "Alors que trois des monstres verts s'élancent vers le tertre dans la ferme intention de vous sauter dessus, vous exécutez vous-même un bond prodigieux qui vous porte à la cime des arbres et vous permet d'atterrir derrière vos assaillants."
    "Ces derniers font immédiatement volte-face et se ruent à nouveau sur vous."
    "Cependant, vous avez remarqué un phénomène fort intéressant en survolant les monstres : leur tête plate est en réalité une espèce de cuvette remplie de liquide !"
    "Vous comprenez maintenant la raison de leur étrange façon de marcher : ces créatures doivent absolument rester en équilibre afin de ne pas renverser leur liquide crânien !"
    menu:
        "Vous n'avez qu'une alternative : vous enfuir en courant":
            jump numero173
        "ou bien vous placer dos aux arbres et faire front à vos ennemis":
            jump numero183

label numero36:
    "Le regard du Phénix se voile et la flamme qui animait ses yeux vacille avant de s'éteindre complètement."
    "La fabuleuse créature s'abat comme une masse à vos pieds, vidée de toute vie. Soudain, elle s'embrase à nouveau !"
    "Fort heureusement, c'est pour devenir la proie de ses propres flammes, et son corps se consume entièrement, ne formant bientôt plus qu'un petit tas de cendres sur le sol."
    "C'est alors que se produit un phénomène incroyable : un autre Phénix, légèrement plus petit que le précédent, renaît des cendres encore fumantes."
    "Il s'immobilise dans les airs en poussant un cri d'exultation, puis s'envole à tire-d'aile, disparaissant de votre vue à votre grand soulagement."
    "Pendant un instant, vous restez tout ébahi de ce que vous venez de voir, puis, reprenant vos esprits, vous franchissez la porte pour retourner au Centre des Univers."
    jump numero8_choix

label numero37:
    "Rassemblant toute l'autorité dont vous pouvez faire preuve dans ces pénibles circonstances, vous ordonnez aux paysans de vous tirer de ce piège."
    "Les hommes s'avancent vers vous un par un, méfiants."
    "Après avoir constaté que vous êtes effectivement dans une bien mauvaise posture, ils se mettent à grimacer des sourires peu rassurants et à discuter de votre sort."
    "La solution qu'ils adoptent à la majorité ne manque pas de raffinement : ils vont vous sortir de là..."
    "pour vous enfourner, vivant, dans une meule à charbon ! Sur ce, ils commencent à préparer des liens pour vous attacher."
    "Mieux vaudrait les dissuader sans délai de commettre un tel acte !"
    menu:
        "Si vous désirez leur faire part de l'importance de votre mission":
            jump numero89
        "Si vous jugez préférable de leur dire que les esprits viendront à jamais les hanter, s'ils osent assassiner le Senseï du Shogun":
            jump numero101

label numero38:
    "Il se produit soudain un craquement assourdissant comme un coup de tonnerre, et une onde de douleur vous foudroie le corps :"
    "quelque chose vient de vous heurter le dos avec une violence inouïe qui vous jette au sol. Vous perdez 3 points d'ENDURANCE."
    $ PerteEndurance(3)
    "Si vous êtes encore en vie, vous constatez, en vous retournant péniblement, qu'une grande herse en fer rouillé vient de s'abattre derrière vous en vous écorchant le dos au passage."
    "Comme il vous est désormais impossible de rebrousser chemin, vous vous remettez en route."
    "Au bout de quelques mètres, une odeur nauséabonde vous frappe les narines, et, droit devant vous, vous apercevez une lueur laiteuse dont l'éclat augmente au fur et à mesure que vous approchez."
    jump numero50

label numero39:
    "Les pointes acérées du trident ont atteint vos poumons. Vous vous efiondrez sur le sol en crachant du sang."
    "Vous êtes tombé aux mains des Kappas, et il n'y a plus aucun espoir. Avant même que vous ne rendiez le dernier souffle, ils vous entraînent au plus profond des eaux glauques de la rivière."

label numero40:
    "Le geôlier parcourt le couloir en réveillant les autres prisonniers, glissant au passage des écuelles d'eau croupie et des tranches de pain noir sous les portes."
    "Puis il revient sur ses pas et ouvre la porte de votre cellule. Cette fois, il est accompagné de trois soldats."
    menu:
        "Si vous voulez faire semblant d'être blessé, afin de les attaquer par surprise dès qu'ils seront près de vous":
            jump numero370
        "Si vous préférez dire que vous êtes blessé, mais attendre qu'ils vous aient sorti de votre cachot pour tenter de prendre une arme à l'extérieur et la fuite par la même occasion":
            jump numero380
