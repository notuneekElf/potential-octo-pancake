import pandas as pd;
import seaborn as sns;
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
df=pd.read_csv(r"C:\Python39\Datasets\bitcoin_dataset.csv")
df1=df.fillna(df.mean())
df2=df1.corr()
sns.heatmap(df2)
plt.show()