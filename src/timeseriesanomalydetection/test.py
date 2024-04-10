import pandas as pd

df = pd.read_csv("D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\负荷数据合集-20231219-rep.csv")
df_all = df[df['指标名称']=='A市地区全社会总电量']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市地区全社会总电量.csv')
df_all = df[df['指标名称']=='A市a县全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市a县全社会负荷.csv')
df_all = df[df['指标名称']=='A市b县全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市b县全社会负荷.csv')
df_all = df[df['指标名称']=='A市c县(不含d县供电公司)全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市c县(不含d县供电公司)全社会负荷.csv')
df_all = df[df['指标名称']=='A市c县全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市c县全社会负荷.csv')
df_all = df[df['指标名称']=='A市d县供电公司全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市d县供电公司全社会负荷.csv')
df_all = df[df['指标名称']=='A市e县市全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市e县市全社会负荷.csv')

df_all = df[df['指标名称']=='A市f县市全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市f县市全社会负荷.csv')

df_all = df[df['指标名称']=='A市g县县全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市g县县全社会负荷.csv')

df_all = df[df['指标名称']=='A市h县县全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市h县县全社会负荷.csv')

df_all = df[df['指标名称']=='A市i县县全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市i县县全社会负荷.csv')

df_all = df[df['指标名称']=='A市j县县全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市j县县全社会负荷.csv')

df_all = df[df['指标名称']=='A市k县市全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市k县市全社会负荷.csv')

df_all = df[df['指标名称']=='A市l县县全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市l县县全社会负荷.csv')

df_all = df[df['指标名称']=='A市m县县全社会负荷']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市m县县全社会负荷.csv')

df_all = df[df['指标名称']=='A市清洁能源出力(大屏展示)']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市清洁能源出力(大屏展示）.csv')

df_all = df[df['指标名称']=='A市全社会负荷(转省)']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市全社会负荷(转省).csv')

df_all = df[df['指标名称']=='f县市总电量']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\f县市总电量.csv')

df_all = df[df['指标名称']=='g县全网总有功电度']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\A市g县县全社会总电量.csv')

df_all = df[df['指标名称']=='j县县全社会口径电量']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\j县县全社会口径电量.csv')

df_all = df[df['指标名称']=='k县市全社会口径电量']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\k县市全社会口径电量.csv')

df_all = df[df['指标名称']=='n县电厂有功出力']
df_all.to_csv('D:\\Code\\python\\TimeSeriesAnomalyDetection\\data\\n县电厂有功出力.csv')
# s_train=s_train.drop(columns=["0"])
# s_train=s_train.drop(columns=["系统"])
# s_train=s_train.drop(columns=["标号"])
# s_train=s_train.drop(columns=["指标名称"])
# s_train=s_train.drop(columns=["序号"])

