import pandas as pd;
import seaborn as sns;
import matplotlib.pyplot as plt
import datetime as dt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score
df=pd.read_csv(r"C:\Python39\Datasets\bitcoin_dataset.csv")
df1=df.fillna(df.mode())
df1['Date']=pd.to_datetime(df1.Date)
df1['Date']=df1['Date'].map(dt.datetime.toordinal)
X=pd.DataFrame(df1['btc_market_price'])
Y=pd.DataFrame(df1['btc_market_price'])
reg=linear_model.LinearRegression()
reg.fit(X,Y)
Y_pred=reg.predict(X)
rmse=mean_squared_error(Y,Y_pred)
print(rmse)
