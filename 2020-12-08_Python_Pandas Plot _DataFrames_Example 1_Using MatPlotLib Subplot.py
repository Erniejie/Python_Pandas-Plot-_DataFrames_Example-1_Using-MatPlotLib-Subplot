#Pandas Plot - How to Use the MatPlotLib Subplot function-6th Nov 2018 Tutorial

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#pd.__version__
df = pd.DataFrame({"key":[215,196,123,150]})
print(df)
#% matplotlib inline :NOTE:this inbuilt function I think is available on jupyternotebook
df["Deflection"] =10
print(df.plot())

plt.show()
