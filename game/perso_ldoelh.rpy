

#initialisation persos
init -1 python:
    import random
    from despin.abs import carac

    habilete = carac.Carac("Habileté", random.randint(7, 12))
    endurance = carac.Carac("Endurance", 12 + random.randint(1, 6) + random.randint(1, 6))
    maxEndurance = endurance.m_Valeur
    chance = carac.Carac("Chance", 6 + random.randint(1, 6))
    maxChance = chance.m_Valeur
