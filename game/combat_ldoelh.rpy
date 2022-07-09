

init -2 python:
    from spe.ldoelh import ennemi
    import random
    ennemis_ = list()

    def ResetValsParDefaut():
        ennemis_ = list()
        unApresLautre_ = True
        jumpFinCombat_ = "???"
        testQuandBlesse_ = None
        gotoLabelQuandBlesseEtMalchanceux_ = ""
        tourGagneParJoueur_ = False # True si le joueur a belssé son ennemi
        tourPerduParJoueur_ = False # True si l'ennemi a blessé le joueur
        malusHabilete_ = 0
        gotoLabelQuandEnnemiBlesse_ = ""
        doublePourBlesser_ = False # si True, alors le joueur n'inflige qu'un dégât par blessure à cet ennemi, sauf si il obtient un double aux dés

    def SetDoublePourBlesser():
        doublePourBlesser_ = True

    def AjouterEnnemi(nom, habilete, endurance):
        nouvEnnemi = ennemi.Ennemi(nom, habilete, endurance)
        ennemis_.append(nouvEnnemi)

    def CommencerCombat(jumpFinCombat):
        global jumpFinCombat_
        jumpFinCombat_ = jumpFinCombat
        renpy.jump("debutCombat")

    def AffichageEnnemis():
        texte = ""
        for enn in ennemis_:
            texte = texte + str(enn)
            texte += "\n"
        return texte

    def SetGoToQuandEnnemiBlesse(gotoLabel):
        global gotoLabelQuandEnnemiBlesse_
        gotoLabelQuandEnnemiBlesse_ = gotoLabel

    def TesterFinCombatPlusDennemis():
        global ennemis_
        return len(ennemis_) == 0

    def TesterFinCombaDennemiEnduranceRestante():
        global ennemis_, situation_
        return ennemis_[0].m_Endurance <= situation_.GetValCaracInt("valEnduranceRestanteEnnemi_")

    def SetFinCombatTesterEnduranceRestanteEnnemi(val):
        """
        à appeler si on veut que le combat s'arrête quand l'ennemi se retrouve avec son endurance inférieur ou égale à val
        """
        global testFinCombat_, situation_
        situation_.SetValCarac("valEnduranceRestanteEnnemi_", val)
        testFinCombat_ = TesterFinCombaDennemiEnduranceRestante

    def SetTesteChanceQuandBlessure(gotoLabel):
        """
        Si cette fonction est appelée chaque fois que le joueur est blessé il doit tenter sa chance et si il est malchanceux il doit aller au gotoLabel
        """
        global testQuandBlesse_, gotoLabelQuandBlesseEtMalchanceux_
        gotoLabelQuandBlesseEtMalchanceux_ = gotoLabel
        testQuandBlesse_ = TesteChanceQuandBlessure

    def SetMalusHabilete(num):
        global malusHabilete_
        malusHabilete_ = num

    # fonction à appeler pour tester si le combat est terminé ( par défaut oui si il n'y a plus d'ennemis)
    testFinCombat_ = TesterFinCombatPlusDennemis

    def nouveauCombat(unApresLautre):
        global unApresLautre_, testFinCombat_, malusHabilete_, gotoLabelQuandEnnemiBlesse_, testQuandBlesse_, gotoLabelQuandBlesseEtMalchanceux_, malusHabilete_
        unApresLautre_ = unApresLautre
        testFinCombat_ = TesterFinCombatPlusDennemis
        ennemis_.clear()
        testQuandBlesse_ = None
        gotoLabelQuandBlesseEtMalchanceux_ = ""
        gotoLabelQuandEnnemiBlesse_ = ""
        malusHabilete_ = 0

    def TesterFinCombat():
        global jumpFinCombat_, testFinCombat_
        if testFinCombat_():
            ResetValsParDefaut()
            renpy.jump(jumpFinCombat_)
        else:
            renpy.jump("debutTourDeCombat")

    def TesteChanceQuandBlessure():
        renpy.jump("TesteChanceQuandBlessure")

    def MalChanceuxQuandBlessure():
        renpy.jump(gotoLabelQuandBlesseEtMalchanceux_)

    def LancerDe():
        return random.randint(1, 6)

    def LancerDeuxDes():
        return LancerDe() + LancerDe()

    def TesterQuandBlesse():
        if testQuandBlesse_ is not None:
            testQuandBlesse_()

    def ActionsQuandEnnemiBlesse():
        global gotoLabelQuandEnnemiBlesse_
        if gotoLabelQuandEnnemiBlesse_ != "":
            renpy.jump(gotoLabelQuandEnnemiBlesse_)

    def BlesseEnnemi(degats):
        ennemi = ennemis_[0]
        ennemi.m_Endurance = ennemi.m_Endurance - degats

    def TourDeCombat():
        global endurance, habilete, ennemis_, tourGagneParJoueur_, tourPerduParJoueur_
        tourGagneParJoueur_ = False
        tourPerduParJoueur_ = False

        resDe1 = LancerDe()
        resDe2 = LancerDe()
        resDeJoueur = resDe1 + resDe2
        resJoueur = habilete.m_Valeur + resDeJoueur - malusHabilete_
        texte = "Vous obtenez {} que vous ajoutez à votre habileté ".format(resDeJoueur)
        if malusHabilete_ > 0:
            texte = texte + "moins le malus de {} ".format(malusHabilete_)
        texte = texte + "ce qui donne {}.".format(resJoueur)
        ennemi = ennemis_[0]
        resDeEnnemi = LancerDe() + LancerDe()
        resEnnemi = ennemi.m_Habilete + resDeEnnemi
        texte = texte + "{} obtient {} qu'il ajoute à son habileté ce qui donne {}.".format(ennemi.m_Nom, resDeEnnemi, resEnnemi)
        degats = 2
        texte = texte + "\n -> "
        if resJoueur > resEnnemi:
            if doublePourBlesser_ and resDe1 != resDe2:
                degats = 1
                texte =  "{}\n Vous n'avez pas obtenu de double aux dés, les dégâts sont donc réduits à 1.".format(texte)
            BlesseEnnemi(degats)
            tourGagneParJoueur_ = True
            if ennemi.m_Endurance <= 0:
                # ennemi éliminé
                texte = texte + "{} est tué.".format(ennemi.m_Nom)
                ennemis_.pop(0)
            else:
                texte = texte + "{} est blessé et perd {} d'endurance.".format(ennemi.m_Nom, degats)
        elif resJoueur < resEnnemi:
            PerteEndurance(degats)
            texte = texte + "Vous êtes blessé et perdez {} d'endurance.".format(degats)
            tourPerduParJoueur_ = True
        else:
            texte = texte + "Égalité."
        return texte

# fin python

label debutCombat:
    if ALeIaijutsu():
        "Grâce à votre maîtrise du Iaijutsu vous infligez 3 dégâts en dégainant votre sabre d'un unique mouvement fulgurant et maîtrisé."
        $ BlesseEnnemi(3)

label debutTourDeCombat:
    $ texteEnnemis = AffichageEnnemis()
    menu:
        "[texteEnnemis]"
        "Lancez deux dés pour votre habileté":
            jump resolutionTourDeCombat

label resolutionTourDeCombat:
    $ texteTourCombat = TourDeCombat()
    "[texteTourCombat]"
    if tourPerduParJoueur_:
        $ TesterQuandBlesse()
    if tourGagneParJoueur_:
        $ ActionsQuandEnnemiBlesse()

label testerFinCombat:
    $ TesterFinCombat()

label TesteChanceQuandBlessure:
    menu:
        "De plus l'effet de la blessure vous oblige à tester votre chance."
        "Lancer deux dés":
            $ texteResultatChance = TentezVotreChance()
    "[texteResultatChance]"
    if not Chanceux():
        $ MalChanceuxQuandBlessure()
    jump testerFinCombat
