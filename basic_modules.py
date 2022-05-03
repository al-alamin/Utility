import warnings
warnings.filterwarnings('always')
warnings.simplefilter('always')
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
import glob, os, sys
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
import csv
import pickle
import math
import os
import traceback
from datetime import datetime
from numpy import random

try:
    import tensorflow as tf
except ImportError:
    traceback.print_exc()
    

try:
    import openai
except ImportError:
    traceback.print_exc()

try:
    from sklearn.model_selection import StratifiedKFold
except ImportError:
    traceback.print_exc()


try:
    import matplotlib.pylab as plt
except ImportError:
    traceback.print_exc()

# try:
#     import 
# except ImportError:
#     traceback.print_exc()

print("Basic modules loaded successfully.")

