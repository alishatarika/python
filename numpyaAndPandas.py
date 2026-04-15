import pandas as pd
import numpy as np
import random

list=[]
result=[]
for i in range(1,11):
    list.append(i)
    result.append(i*i)
numbers_array = np.array(list)
squares_array = np.array(result)
data = {
    'Numbers': numbers_array,
    'Squares': squares_array
}
data = pd.DataFrame(data)
print(data)


data = {
    'Name': ["Alice", "Bob", "Charlie"],
    'Age': [24, 30, 22],
    'Salary': [50000, 60000, 40000]
}

data = pd.DataFrame(data)

myage_salary = np.array(data[['Name','Age', 'Salary']])

age_condition = myage_salary[:,1] > 25
salary_condition = myage_salary[:, 2] > 45000
combined_condition = age_condition & salary_condition
filterresult = myage_salary[combined_condition]
print(filterresult)


height={
    'Name':['Alice','Bob','Charlie'],
    'Height(cm)':[160,175,180]
}
height['Height(inches)'] = [h * 0.393701 for h in height['Height(cm)']]
df_height = pd.DataFrame(height)
print(df_height)



data = np.random.randint(1, 101, size=(5,3 ))
df = pd.DataFrame(data, columns=['a', 'b', 'c'])

print(df)
A = np.array(df['a'])
meanA=A.mean()
stA=A.std()
B = np.array(df['b'])
meanB=A.mean()
stB=B.std()
C= np.array(df['c'])
meanC=C.mean()
stC=C.std()

print("mean of a ,b and c is",meanA,meanB,meanC)
print("standard deviation of a ,b and c is",stA,stB,stC)


data2 = {
    'Name': ["Alice", "Bob", "Charlie"],
    'Age': [24, 'NAN', 22],
    'Score': [85, 90, 'NAN']
}
data2 = pd.DataFrame(data2)

data2 = data2.replace('NAN', np.nan)

age_mean = data2['Age'].astype(float).mean()
score_mean = data2['Score'].astype(float).mean()
data2['Age'].fillna(age_mean, inplace=True)
data2['Score'].fillna(score_mean, inplace=True)
new = data2[['Name', 'Age', 'Score']].to_numpy()


print(new)

