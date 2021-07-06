import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

down= pd.read_csv('walk_down_final.csv', index_col=0)

plt.plot(down['gFx'])
plt.show