import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
import json

dirpath = r'./media_competetions_train/'
used_features_num = [9, 12, 13, 16, 19, 22, 23, 24, 27, 45, 60, 79, 80, 81]

raw_data = pd.read_csv(dirpath + 'type-four-0-150000-samples.csv',sep = ',', \
						 low_memory = False)

# print(raw_data.iloc[0:10,9:88])

numid = len(raw_data)
print('total indices: {}'.format(numid))
numcol = raw_data.columns.size
print('total columns: {}'.format(numcol))


column_headers = raw_data.columns.values.tolist()
print(column_headers)
# ids = list( range(0, len(column_headers)) )
# dictc = dict(zip(ids, column_headers))
# print(json.dumps(dictc, indent=4, ensure_ascii=False))

used_features = raw_data.columns[used_features_num].tolist()
print(used_features)

data = np.array(raw_data.iloc[:, used_features_num].values)

for i in range(0,len(used_features_num)):
	print("info of {} : ".format(used_features[i]))
	print("min:{}  max:{}  avg:{}  ".format(data[i].min(), data[i].max(), data[i].mean()))





# columnsToEncode = list(data.columns.values)
# print(columnsToEncode)
# assert len(columnsToEncode) == 79


# le = LabelEncoder()

# for feature in columnsToEncode:
# 	try:
# 		data[feature] = le.fit_transform(data[feature])
# 		# print(data[feature])
# 	except:
# 		print ('error in \"' + str(feature) + '\" ')

# print(data)


# Encode a numeric column as zscores
def encode_numeric_zscore(df, name, mean=None, sd=None):
    if mean is None:
        mean = df[name].mean()

    if sd is None:
        sd = df[name].std()

    df[name] = (df[name] - mean) / sd