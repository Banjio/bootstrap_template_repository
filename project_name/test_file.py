import pandas as pd
import numpy as np
from pydantic import BaseModel

def this_is_a_test_function(a: str, b: str) -> str:
    """Add number only numbers together and avoid merging strings. try casting

    Arguments:
        a {str} -- a number or string that can be converted to a number
        b {str} -- a number or string that can be converted to a number

    Returns:
        str -- added a and b
    """
    if isinstance(a, int) or isinstance(b, int): # This comment should resemble a way to long line so+
        return a + b
    else:
        return int(a) + int(b)