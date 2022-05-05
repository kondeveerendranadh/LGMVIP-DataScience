import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sklearn

if 'model_selection' in dir(sklearn):
    print(True)
else:
    print(False)