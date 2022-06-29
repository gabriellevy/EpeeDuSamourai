init python:
    from abs.religions import religion
    from spe.humanite import pnj_spe
    from abs.humanite import metier
    from abs.humanite import pnj
    from abs.humanite import trait
    import random

    class SituationSpe(Situation):

        # Set the store.{prefix}.character_id value
        STORE_PREFIX = "stats_spe"

        # Boolean toggle for validation - defaults both True
        VALIDATE_VALUES = False
        COERCE_VALUES = False

        STAT_DEFAULTS = {
        }

        # def __init__(self, id, **kwargs):
        #     Situation.__init__(self, id, **kwargs)

        # -------------------------------------------------- temps -------------------------------------------------
        
