def greetings(who:str='there') -> str:
    """ Greetings
    This is a greeting function!

    Parameters
    ----------
    who : str
        Who to greet

    Returns
    -------
    str
        Greetings
    """
    greet='Hi ' + who + '!'
    print(greet)
    return greet