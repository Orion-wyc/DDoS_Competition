import os
import numpy as np
import pandas as pd

BASEDIR = os.path.abspath('.')
DATASETPATH = BASEDIR + r'\media_competetions_train'


def getandcombine():
	count_files = 0
	for root, dirs, fnames in os.walk(DATASETPATH):
		for fname in fnames:
			print('reading ' + os.path.join(root,fname))
			df = pd.read_csv(os.path.join(root, fname), skipinitialspace=True, low_memory=False)
			if count_files==0:
				df.to_csv(BASEDIR + r'\combined_data.csv', encoding='utf-8', index=False, mode='a+')
				count_files += 1;
			else:	
				df.to_csv(BASEDIR + r'\combined_data.csv', encoding='utf-8', index=False, header=False, mode='a+')
	
	print('Finishing Combining...')



if __name__ == "__main__":
	print(BASEDIR + r'\combined_data.csv')
	getandcombine()