import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy

new_data = pd.read_csv('marscrater_pds.csv', low_memory=False)
#new_data = new_data.ix[:1000]
#
# # ______________________________ Basics of Linear Regression_____________________________________
#
# scat0 = seaborn.regplot(x="DEPTH_RIMFLOOR_TOPOG", y="NUMBER_LAYERS", fit_reg=True, data=new_data)
# plt.xlabel("Crater's depth, km")
# plt.ylabel("Number of layers in a crater, km")
# plt.title("Association between crater's depth and its number of layers")
# plt.show()
#
# # ----------- centering the explanatory variable by subrtacting the mean
# depth_mean = new_data["DEPTH_RIMFLOOR_TOPOG"].mean()
# print("mean of the depth variable = ", depth_mean)
# new_data["DEPTH_RIMFLOOR_TOPOG"] = new_data["DEPTH_RIMFLOOR_TOPOG"] - depth_mean
# print("mean of the depth variable after normalization = ", new_data["DEPTH_RIMFLOOR_TOPOG"].mean())
#
# print ("OLS regression model for the association between crater's depth and its number of layers")
# model1 = smf.ols(formula="NUMBER_LAYERS ~ DEPTH_RIMFLOOR_TOPOG", data=new_data)
# results1 = model1.fit()
# print(results1.summary())


# #___________________________________ Multiple Regression___________________________________________
#
# # # run the second order fit line
# # scat1 = seaborn.regplot(x="DIAM_CIRCLE_IMAGE", y="DEPTH_RIMFLOOR_TOPOG", fit_reg=True, order = 2, data=new_data)
# # plt.xlabel("Crater's diameter, km")
# # plt.ylabel("Crater's depth, km")
# # plt.title("Association between crater's diameter and depth")
# # plt.show()
#
# # center quantitative IVs for regression analysis
# new_data['DIAM_CIRCLE_IMAGE'] = (new_data['DIAM_CIRCLE_IMAGE'] - new_data['DIAM_CIRCLE_IMAGE'].mean())
# #new_data['NUMBER_LAYERS'] = (new_data['NUMBER_LAYERS'] - new_data['NUMBER_LAYERS'].mean())
# print(new_data[["DIAM_CIRCLE_IMAGE", "NUMBER_LAYERS"]].describe())
#
# # linear regression analysis
# print ("\nOLS regression model for the association between crater's diameter and depth")
# model1 = smf.ols(formula="DEPTH_RIMFLOOR_TOPOG ~ DIAM_CIRCLE_IMAGE", data=new_data)
# results1 = model1.fit()
# print(results1.summary())
#
# # polynomial regression analysis
# print ("\nOLS polynomial regression model for the association between crater's diameter and depth")
# model1 = smf.ols(formula="DEPTH_RIMFLOOR_TOPOG ~ DIAM_CIRCLE_IMAGE + I(DIAM_CIRCLE_IMAGE**2)", data=new_data)
# results1 = model1.fit()
# print(results1.summary())
#
# # adding another explanatory variable
# print ("\nOLS polynomial and multivariate regression model")
# model1 = smf.ols(formula="DEPTH_RIMFLOOR_TOPOG ~ DIAM_CIRCLE_IMAGE + I(DIAM_CIRCLE_IMAGE**2) + NUMBER_LAYERS", data=new_data)
# results1 = model1.fit()
# print(results1.summary())
#
# # # q-q plot for normality
# # qq = sm.qqplot(results1.resid, line = 'r')
# # plt.show()
#
# # # plot of residuals
# # stdres = pd.DataFrame(results1.resid_pearson)
# # plt.plot(stdres, 'o', ls = 'None')
# # l = plt.axhline(y=0, color = 'r')
# # plt.ylabel('Standardized redisual')
# # plt.xlabel('Observation number')
# # plt.show()
#
# # # diagnostic plots
# # figure1 = plt.figure(figsize=(12, 8))
# # figure1 = sm.graphics.plot_regress_exog(results1, "NUMBER_LAYERS", fig = figure1)
# # plt.show()
#
# # figure1 = plt.figure(figsize=(12, 8))
# # figure1 = sm.graphics.plot_regress_exog(results1, "DIAM_CIRCLE_IMAGE", fig = figure1)
# # plt.show()
#
# # # leverage plot
# # # the data is too big to pring the plot. to print plot with a subset of the data uncomment the line #new_data = new_data.ix[:1000]
# # # at the beginning of the code and retrain the model.
# # figure1 = sm.graphics.influence_plot(results1, size=8)
# # plt.show()


# ____________________________ Logistic Regression _____________________

# # examining the data before recoding
# print(new_data.groupby("DEPTH_RIMFLOOR_TOPOG").size())
#
# print(new_data.groupby("DIAM_CIRCLE_IMAGE").size())
# new_data["DIAM_Q"] = pd.qcut(new_data["DIAM_CIRCLE_IMAGE"], 4)
# print(new_data.groupby("DIAM_Q").size())
# print()


# recode layer numbers into 2 groups: 0:{0,1}, 1:{2,3,4,5}
recode = {0: 0, 1: 0, 2:1, 3:1, 4:1, 5:1}
new_data['lay_cat'] = new_data['NUMBER_LAYERS'].map(recode)


# recode depth into 2 groups: 0: <= 0 , 1: > 0
def depth(x):
   if x['DEPTH_RIMFLOOR_TOPOG'] <= 0:
      return 0
   else:
      return 1
new_data['depth_cat'] = new_data.apply(lambda x: depth(x), axis=1)


# recode diameter into 2 groups: 0: < 2 , 1: >= 2
def diameter(x):
   if x['DIAM_CIRCLE_IMAGE'] < 2:
      return 0
   else:
      return 1
new_data['diam_cat'] = new_data.apply(lambda x: diameter(x), axis=1)

# print(new_data.head(10))

#
# # logistic regression for depth -> number of layers
# print ("Logistic regression model for the association between crater's depth and number of layers")
# model1 = smf.logit(formula="lay_cat ~ depth_cat", data=new_data)
# results1 = model1.fit()
# print(results1.summary())
#
# # odds ratios
# print("\nOdds ratios")
# print(numpy.exp(results1.params))
#
# # odds ratios with 95% confidence intervals
# print("\nConfidence intervals")
# conf = results1.conf_int()
# conf['Odds ratio'] = results1.params
# conf.columns = ['Lower conf.int.', 'Upper conf.int.', 'Odds ratio']
# print(numpy.exp(conf))


# logistic regression for depth+diameter -> number of layers
print ("Logistic regression model for the association between crater's depth&diameter and number of layers")
model1 = smf.logit(formula="lay_cat ~ depth_cat + diam_cat", data=new_data)
results1 = model1.fit()
print(results1.summary())

# odds ratios with 95% confidence intervals
print("\nConfidence intervals")
conf = results1.conf_int()
conf['Odds ratio'] = results1.params
conf.columns = ['Lower conf.int.', 'Upper conf.int.', 'Odds ratio']
print(numpy.exp(conf))