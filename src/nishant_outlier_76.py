import pandas as pd
import numpy as np

def remove_outliers(incsv_filename, outcsv_filename,threshold):

    dataset = pd.read_csv(incsv_filename)
    data = dataset.iloc[:,1:]
    shape=np.shape(data)
    rows=shape[0]
    columns=shape[1] 
    outliers=[]
    for col in range(columns):
        mean = np.mean(data.iloc[:,col])
        std = np.std(data.iloc[:,col])
        for row in range(rows):
            z_score = (data.iloc[row,col]-mean)/std
            if np.abs(z_score)>threshold:
                if row not in outliers:
                	outliers.append(row)
    dataset=dataset.drop(outliers)            
    dataset.to_csv(outcsv_filename, index=False)
    print ('The no of rows removed:',len(data) - len(dataset))

def row_elimination(file1):
	df=pd.read_csv(file1)
	data=df.iloc[:,1:]
	shape=np.shape(data)
	rows=shape[0]
	columns=shape[1]
	lb=[]
	ub=[]
	for i in range(columns):
		quar1,quar3=np.percentile(sorted(data.iloc[:,i]),[25,75])
		iqr=quar3-quar1
		lb.append((quar1-1.5*iqr))
		ub.append((quar3+1.5*iqr))
	outliers=[]
	for i in range(columns):
		for j in range(rows):
			if(data.iloc[j,i]<lb[i] or data.iloc[j,i]>ub[i]):
				if j not in outliers:
					outliers.append(j+1)
	print('No. of rows removed : ',len(outliers))
	print('Rows removed are : ',outliers)
	return outliers

def remove_outliers_iqr(file1,file2):
	df=pd.read_csv(file1)
	df=df.iloc[:,1:]
	outliers=row_elimination(file1)
	shape=np.shape(df)
	rows=shape[0]
	df_n=pd.DataFrame()
	for i in range(rows):
		if i+1 not in outliers:
			df_n=df_n.append(df.iloc[i,:])
	df_n=df_n.reset_index(drop=True)
	new_IDs=[]
	for i in range(rows-len(outliers)):
		new_IDs.append(i+1)
	new_IDs=pd.Series(new_IDs)
	df_n=pd.concat([new_IDs,df_n],axis=1)
	df_n.to_csv(file2, index=False)
	print('New Dataset : ')
	print(df_n)
