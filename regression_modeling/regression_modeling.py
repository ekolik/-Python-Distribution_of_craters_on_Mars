import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

new_data = pd.read_csv('marscrater_pds.csv', low_memory=False)

scat0 = seaborn.regplot(x="DEPTH_RIMFLOOR_TOPOG", y="NUMBER_LAYERS", fit_reg=True, data=new_data)
plt.xlabel("Crater's depth, km")
plt.ylabel("Number of layers in a crater, km")
plt.title("Association between crater's depth and its number of layers")
plt.show()

# ----------- centering the explanatory variable by subrtacting the mean
depth_mean = new_data["DEPTH_RIMFLOOR_TOPOG"].mean()
print("mean of the depth variable = ", depth_mean)
new_data["DEPTH_RIMFLOOR_TOPOG"] = new_data["DEPTH_RIMFLOOR_TOPOG"] - depth_mean
print("mean of the depth variable after normalization = ", new_data["DEPTH_RIMFLOOR_TOPOG"].mean())

print ("OLS regression model for the association between crater's depth and its number of layers")
model1 = smf.ols(formula="NUMBER_LAYERS ~ DEPTH_RIMFLOOR_TOPOG", data=new_data)
results1 = model1.fit()
print(results1.summary())