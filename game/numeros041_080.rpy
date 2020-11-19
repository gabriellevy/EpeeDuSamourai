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

label numero59:
    "Les charbonniers sont au nombre de dix."
    "Ils sont regroupés au centre de plusieurs tertres fumants, recouverts de tourbe fraîchement extraite."
    "Des volutes de fumée grise et dense s'échappent des monticules : c'est sous ces meules qu'on brûle du bois à très haute température, afin de le transformer en charbon."
    "A côté, il y a de grands tas de bûches prêtes à subir le même traitement."
    menu:
        "A présent, qu'allez-vous faire :"
        "ordonner à tous les hommes présents dans la charbonnière de s'agenouiller devant vous en signe de soumission":
            jump numero111
        "ou bien décocher une flèche au jeune malotru qui vous a insulté" if PeutTirerALArc():
            jump numero123
        "tirer vos sabres":
            jump numero135
        "ou encore vous élancer d'un bond par-dessus le petit groupe" if disciplineKarumijutsu == discipline.m_Valeur:
            jump numero147

label numero60:
    "Le sabre au poing, vous avancez en criant :"
    "— Vous feriez mieux de m'aider, sinon gare aux conséquences !"
    "L'étrange femme vous observe, le visage blême et déformé par la peur, mais elle tend soudain un bras en avant et fait jaillir un éclair bleu de ses doigts fuselés."
    "La décharge d'énergie explose à vos pieds, libérant une flamme bleutée qui vous brûle au second degré."
    "Vous perdez 2 points d'ENDURANCE."
    $ PerteEndurance(2)
    "Une fois remis de ce choc, vous constatez que la femme a disparu."
    menu:
        "Si vous voulez vous lancer à sa recherche":
            jump numero70
        "Si vous préférez ne pas insister, franchissez la porte qui vous ramènera au Centre des Univers.":
            jump numero8_choix

label numero61:
    "Alors que vous êtes à mi-chemin, vos pieds dérapent soudain sur le limon vaseux qui recouvre la jetée et, perdant l'équilibre, vous tombez à la renverse dans les eaux écumeuses qui rugissent en aval."
    "Malheureusement pour vous, les Kappas — puisque c'est ainsi qu'on nomme ces abominables créatures ont justement tendu là un piège d'une rare cruauté :"
    "plusieurs rangées de pieux acérés qui affleurent à la surface. Vous vous empalez dessus et, privé de la protection de votre armure, vous n'avez plus aucune chance de vous en sortir vivant."

label numero62:
    "D'un geste net, vous plongez votre sabre dans l'oeil droit du monstre."
    "Celui-ci se rejette en arrière en émettant un affreux gargouillement, puis il se met à battre frénétiquement l'air de ses pattes, dans les affres de l'agonie."
    "Vous reculez pour l'éviter, mais il s'apaise soudain et s'écroule, raide mort, sur le sol."
    "En inspectant rapidement la caverne, vous apercevez une issue dans le fond et, dans un coin, le « Trésor » du monstre : un amas de vêtements en loques, d'ossements et d'armes rongées par la rouille."
    "En y regardant de plus près, toutefois, vous découvrez qu'il y a également 15 Pièces d'Or, un casque en argent finement ciselé, une fiole contenant un liquide vert foncé, ainsi qu'un magnifique éventail de guerre en fer forgé qu'on utilisait jadis pour envoyer des messages codés aux troupes."
    "Cet étrange objet est incrusté, sur la tranche, d'un motif en ivoire dont la seule vue vous donne la nausée,"
    menu:
        "Que voulez-vous faire à présent :"
        "Ramasser l'éventail de guerre et l'ouvrir ?":
            jump numero182
        "Prendre une gorgée du liquide vert contenu dans la fiole ?":
            jump numero196
        "Mettre le casque d'argent ?":
            jump numero210
        "Laisser tout cela et sortir de la caverne sans plus tarder ?":
            jump numero222

