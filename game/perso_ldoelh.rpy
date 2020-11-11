

#initialisation persos
init -1 python:
    import random
    from despin.abs import carac

    habilete = carac.Carac("Habileté", random.randint(7, 12))
    endurance = carac.Carac("Endurance", 12 + random.randint(1, 6) + random.randint(1, 6))
    maxEndurance = endurance.m_Valeur
    chance = carac.Carac("Chance", 6 + random.randint(1, 6))
    maxChance = chance.m_Valeur
    repas = carac.Carac("Repas", 10)

    flechesSaule = carac.Carac("Flèches de saule", 0)
    flechesHarpon = carac.Carac("Flèches harpon", 0)
    flechesPerforantes = carac.Carac("Flèches perforantes", 0)
    flechesHurleuses = carac.Carac("Flèches hurleuses", 0)

    disciplineKyujutsu = "Kyujutsu"
    disciplineIaijutsu = "Iaijutsu"
    disciplineKarumijutsu = "Karumijutsu"
    disciplineNitoKenjutsu = "Ni-to-Kenjutsu"

    def DisciplineAleatoire():
        global disciplineKyujutsu, disciplineIaijutsu, disciplineKarumijutsu, disciplineNitoKenjutsu
        val = random.randint(1, 4)
        discipline = "tmp"
        if val == 1:
            discipline = disciplineKyujutsu
        elif val == 2:
            discipline = disciplineIaijutsu
        elif val == 3:
            discipline = disciplineKarumijutsu
        elif val == 4:
            discipline = disciplineNitoKenjutsu

        caracDiscipline = carac.Carac("Discipline", discipline)
        return caracDiscipline

    discipline = DisciplineAleatoire()

    # arc :
    def Kyujutsu():
        global discipline, disciplineKyujutsu, flechesSaule, flechesHarpon, flechesPerforantes, flechesHurleuses
        flechesSaule.m_Valeur = 3
        flechesHarpon.m_Valeur = 3
        flechesPerforantes.m_Valeur = 3
        flechesHurleuses.m_Valeur = 3
        discipline = carac.Carac("Discipline", disciplineKyujutsu)

    def Iaijutsu():
        global discipline, disciplineIaijutsu
        discipline = carac.Carac("Discipline", disciplineIaijutsu)

    def Karumijutsu():
        global discipline, disciplineKarumijutsu
        discipline = carac.Carac("Discipline", disciplineKarumijutsu)

    def NitoKenjutsu():
        global discipline, disciplineNitoKenjutsu
        discipline = carac.Carac("Discipline", disciplineNitoKenjutsu)
