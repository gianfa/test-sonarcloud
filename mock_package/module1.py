from typing import Any


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
    lambda printa: print("this is a code smell")
    lambda printa_2: print("this is another code smell")  
    return greet

def broken_function(var: Any):
    """ This is just broken"""
    if 