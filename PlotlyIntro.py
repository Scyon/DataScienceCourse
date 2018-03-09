import numpy as np
import pandas as pd
import cufflinks as cf
import plotly.plotly
from plotly.offline import download_plotlyjs, iplot

cf.go_offline()
df = pd.DataFrame(data=np.random.randm(100, 4), columns='A B C D'.split())
print(df.head())