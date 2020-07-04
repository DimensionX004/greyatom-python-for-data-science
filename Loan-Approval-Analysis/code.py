# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)

#Code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
#print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
#print(numerical_var)

banks = bank.drop(columns = 'Loan_ID')
#print(banks.isnull().sum())
bank_mode = banks.mode()
banks = banks.replace(to_replace = np.nan, value = bank_mode)
#print(banks.shape)
#print(banks.isnull().sum().values.sum())

avg_loan_amount = pd.pivot_table(banks, values = 'LoanAmount', index = ['Gender', 'Married', 'Self_Employed'], aggfunc = np.mean)
#print(avg_loan_amount['LoanAmount'][1],2)

loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].count()
#print(loan_approved_se)
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].count()
#print(loan_approved_nse)
Loan_Status = 614
percentage_se = (loan_approved_se/Loan_Status)*100
percentage_nse = (loan_approved_nse/Loan_Status)*100

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
#print(loan_term)
big_loan_term = loan_term[loan_term>=25].count()
#print(big_loan_term)

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values.iloc[1,0])