label numero63:
    "D'un geste vif, vous lancez l'Epée vers le trône."
    "La lame magique vole comme une flèche vers sa cible."
    "Dès qu'elle franchit le cercle des ombres qui entourent le trône, elle explose en une immense gerbe de lumière qui les consume toutes entièrement."
    "Puis Mort Joyeuse continue sa trajectoire et, dans le rayonnement intense, vous voyez Ikiru se recroqueviller craintivement au fond de son siège."
    "Pourtant, au dernier moment, il fait preuve d'un réflexe inattendu et se jette sur le côté."
    "La lame se plante profondément dans le trône, où elle reste en vibrant."
    "La voici hors de votre portée, et le pouvoir qu'elle vous conférait s'est évanoui ;"
    "vous perdez 4 points d'ENDURANCE , 2 points d'HABILETÉ et 2 points de CHANCE."
    $ PerteEndurance(4)
    $ PerteHabilete(2)
    $ PerteChance(2)
    "Ikiru se redresse alors fièrement et vous dit:"
    "-Pauvre imbécile !"
    "Sa voix sonne comme un bruissement de feuilles mortes."
    jump numero260

label numero64:
    "Vous avancez à découvert. Les Shikomes vous regar-dent approcher d'un oeil morne ;"
    "ils dégagent une forte odeur de beurre rance. Alors que vous arrivez à leur hauteur, vous les prenez par surprise et vous passez à l'attaque."
    "Il ne vous faut que quelques secondes pour en éliminer un, mais le second, en revanche, en profite pour beugler d'effroi."
    "En l'espace de deux minutes, tout le château se met à fourmiller de gardes samouraïs et d'autres Shikomes."
    "Vous tentez immédiatement de fuir, mais vous êtes rapidement submergé par le flot de vos poursuivants."
    "Ils vous font prisonnier et vous accablent de sarcasmes, riant du Shogun et de son minable Senseï apparemment, ils savent qui vous êtes..."
    "On vous traîne ensuite sans ménagement jusque dans les cachots, et l'on vous jette dans une sinistre cellule."
    "Le geôlier, un homme gras et rougeaud, vêtu d'un pourpoint de cuir crasseux, vous grogne d'un air goguenard :"
    g "— On te conduira demain devant le Shogun Tsietsin."
    "Puis il vous ferme brutalement la porte à la figure."
    "Vous voici seul. On vous a pris toutes vos armes et cela vous fait bien plus honte que l'indignité de votre capture et les humiliations que vous avez dû subir."
    "Vous perdez 1 point d'Honneur."
    $ PerteHonneur(1)
    "A présent, il ne vous reste plus qu'à aller vous allonger sur la maigre paillasse qui occupe un coin du cachot et à essayer de trouver le sommeil en attendant le lendemain matin."
    jump numero316

label numero65:
    "La nuit tombe, et vous n'êtes toujours pas arrivé à vous sortir des griffes de ce piège."
    "Par ailleurs, vous éprouvez la désagréable sensation que les charbonniers vous épient, cachés dans les environs."
    "Peu à peu, la nuit s'anime d'une multitude de bruits : bruissement des feuilles au gré du vent, trottinement des petits animaux qui peuplent le sous-bois et piaillements brefs de rapaces nocturnes."
    "Soudain, tout se taît. Le vent lui-même s'est calmé."
    "Quelques secondes plus tard, un seul bruit vient percer le silence pesant qui s'est abattu sur la forêt :"
    "la démarche souple mais puissante d'une bête qui avance à pas feutrés. Vous l'entendez renifler votre piste."
    "Tout à coup, elle pousse un rugissement féroce qui fait s'envoler une nuée d'oiseaux affolés."
    "Il s'agit certainement d'un Shako-Gurubi, une espèce de panthère relativement commune dans ces régions boisées."
    "Hélas ! vous êtes presque impuissant, pris au piège dans l'obscurité totale."
    menu:
        "Qu'allez-vous donc faire :"
        "tirer de toutes vos forces sur votre jambe afin de vous arracher du piège à tout prix et vous défendre l'arme à la main":
            jump numero119
        "ou bien tenir votre sabre à bout de bras et vous préparer à lutter à l'aveuglette, en espérant que la bête ne vous attaquera pas":
            jump numero139

