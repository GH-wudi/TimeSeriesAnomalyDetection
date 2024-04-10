from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from adtk.visualization import plot
from adtk.data import validate_series

path_list = glob('../../data/*.csv')
path_list.remove('../../data\\负荷数据合集-20231219-rep.csv')
# print(path_list)
for path in path_list:
    df = pd.read_csv(path, index_col="读取时间", parse_dates=True)
    df = df.loc[:,['指标值']]
    df = validate_series(df)
    plot(df)
    plt.savefig(path.replace('csv','png'))
    print(path)
# df = pd.read_csv("D:\\Code\\Al\\TimeSeriesAnomalyDetection\\data\\A市地区全社会总电量.csv", index_col="读取时间", parse_dates=True)

# df = df.loc[:,['指标值']]
# # plot(s_train)
# plt.show()