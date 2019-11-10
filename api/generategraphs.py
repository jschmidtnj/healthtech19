import pandas as pd
import seaborn as sns
import numpy as np


d = {1:np.random.randint(11,size=18),
        2:np.random.randint(11,size=18),
        3:np.random.randint(11,size=18),
        4:np.random.randint(11,size=18),
        5:np.random.randint(11,size=18),
        6:np.random.randint(11,size=18),
        7:np.random.randint(11,size=18),
        8:np.random.randint(11,size=18),
        9:np.random.randint(11,size=18),
        10:np.random.randint(11,size=18),
        11:np.random.randint(11,size=18),
        12:np.random.randint(11,size=18),
        13:np.random.randint(11,size=18),
        14:np.random.randint(11,size=18),
        15:np.random.randint(11,size=18),
        16:np.random.randint(11,size=18),
        17:np.random.randint(11,size=18),
        18:np.random.randint(11,size=18),
        19:np.random.randint(11,size=18),
        20:np.random.randint(11,size=18),
        21:np.random.randint(11,size=18),
        22:np.random.randint(11,size=18),
        23:np.random.randint(11,size=18),
        24:np.random.randint(11,size=18),
        25:np.random.randint(11,size=18),
        26:np.random.randint(11,size=18),
        27:np.random.randint(11,size=18),
        28:np.random.randint(11,size=18),
        29:np.random.randint(11,size=18),
        30:np.random.randint(11,size=18)}

def lineplot(data=d):
    df = pd.DataFrame.from_dict(data)
    df = df.transpose()
    df['average'] = df.mean(numeric_only=True, axis=1)
    lineplot = sns.lineplot(data=df['average'], label="Average Pain Over Time")
    figure = lineplot.get_figure()
    figure.savefig('output.png')
    return figure
    