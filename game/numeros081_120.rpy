






label numero94:
    "Vous avancez à grands pas le long de la galerie, bien décidé à en finir une fois pour toutes avec Ikiru. Du trône vous parvient un rire macabre qui vous fait courir un frisson le long de l'échiné."
    "La sombre silhouette se lève et gesticule au-dessus du puits. C'est alors qu'à votre grande horreur, vous en voyez surgir une masse ténébreuse qui prend peu à peu forme sous vos yeux."
    "C'est une créature d'apparence vaguement humaine, mais pourvue de cornes sur la tête et de longues griffes acérées en guise de doigts : c'est un Démon de l'Ombre, un être semi-corporel issu du Monde Inférieur. Vous devez le combattre :"
    "Chaque fois que vous réussirez à frapper cet adversaire très particulier, lancez un dé. Si vous obtenez un chiffre pair, la blessure infligée lui coûtera 2 points d'ENDURANCE. Si le chiffre obtenu est impair, votre lame n'aura fait qu'érafler sa chair inconsistante et il ne perdra que 1 seul point d'ENDURANCE."
    $ nouveauCombat(True)
    $ AjouterEnnemi("DÉMON DE L'OMBRE", 9, 10)
    $ SetDoublePourBlesser()
    $ CommencerCombat("numero260")





label numero98:
    "Vous vous trouvez sur un monticule de terre meuble. Tout autour de vous s'étend un grand marécage dont les eaux troubles et puantes se soulèvent en faisant de grosses bulles."
    "Seuls quelques arbres torses et diverses variétés de plantes aquatiques ont réussi à s'extirper de ce cloaque. Derrière vous, la porte reconduisant au Centre des Univers flotte entre ciel et eau."
    "Soudain, un gigantesque serpent jaillit du bourbier en fouettant l'air à grands coups de tête, prêt à vous couper le corps en deux. Ses yeux luisent comme deux diamants noirs."
    menu:
        "Si vous voulez attaquer ce monstrueux reptile":
            jump numero246
        "Si vous préférez vous servir d'un objet spécial pour le neutraliser":
            jump numero258