label numero66:
    "Vous franchissez la porte de la « Montagne de l'Ineffable Sainteté»."
    "Vous vous retrouvez au pied d'un haut sommet, facile à escalader, certes, mais dont l'ascension serait longue et exténuante."
    "Néanmoins, comme il n'y a apparemment aucune autre chose à faire, vous commencez à grimper."
    "Après une éternité, vous arrivez enfin au sommet."
    "Le spectacle qui vous y attend vous laisse tout ébahi : une créature de noble stature se dresse juste devant vous."
    "Ses yeux sont deux boules de feu ; elle a un corps de cheval pourvu de deux immenses ailes et surmonté d'une tête de lion."
    "Il se dégage de tout son être une forte aura de puissance et de majesté."
    "C'est un Ki-Rin, serviteur des dieux, représentant et défenseur de la justice et du bien."
    "L'être magnifique vous observe pendant un court instant."
    if honneur.m_Valeur >= 5:
        jump numero340
    else:
        jump numero352

label numero67:
    "Les pointes du trident ont transpercé votre armure et vous ont brisé deux côtes."
    "Vous perdez 4 points d'ENDURANCE."
    $ PerteEndurance(4)
    "Si vous survivez à cette douloureuse blessure, vous jugez préférable de vous faire le plus discret possible et vous vous éloignez rapidement de cet endroit bourbeux."
    jump numero335

label numero68:
    "Derrière la porte des « Anciennes Plaines » s'ouvre un paysage époustouflant : une immense étendue steppique où se dressent à perte de vue des collines basses, couvertes de taillis."
    "Le ciel est bleu, sans un nuage, et l'air semble le plus pur et le plus frais que vous n'ayez jamais respiré."
    "Soudain, vous voyez passer devant vous un cerf primitif qui disparaît en bon-dissant."
    "Derrière vous, flottant entre terre et ciel, se trouve la porte qui vous ramènera au Centre des Univers."
    "C'est alors que surgit un autre animal. Mais cette fois, c'est un énorme fauve : l'ancêtre du tigre, trois fois plus gros, et dont la gueule s'orne de redoutables crocs en forme de sabre."
    "L'animal vous fixe sans ciller, puis il s'élance dans votre direction. Ses bonds sont si puissants qu'il semble voler. Dans quelques secondes, il sera sur vous."
    menu:
        "Qu'allez-vous faire :"
        "exhiber le Phénix en Rubis" if phenixEnRubis:
            jump numero214
        "tirer une flèche avec votre arc" if PeutTirerALArc():
            jump numero224
        "ou souffler dans un cor" if aUnCor:
            jump numero234
        "Si vous jugez préférable de prendre immédiatement la porte afin de regagner le Centre des Univers":
            jump numero8_choix

label numero69:
    "Les têtes désincarnées commencent à s'entrechoquer en hurlant et en proférant d'ignobles malédictions, puis elles se jettent sur vous et vous frappent à grands coups de crânes."
    "Vous résistez pendant un moment à cette terrifiante attaque, mais vous finissez par être à moitié assommé et totalement incapable de vous défendre plus longtemps."
    "Dans vos mouvements affolés et désordonnés, vous vous heurtez violemment contre la margelle du puits et vous tombez à la renverse, faisant une chute de quelque vingt mètres avant de plonger dans une eau glaciale."
    jump numero25

label numero70:
    "Vous suivez la piste de l'étrange femme à travers les bois, mais vous perdez sa trace au bout de quelques dizaines de mètres."
    "Vous continuez malgré tout à avancer au hasard. Peu après, vous réalisez que vous êtes complètement perdu :"
    "vous avez l'impression que la forêt se modifie sans cesse autour de vous et vous n'avez plus le moindre sens de l'orientation."
    "Vous voici condamné à errer pour l'éternité dans la Forêt Enchantée. Peut-être, un jour, croiserez-vous le chemin de la jeune femme ? En attendant, votre aventure se termine ici."

