import numpy as np
import pandas as pd
import statsmodels.api as sm
import pdb
import math

df = pd.read_csv('historical_data1_Q32008_v3.csv')

def one(n):
	return 1
df['Constant'] = df['First_Pay_Date'].apply(one)

def T_F(n):
	if n == 0:
		return bool(False)
	else:
		return bool(True)

df['Deliq'] = df['Deliquency'].apply(T_F)

dfLP = pd.get_dummies(df['Loan_Purpose'], prefix='Loan_Purp')

df = pd.merge(df, dfLP, left_index=True, right_index=True)

cols_to_keep = ['Credit_Score', 'Orig_Combined_LTV', 'Orig_Debt_to_Income', 'Orig_Int_Rate', 'Loan_Purp_N']
Ind_Vars = df[cols_to_keep]

logit = sm.Logit(df['Deliq'], df[Ind_Vars])
result = logit.fit()
coeff = result.params
print result.summary()



#def calc_deliq(params, CreditScore, OrigCombinedLTV, OrigDebttoIncome, OrigUPB, OrigIntRate):
#	deliq = params['Constant'] + params['Credit_Score'] * CreditScore + params['Orig_Combined_LTV'] * OrigCombinedLTV + params['Orig_Debt_to_Income'] * OrigDebttoIncome + params['Orig_Int_Rate'] * OrigIntRate
#	return abs(deliq)
#def logistic_function_prob(deliq):
#	p = 1/(1 + math.exp(-(deliq)))
#	return p
##interest_rate = calc_int_rate(coeff, 735, 20000)
#print logistic_function_prob(deliq)

