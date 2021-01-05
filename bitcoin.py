import pandas as pd;
import seaborn as sns;
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Python39\Datasets\bitcoin_dataset.csv")
df1=df.corr()
sns.heatmap(df1)
plt.show()