label numero71:
    "La première personne que vous rencontrez est une vieille paysanne qui porte sur la tête un fichu en soie défraîchie."
    "Elle semble triste et mélancolique, mais accepte néanmoins de vous conduire chez elle."
    "Son humble demeure est une vieille cabane en bois dont un des murs est à moitié défoncé."
    "La femme vous désigne une paillasse dans un coin et, dans l'âtre, une petite marmite remplie de gruau."
    menu:
        "Si vous souhaitez réparer le mur avant de vous installer":
            jump numero215
        "Si vous préférez vous rassasier sans plus attendre":
            jump numero203

label numero72:
    "Votre arme décrit un rapide arc de cercle et entaille profondément la jambe du cavalier."
    "Ce dernier laisse échapper un hurlement de douleur et tombe de sa selle."
    "Avant même qu'il ne touche le sol, vous lui tranchez la tête d'un coup de katana."
    "Maintenant, la situation vous apparaît sous un jour nouveau :"
    "le seigneur Tsietsin est un félon et ses hommes sont en train de semer la terreur dans le village, pillant et massacrant des paysans sans défense."
    menu:
        "Si vous décidez d'abandonner le village à son triste sort, pour donner priorité absolue à votre mission":
            jump numero104
        "Si vous voulez aller prêter main-forte aux paysans et attaquer le premier samouraï que vous rencontrerez":
            jump numero116
        "Si vous jugez plus efficace de vous rendre au village et de proclamer qu'en tant que Senseï du Shogun, vous vous battrez en duel, selon les règles de l'honneur, contre quiconque osera se dresser contre vous":
            jump numero128
        "Enfin, si vous maîtrisez l'art du Kyujutsu, vous pouvez gagner le village et, vous cachant de maison en maison, abattre les pillards un à un, au fur et à mesure qu'ils apparaîtront dans votre ligne de tir" if PeutTirerALArc():
            jump numero140

label numero73:
    "Vous avancez d'un pas prudent sur la jetée en pierre."
    "Celle-ci est immergée de quelques centimètres et le limon vaseux qui la recouvre la rend dangereusement glissante."
    "Soudain, deux monstres à la peau verte et squameuse jaillissent des profondeurs de la rivière et prennent pied sur la jetée."
    "Ils sont munis d'impressionnantes griffes palmées qui leur permettent d'avancer sans glisser sur la vase."
    menu:
        "Si vous voulez sauter de la jetée et plonger dans les eaux écumeuses qui rugissent en aval":
            jump numero49
        "Si vous préférez rebrousser chemin et, une fois la berge atteinte, vous enfuir au plus vite et chercher un endroit plus sûr pour traverser":
            jump numero105
        "Vous pouvez tenter d'effrayer vos ennemis en tirant une flèche hurleuse." if PeutTirerALArc():
            jump numero21

label numero74:
    "Vous avez vaincu le Dai-Oni ! Ce dernier gît à vos pieds et sa vie ne tient plus qu'à un fil. Peu à peu, les ombres fantomatiques quittent l'Arène."
    "Quand vous restez seul à seul avec votre adversaire, vous l'entendez murmurer avec peine."
    d "— Tu as gagné, mortel, et je suis tenu, par les lois célestes qui régissent le Tournoi de l'Espace, de t'accorder une seule et unique question."
    "L'aura de magie qui auréolait le Dai-Oni est en train de disparaître."
    "De votre côté, la victoire que vous venez de remporter sur cet adversaire hors du commun vous permet de regagner 1 point d'HABILETÉ, 1 point de CHANCE ou 2 points d'ENDURANCE, selon les dommages qui vous ont éventuellement été infligés lors du précédent combat."
    $ GainHabilete(1)
    $ GainChance(1)
    $ GainEndurance(2)
    menu:
        "A présent, qu'allez-vous demander au Dai-Oni :"
        "Quel est le secret de Mort Joyeuse ?":
            jump numero206
        "Comment vaincre Ikiru, Maître des Ténèbres ?":
            jump numero188
        "Pouvez-vous m'aider à accomplir ma mission et anéantir Ikiru ?":
            jump numero150





























# --------------youpi
