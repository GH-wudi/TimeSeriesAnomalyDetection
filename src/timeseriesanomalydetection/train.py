import pandas as pd
from adtk.data import validate_series
from adtk.visualization import plot
import matplotlib.pyplot as plt
from adtk.detector import SeasonalAD

s_train = pd.read_csv("D:\\Code\\Al\\TimeSeriesAnomalyDetection\\data\\A市地区全社会总电量.csv", index_col="读取时间", parse_dates=True)
s_train = s_train.loc[:,['指标值']]
# print(s_train)

s_train = validate_series(s_train)
seasonal_ad = SeasonalAD()
anomalies = seasonal_ad.fit_detect(s_train)
plot(s_train, anomaly=anomalies, anomaly_color="red", anomaly_tag="marker")
# plot(s_train)
plt.show()