

init -2 python:
    from despin.ldoelh import ennemi
    import random

    unApresLautre_ = True
    ennemis_ = list()
    jumpFinCombat_ = ""

    def nouveauCombat(unApresLautre):
        unApresLautre_ = unApresLautre
        ennemis_.clear()

    def AjouterEnnemi(nom, habilete, endurance):
        nouvEnnemi = ennemi.Ennemi(nom, habilete, endurance)
        ennemis_.append(nouvEnnemi)

    def CommencerCombat(jumpFinCombat):
        jumpFinCombat_ = jumpFinCombat
        renpy.jump("debutCombat")

    def AffichageEnnemis():
        texte = ""
        for enn in ennemis_:
            texte = texte + str(enn)
            texte += "\n"
        return texte

    def TesterFinCombat():
        if len(ennemis_) > 0:
            renpy.jump("debutTourDeCombat")
        else:
            renpy.jump(jumpFinCombat_)

    def LancerDe():
        return random.randint(1, 6)

    def TourDeCombat():
        global endurance, habilete, ennemis_

        resDeJoueur = LancerDe() + LancerDe()
        resJoueur = habilete.m_Valeur + resDeJoueur
        texte = "Vous obtenez {} que vous ajoutez à votre habileté ce qui donne {}.".format(resDeJoueur, resJoueur)
        ennemi = ennemis_[0]
        resDeEnnemi = LancerDe() + LancerDe()
        resEnnemi = ennemi.m_Habilete + resDeEnnemi
        texte = texte + "{} obtient {} qu'il ajoute à son habileté ce qui donne {}.".format(ennemi.m_Nom, resDeEnnemi, resEnnemi)
        degats = 2
        texte = texte + "\n -> "
        if resJoueur > resEnnemi:
            ennemi.m_Endurance = ennemi.m_Endurance - degats
            if ennemi.m_Endurance <= 0:
                # ennemi éliminé
                texte = texte + "{} est tué.".format(ennemi.m_Nom)
                ennemis_.pop(0)
            else:
                texte = texte + "{} est blessé et perd {} d'endurance.".format(ennemi.m_Nom, degats)
        elif resJoueur < resEnnemi:
            PerteEndurance(degats)
            texte = texte + "Vous êtes blessé et perdez {} d'endurance.".format(degats)
        else:
            texte = texte + "Égalité."
        return texte


label debutCombat:
    "Le combat commence !"

label debutTourDeCombat:
    $ texteEnnemis = AffichageEnnemis()
    menu:
        "[texteEnnemis]"
        "Lancez deux dés pour votre habileté":
            jump resolutionTourDeCombat

label resolutionTourDeCombat:
    $ texteTourCombat = TourDeCombat()
    "[texteTourCombat]"
    $ TesterFinCombat()
