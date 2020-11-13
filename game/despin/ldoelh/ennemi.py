# -*-coding:utf-8 -*

class Ennemi:
    """
    ennemi du joueur lors des combat avec ses caracs de combat de base
    """

    def __init__(self, nom, habilete, endurance):
        self.m_Nom = nom
        self.m_Habilete = habilete
        self.m_Endurance = endurance

    def __repr__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Carac '{}', Valeur '{}'".format(self.m_Id, self.m_Valeur)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        return "{} : Habilete {} - Endurance {}".format(self.m_Nom, self.m_Habilete, self.m_Endurance)
