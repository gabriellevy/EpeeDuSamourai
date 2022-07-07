


label numero123:
    "En moins de temps qu'il ne le faut pour le dire, vous décochez une flèche au jeune insolent."
    menu:
        "Testez votre habileté."
        "Jetez deux dés.":
            $ texteResultatHabilete = TentezVotreHabilete()
    "[texteResultatHabilete]"
    if habile_:
        jump numero207
    else:
        jump numero351

label numero135:
    "L'un des charbonniers retire la tourbe humide de la meule la plus proche ; il en jaillit aussitôt de grandes flammes, accompagnées d'une fumée acre et dense."
    "D'autres s'emparent de pieux acérés en vue de vous attaquer ; les derniers, enfin, partent se dissimuler dans les bois qui s'étendent derrière la charbonnière."
    menu:
        "Tentez votre Chance."
        "Lancer deux dés":
            $ texteResultatChance = TentezVotreChance()
    "[texteResultatChance]"
    if Chanceux():
        jump numero293
    else:
        jump numero307
