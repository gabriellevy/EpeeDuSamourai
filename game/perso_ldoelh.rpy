#initialisation persos
init -1 python:
    import random
    from abs import carac

    def initBaseCaracs():
        global situation_
        enduranceVal = 12 + random.randint(1, 6) + random.randint(1, 6)
        situation_.SetValCarac("endurance", enduranceVal)
        situation_.SetValCarac("maxEndurance", enduranceVal)
        situation_.SetValCarac("honneur", 3)

        maxRepas = 10
        situation_.SetValCarac("repas", maxRepas)
        situation_.SetValCarac("maxRepas", maxRepas)

    # -------------> infos diverses spécifiques aventure
    # ATTENTION A FAIRE : rien de tout ça ne se sauvegarde. Il faudra probablement en faire des caracs de situation (mais que faire pour sauvegarder un combat en cours ?) etc
    cartePagodeEcarlate_ = False # a une carte qui mène à la pagode écarlate
    secretMortJoyeuse_ = False

    flechesSaule = carac.Carac("Flèches de saule", 0)
    flechesHarpon = carac.Carac("Flèches harpon", 0)
    flechesPerforantes = carac.Carac("Flèches perforantes", 0)
    flechesHurleuses = carac.Carac("Flèches hurleuses", 0)

    disciplineKyujutsu = "Kyujutsu" # tir à l'arc
    disciplineIaijutsu = "Iaijutsu"
    disciplineKarumijutsu = "Karumijutsu"
    disciplineNitoKenjutsu = "Ni-to-Kenjutsu"

    # objets
    phenixEnRubis = False # A un Phénix en Rubis
    aUnCor = False

    # soutiens lors du tournoi de l'espace
    soutienTatsu = False
    soutienKiRin = False

    # chance
    chance = carac.Carac("Chance", 6 + random.randint(1, 6))
    maxChance = chance.m_Valeur
    chanceux = True # true si le dernier lancer a donné comme résultat "chanceux"

    # habileté :
    habilete = carac.Carac("Habileté de base", random.randint(7, 12))
    habileteCalculee = carac.Carac("Habileté", habilete.m_Valeur) # peut être différente de l'habileté de base si par exemple le perso a perdu son épée
    aUnKatana = True
    habile_ = True # true si le dernier lancer baé sur l'habileté a donné une réussite

    def ObtientLePhenixRubis():
        situation_.SetValCarac("PhenixRubis", 1)

    def ALePhenixRubis():
        return situation_.GetValCaracInt("PhenixRubis") == 1

    def PeutTirerALArc():
        return disciplineKyujutsu == discipline.m_Valeur and ADesFleches()

    def ADesFleches():
        return flechesSaule.m_Valeur > 0 or flechesHarpon.m_Valeur > 0 or flechesPerforantes.m_Valeur > 0 or flechesHurleuses.m_Valeur > 0

    def GainDeChance(num):
        global chance, maxChance
        chance.m_Valeur = chance.m_Valeur + num
        if chance > maxChance:
            chance = maxChance

    def PerteChance(num):
        global chance, maxChance
        chance.m_Valeur = chance.m_Valeur - num
        if chance.m_Valeur < 0:
            chance.m_Valeur = 0

    def GainDeHabilete(num):
        global habilete
        habilete.m_Valeur = habilete.m_Valeur + num
        CalculerHabilete()

    def PerteHabilete(num):
        global habilete
        habilete.m_Valeur = habilete.m_Valeur - num
        if habilete.m_Valeur < 0:
            habilete.m_Valeur = 0
        CalculerHabilete()

    def GainEndurance(num):
        global endurance, maxEndurance
        situation_.AjouterACarac("endurance", num)
        maxVal = situation_.GetValCaracInt("maxEndurance")
        if situation_.GetValCaracInt("endurance") > maxVal:
            situation_.SetValCarac("endurance", maxVal)

    def PerteEndurance(num):
        global situation_
        situation_.RetirerACarac("endurance", num)
        if situation_.GetValCaracInt("endurance") <= 0:
            situation_.SetValCarac("endurance", 0)
            renpy.jump("mort")

    def GainHonneur(num):
        global situation_
        situation_.AjouterACarac("honneur", num)

    def PerteHonneur(num):
        global situation_
        situation_.RetirerACarac("honneur", num)
        if situation_.GetValCaracInt("honneur") <= 0:
            situation_.SetValCarac("honneur", 0)
            renpy.jump("numero99")

    def TentezVotreChance():
        global chance, chanceux
        jet = random.randint(1, 6) + random.randint(1, 6)
        texte = "rien encore"
        if jet <= chance.m_Valeur:
            chanceux = True
            texte = "{} est inférieur ou égal à votre chance de {} : vous êtes chanceux !".format(jet, chance)
        else:
            chanceux = False
            texte = "{} est supérieur à votre chance de {} : vous êtes malchanceux !".format(jet, chance)
        chance.m_Valeur = chance.m_Valeur - 1
        return texte

    def TentezVotreHabilete():
        global habilete, habile_
        jet = random.randint(1, 6) + random.randint(1, 6)
        texte = "rien encore"
        if jet < habilete.m_Valeur:
            habile_ = True
            texte = "{} est inférieur à votre habileté de {}. Réussite !".format(jet, habilete.m_Valeur)
        else:
            habile_ = False
            texte = "{} est supérieur ou égal à votre habileté de {} : échec !".format(jet, habilete.m_Valeur)
        return texte


    # arc :
    def Kyujutsu():
        global discipline, disciplineKyujutsu, flechesSaule, flechesHarpon, flechesPerforantes, flechesHurleuses
        flechesSaule.m_Valeur = 3
        flechesHarpon.m_Valeur = 3
        flechesPerforantes.m_Valeur = 3
        flechesHurleuses.m_Valeur = 3
        discipline = carac.Carac("Discipline", disciplineKyujutsu)
        return discipline

    def Iaijutsu():
        global discipline, disciplineIaijutsu
        discipline = carac.Carac("Discipline", disciplineIaijutsu)
        return discipline

    def Karumijutsu():
        global discipline, disciplineKarumijutsu
        discipline = carac.Carac("Discipline", disciplineKarumijutsu)
        return discipline

    def NitoKenjutsu():
        global discipline, disciplineNitoKenjutsu
        discipline = carac.Carac("Discipline", disciplineNitoKenjutsu)
        return discipline

    def DisciplineAleatoire():
        global disciplineKyujutsu, disciplineIaijutsu, disciplineKarumijutsu, disciplineNitoKenjutsu
        return Kyujutsu() # tmp test
        val = random.randint(1, 4)
        if val == 1:
            return Kyujutsu()
        elif val == 2:
            return Iaijutsu()
        elif val == 3:
            return Karumijutsu()

        return NitoKenjutsu()

    def CalculerHabilete():
        global habilete, habileteCalculee

        habileteCalculee.m_Valeur = habilete.m_Valeur
        if not aUnKatana:
            habileteCalculee.m_Valeur -= 1
        return habileteCalculee

    discipline = DisciplineAleatoire()
