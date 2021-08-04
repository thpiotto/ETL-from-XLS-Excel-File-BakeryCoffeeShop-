def do_nothing():
    """
    Literally does nothing.
    Use it, with some moderation, only when you need it (:
    """
    
    pass

def brazil_currency_notation(_):
    """
    Switch to Latin currency notation.

    EXPLANATION: Some Latin countries use comma to separate floating points.
    """
    return str(_).replace('.', ',')