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
