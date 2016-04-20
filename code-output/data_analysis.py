import pandas as pd
import numpy
import seaborn
import matplotlib.pyplot as plt
import math
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi
import scipy.stats

data = pd.read_csv('marscrater_pds.csv', low_memory=False)

# ------------ to create the subsets of craters which are located in north-western, north-eastern,
# south-western, and south-eastern quadrants -------------------------------------
n_w = data[(data["LATITUDE_CIRCLE_IMAGE"] >= 0) & (data["LONGITUDE_CIRCLE_IMAGE"] < 0)]
n_e = data[(data["LATITUDE_CIRCLE_IMAGE"] > 0) & (data["LONGITUDE_CIRCLE_IMAGE"] >= 0)]
s_w = data[(data["LATITUDE_CIRCLE_IMAGE"] < 0) & (data["LONGITUDE_CIRCLE_IMAGE"] <= 0)]
s_e = data[(data["LATITUDE_CIRCLE_IMAGE"] <= 0) & (data["LONGITUDE_CIRCLE_IMAGE"] > 0)]
# ------------ to create a new table with a column that indicates to which hemisphere a crater belongs ---------
n_w['HEMISPH'] = 'nw'
n_e['HEMISPH'] = 'ne'
s_w['HEMISPH'] = 'sw'
s_e['HEMISPH'] = 'se'

frames = [n_w, n_e, s_w, s_e]
new_data = pd.concat(frames)

# # ------------- Hypothesis Testing and ANOVA ------------------------------------------------------------

# # ------------- to use ols function for calculating the F-statistic and associated p-value ---------------
# model1 = smf.ols(formula="DIAM_CIRCLE_IMAGE ~ C(HEMISPH)", data=new_data)
# results1 = model1.fit()
# print(results1.summary())
#
# sub = new_data[['DIAM_CIRCLE_IMAGE', 'HEMISPH']]
# print("\nMeans for craters' diameters by quadrant of Mars")
# print(sub.groupby('HEMISPH').mean())
# print("\nStandard deviations for craters' diameters by quadrant of Mars")
# print(sub.groupby('HEMISPH').std(), '\n')
#
# # ------------- to perform Post hoc test (using Tukey's Honestly Significant Difference Test) -------------------------
# mc1 = multi.MultiComparison(sub['DIAM_CIRCLE_IMAGE'], sub['HEMISPH'])
# res1 = mc1.tukeyhsd()
# print(res1.summary())


# -------------------- Chi Square Test of Independence ---------------------------------------

# print(pd.isnull(data["NUMBER_LAYERS"]).any())
# contingency table of every number of layers vs every quadrant
ct1 = pd.crosstab(new_data['NUMBER_LAYERS'], new_data['HEMISPH'])
print(ct1)
# column percentages
colsum = ct1.sum(axis=0)
print(ct1/colsum)
# chi-square
cs1 = scipy.stats.chi2_contingency(ct1)
print(cs1)

# recode layer numbers into 2 groups: {0,1}, {2,3,4,5}
print('\n-------------We recoded the layers` numbers into 2 groups: {0,1} and {2,3,4,5}------------')
recode = {0: 0, 1: 0, 2:1, 3:1, 4:1, 5:1}
new_data['lay'] = new_data['NUMBER_LAYERS'].map(recode)
# print contingency, percentages, and chi-square for the recoded data
ct1 = pd.crosstab(new_data['lay'], new_data['HEMISPH'])
print(ct1)
colsum = ct1.sum(axis=0)
print(ct1/colsum)
cs1 = scipy.stats.chi2_contingency(ct1)
print(cs1)

# now make post hoc tests for each pair of quadrants
print('\n-------------Post hoc test for nw-vs-ne quadrant------------')
recode1 = {'nw': 'nw', 'ne': 'ne'}
new_data['q'] = new_data['HEMISPH'].map(recode1)
ct1 = pd.crosstab(new_data['lay'], new_data['q'])
print(ct1)
colsum = ct1.sum(axis=0)
print(ct1/colsum)
cs1 = scipy.stats.chi2_contingency(ct1)
print(cs1)

print('\n-------------Post hoc test for nw-vs-se quadrant------------')
recode1 = {'nw': 'nw', 'se': 'se'}
new_data['q'] = new_data['HEMISPH'].map(recode1)
ct1 = pd.crosstab(new_data['lay'], new_data['q'])
print(ct1)
colsum = ct1.sum(axis=0)
print(ct1/colsum)
cs1 = scipy.stats.chi2_contingency(ct1)
print(cs1)

print('\n-------------Post hoc test for nw-vs-sw quadrant------------')
recode1 = {'nw': 'nw', 'sw': 'sw'}
new_data['q'] = new_data['HEMISPH'].map(recode1)
ct1 = pd.crosstab(new_data['lay'], new_data['q'])
print(ct1)
colsum = ct1.sum(axis=0)
print(ct1/colsum)
cs1 = scipy.stats.chi2_contingency(ct1)
print(cs1)

print('\n-------------Post hoc test for ne-vs-se quadrant------------')
recode1 = {'ne': 'ne', 'se': 'se'}
new_data['q'] = new_data['HEMISPH'].map(recode1)
ct1 = pd.crosstab(new_data['lay'], new_data['q'])
print(ct1)
colsum = ct1.sum(axis=0)
print(ct1/colsum)
cs1 = scipy.stats.chi2_contingency(ct1)
print(cs1)

print('\n-------------Post hoc test for ne-vs-sw quadrant------------')
recode1 = {'ne': 'ne', 'sw': 'sw'}
new_data['q'] = new_data['HEMISPH'].map(recode1)
ct1 = pd.crosstab(new_data['lay'], new_data['q'])
print(ct1)
colsum = ct1.sum(axis=0)
print(ct1/colsum)
cs1 = scipy.stats.chi2_contingency(ct1)
print(cs1)

print('\n-------------Post hoc test for se-vs-sw quadrant------------')
recode1 = {'se': 'se', 'sw': 'sw'}
new_data['q'] = new_data['HEMISPH'].map(recode1)
ct1 = pd.crosstab(new_data['lay'], new_data['q'])
print(ct1)
colsum = ct1.sum(axis=0)
print(ct1/colsum)
cs1 = scipy.stats.chi2_contingency(ct1)
print(cs1)

# graph percent with layers >= 2 within each quadrant
seaborn.factorplot(x='HEMISPH', y='lay', data= new_data, kind='bar', ci=None)
plt.xlabel("Quadrants of Mars: north-western, north-eastern, south-western, and south-eastern")
plt.ylabel("Percent of craters with 2 or more layers")
plt.title("Percent of craters with 2 or more layers per each quadrant of Mars")
plt.show()