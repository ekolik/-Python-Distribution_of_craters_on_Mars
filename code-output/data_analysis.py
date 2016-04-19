import pandas as pd
import numpy
import seaborn
import matplotlib.pyplot as plt
import math
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi

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


# ------------- to use ols function for calculating the F-statistic and associated p-value ---------------
model1 = smf.ols(formula="DIAM_CIRCLE_IMAGE ~ C(HEMISPH)", data=new_data)
results1 = model1.fit()
print(results1.summary())

sub = new_data[['DIAM_CIRCLE_IMAGE', 'HEMISPH']]
print("\nMeans for craters' diameters by quadrant of Mars")
print(sub.groupby('HEMISPH').mean())
print("\nStandard deviations for craters' diameters by quadrant of Mars")
print(sub.groupby('HEMISPH').std(), '\n')

# ------------- to perform Post hoc test (using Tukey's Honestly Significant Difference Test) -------------------------
mc1 = multi.MultiComparison(sub['DIAM_CIRCLE_IMAGE'], sub['HEMISPH'])
res1 = mc1.tukeyhsd()
print(res1.summary())