import pandas as pd
import numpy as np
from pydantic import BaseModel

def this_is_a_test_function(a, b):
    if isinstance(a, int) or isinstance(b, int): # This comment should resemble a way to long line so+
        return a + b
    else:
        return int(a) + int(b)