import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm

new_data = pd.read_csv('marscrater_pds.csv', low_memory=False)
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


#___________________________________ Multiple Regression___________________________________________

# # run the second order fit line
# scat1 = seaborn.regplot(x="DIAM_CIRCLE_IMAGE", y="DEPTH_RIMFLOOR_TOPOG", fit_reg=True, order = 2, data=new_data)
# plt.xlabel("Crater's diameter, km")
# plt.ylabel("Crater's depth, km")
# plt.title("Association between crater's diameter and depth")
# plt.show()

# center quantitative IVs for regression analysis
new_data['DIAM_CIRCLE_IMAGE'] = (new_data['DIAM_CIRCLE_IMAGE'] - new_data['DIAM_CIRCLE_IMAGE'].mean())
new_data['NUMBER_LAYERS'] = (new_data['NUMBER_LAYERS'] - new_data['NUMBER_LAYERS'].mean())
print(new_data[["DIAM_CIRCLE_IMAGE", "NUMBER_LAYERS"]].describe())

# linear regression analysis
print ("\nOLS regression model for the association between crater's diameter and depth")
model1 = smf.ols(formula="DEPTH_RIMFLOOR_TOPOG ~ DIAM_CIRCLE_IMAGE", data=new_data)
results1 = model1.fit()
print(results1.summary())

# polynomial regression analysis
print ("\nOLS polynomial regression model for the association between crater's diameter and depth")
model1 = smf.ols(formula="DEPTH_RIMFLOOR_TOPOG ~ DIAM_CIRCLE_IMAGE + I(DIAM_CIRCLE_IMAGE**2)", data=new_data)
results1 = model1.fit()
print(results1.summary())

# adding another explanatory variable
print ("\nOLS polynomial and multivariate regression model")
model1 = smf.ols(formula="DEPTH_RIMFLOOR_TOPOG ~ DIAM_CIRCLE_IMAGE + I(DIAM_CIRCLE_IMAGE**2) + NUMBER_LAYERS", data=new_data)
results1 = model1.fit()
print(results1.summary())

# # q-q plot for normality
# qq = sm.qqplot(results1.resid, line = 'r')
# plt.show()

# # plot of residuals
# stdres = pd.DataFrame(results1.resid_pearson)
# plt.plot(stdres, 'o', ls = 'None')
# l = plt.axhline(y=0, color = 'r')
# plt.ylabel('Standardized redisual')
# plt.xlabel('Observation number')
# plt.show()

# # diagnostic plots
# # figure1 = plt.figure(figsize=(12, 8))
# # figure1 = sm.graphics.plot_regress_exog(results1, "NUMBER_LAYERS", fig = figure1)
# # plt.show()
#
# figure1 = plt.figure(figsize=(12, 8))
# figure1 = sm.graphics.plot_regress_exog(results1, "DIAM_CIRCLE_IMAGE", fig = figure1)
# plt.show()

# leverage plot
figure1 = sm.graphics.influence_plot(results1, size=8)
plt.show()






