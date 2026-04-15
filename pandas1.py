import pandas as pd
import numpy
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
mydataset = pd.DataFrame(mydataset)

print(mydataset)
print(type(mydataset))
mydataset.to_csv('mydata.csv')
#mydataset.to_csv('mydata2.csv',index=False)
print(mydataset.head(2))
print(mydataset.tail(1))
print(mydataset.describe())
mydata2=pd.read_csv('mydata2.csv')
mydata2['cars'][1]='jgj'
mydata2.to_csv('mydata2.csv')

print(pd.Series(numpy.random.rand(45)))