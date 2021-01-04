import pandas as pd;
import seaborn as sns;
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Python39\Datasets\bitcoin_dataset.csv")
df1=sns.load_dataset("df")
sns.jointplot(x="x_corr",y="y_corr",data=df)
plt.show()