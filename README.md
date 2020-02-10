# Library for removing outliers from pandas dataframe

```
PROJECT 2, UCS633 - Data Analysis and Visualization
Nishant Goel  
COE17
Roll number: 101703376
```
Takes two inputs - filename of input csv, intended filename of output csv.

Output is the number of rows removed from the input dataset.It also shows new dataset in case of IQR

Output is the number of rows removed from the input dataset in case of z-score

## Installation
`pip install nishant_outlier_76`

*Recommended - test in a virtual environment.* 

## Use via command line
```
outliers_cli in.csv out.csv
outliers_cli in.csv out.csv 1.5
```

First argument after outcli is the input csv filename from which the dataset is extracted. The second argument is for storing the final dataset after processing.

## Use in .py script
```
from nishant_outlier_76 import remove_outliers_iqr
remove_outliers('input.csv', 'output.csv')
```
```
from nishant_outlier_76 import remove_outliers
remove_outliers('input.csv', 'output.csv',threshold)
```
