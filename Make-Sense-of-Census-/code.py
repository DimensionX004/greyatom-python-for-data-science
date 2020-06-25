# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record = [[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
#Step-1
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census = np.concatenate([data, new_record])
print(data.shape)
print(census.shape)

#Code starts here
#Step-2
age = census[:, 0]
max_age = max(age)
min_age = min(age)
age_mean = np.mean(age)
age_std = np.std(age)

#Step-3
r_0 = []
r_1 = []
r_2 = []
r_3 = []
r_4 = []
for i in census[:, 2]:
    if (i==0):
        r_0.append(i)
    elif (i==1):
        r_1.append(i)
    elif (i==2):
        r_2.append(i)
    elif (i==3):
        r_3.append(i)
    elif (i==4):
        r_4.append(i)

race_0 = np.array(r_0)
race_1 = np.array(r_1)
race_2 = np.array(r_2)
race_3 = np.array(r_3)
race_4 = np.array(r_4)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

min_len = len_0
minority_race = 0
if(min_len>len_1):
    min_len=len_1
    minority_race = 1
if(min_len>len_2):
    min_len=len_2
    minority_race = 2
if(min_len>len_3):
    min_len=len_3
    minority_race = 3
if(min_len>len_4):
    min_len=len_4
    minority_race = 4

print("Minority Race :", minority_race)

#Step-4
senior_citizens = np.array(age[age>60])
working_hours_sum = 0
for i in range(len(age)):
    if(age[i]>60):
        working_hours_sum = working_hours_sum + census[:,6][i]
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
avg_working_hours = (working_hours_sum/senior_citizens_len)
print(avg_working_hours)

#Step-5
high = np.array(census[:,1][census[:,1]>10])
low = np.array(census[:,1][census[:,1]<=10])

high_low = census[:,1]
sum_high = 0
sum_low = 0
for i in range(len(high_low)):
    if(high_low[i]>10):
        sum_high = sum_high + census[:,7][i]
    elif(high_low[i]<=10):
        sum_low = sum_low + census[:,7][i]

avg_pay_high = sum_high/len(high)
avg_pay_low = sum_low/len(low)
print(avg_pay_high) 
print(avg_pay_low)


