import pandas as pd
import numpy as np
import scipy.stats as stats

#Question 1

#A is the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.

pd.set_option('display.precision', 2)
data = pd.read_csv('assets/NISPUF17.csv')     
data = data.set_index(data.columns[0])
a = len(data['EDUC1'])
rqd = data['EDUC1'].value_counts().sort_index()     # distinct counts
rqd = rqd.rename(index={1:'less than high school', 2:'high school', 3:'more than high school but not college', 4:'college'})
rqd = rqd.div(a).apply(lambda x: round(x,1))
A = dict(rqd)

# Question 2

#Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. 

# The code below returns a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.

bf1 = data[data['CBF_01']==1]   #who had breastmilk
nbf1 = data[data['CBF_01']==2]  #no breastmilk
X = bf1['P_NUMFLU'].dropna()
AA = X.sum()/len(X)                 # average of breastfed vaccines
Y = nbf1['P_NUMFLU'].dropna()
BB = Y.sum()/len(Y)                 # average of non-breastfed vaccines
tup = (AA,BB)


# Question 3

#Let's see if there is any evidence of a link between vaccine effectiveness and sex of the child. Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex.

rqd1_male=len(data[(data['P_NUMVRC']>=1) & (data['HAD_CPOX']==1) & (data['SEX']==1)])    # acquired chicken pox, male 
drqd1_male=len(data[(data['P_NUMVRC']>=1) & (data['HAD_CPOX']==2) & (data['SEX']==1)])   # didn't acquire chicken pox, male
rqd1_female=len(data[(data['P_NUMVRC']>=1) & (data['HAD_CPOX']==1) & (data['SEX']==2)])  # acquired chicken pox, female
drqd1_female=len(data[(data['P_NUMVRC']>=1) & (data['HAD_CPOX']==2) & (data['SEX']==2)]) # didn't acquire chicken pox, female
ratio = {"male":rqd1_male/drqd1_male,"female":rqd1_female/drqd1_female}                  # ratio

#Question 4

#Calculate correlation between the use of the vaccine and whether it results in prevention of the infection or disease. Here, we calculate the correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).

cpox = data[((data['HAD_CPOX']==1) | (data['HAD_CPOX']==2)) & (data['P_NUMVRC'].notnull())]['HAD_CPOX']    # filtering out chicken pox column
vcn = data[((data['HAD_CPOX']==1) | (data['HAD_CPOX']==2)) & (data['P_NUMVRC'].notnull())]['P_NUMVRC']     # filetring out the number of vaccines received column
corr1, pval1=stats.pearsonr(cpox,vcn)                                                                      # Pearson correlation, i.e. linear correlation


