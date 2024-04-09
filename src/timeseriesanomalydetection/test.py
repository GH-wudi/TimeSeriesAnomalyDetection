import pandas as pd

df = pd.read_csv("D:\\Code\\Al\\TimeSeriesAnomalyDetection\\data\\负荷数据合集-20231219-rep.csv")
df_all = df[df['指标名称']=='A市地区全社会总电量']
# s_train=s_train.drop(columns=["0"])
# s_train=s_train.drop(columns=["系统"])
# s_train=s_train.drop(columns=["标号"])
# s_train=s_train.drop(columns=["指标名称"])
# s_train=s_train.drop(columns=["序号"])
df_all.to_csv('D:\\Code\\Al\\TimeSeriesAnomalyDetection\\data\\A市地区全社会总电量.csv')
