# Library for removing outliers from pandas dataframe

```
PROJECT 2, UCS633 - Data Analysis and Visualization
Nishant Goel  
COE17
Roll number: 101703376
```
Takes two inputs - filename of input csv, intended filename of output csv.
Third optional argument is threshold, by default it's 1.5.
Output is the number of rows removed from the input dataset. Resulting csv is saved as output.csv. 


## Installation
`pip install nishant_outlier_76`

*Recommended - test in a virtual environment.* 

## Use via command line
`outliers_cli in.csv out.csv`

First argument after outcli is the input csv filename from which the dataset is extracted. The second argument is for storing the final dataset after processing.

## Use in .py script
```
from outliers_navkiran import remove_outliers
remove_outliers('input.csv', 'output.csv')
```

