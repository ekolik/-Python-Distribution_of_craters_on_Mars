import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import sklearn
from sklearn import preprocessing
from sklearn.linear_model import LassoLarsCV
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi


new_data = pd.read_csv('marscrater_pds.csv', low_memory=False)
#
# #__________________________Decision Trees__________________________________________
#
# # recode layer numbers into 2 groups: {0,1}, {2,3,4,5}. this would be the response variable
# recode = {0: 0, 1: 0, 2:1, 3:1, 4:1, 5:1}
# new_data['NUMBER_LAYERS'] = new_data['NUMBER_LAYERS'].map(recode)
#
# # round up the explanatory variables and subset the data
# new_data["DIAM_INT"] = new_data["DIAM_CIRCLE_IMAGE"].round()
# new_data["LATITUDE_CIRCLE_IMAGE"] = new_data["LATITUDE_CIRCLE_IMAGE"].round()
# new_data["LONGITUDE_CIRCLE_IMAGE"] = new_data["LONGITUDE_CIRCLE_IMAGE"].round()
# new_data = new_data.ix[:100]
#
# # split into training and testing sets
# predictors = new_data[["DIAM_INT", 'LATITUDE_CIRCLE_IMAGE', "LONGITUDE_CIRCLE_IMAGE"]]
# targets = new_data.NUMBER_LAYERS
#
# pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.4)
# pred_train.shape
# pred_test.shape
# tar_train.shape
# tar_test.shape
#
# # build model on training data
# classifier = DecisionTreeClassifier()
# classifier = classifier.fit(pred_train, tar_train)
#
# predictions = classifier.predict(pred_test)
#
# # print the confusion matrix and accuracy of the model
# print(sklearn.metrics.confusion_matrix(tar_test, predictions))
# print(sklearn.metrics.accuracy_score(tar_test, predictions))
#
# # export the tree for viewing
# export_graphviz(classifier, out_file="decision_tree.dot")
#
# # to view the decision tree create a .pdf file from the created .dot file
# # by typing in the terminal from this directory: dot -Tpdf decision_tree -o decision_tree.pdf

# #____________________________________Random Forests________________
#
# # recode layer numbers into 2 groups: {0,1}, {2,3,4,5}. this would be the response variable
# recode = {0: 0, 1: 0, 2:1, 3:1, 4:1, 5:1}
# new_data['NUMBER_LAYERS'] = new_data['NUMBER_LAYERS'].map(recode)
#
# # split into training and testing sets
# predictors = new_data[["DIAM_CIRCLE_IMAGE", 'DEPTH_RIMFLOOR_TOPOG']]
# targets = new_data.NUMBER_LAYERS
#
# pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.4)
#
# # build model on training data
#
#
# classifier = RandomForestClassifier(n_estimators=25)
# classifier = classifier.fit(pred_train, tar_train)
#
# predictions = classifier.predict(pred_test)
# # print the confusion matrix and accuracy of the model
# print('confusion matrix:\n', sklearn.metrics.confusion_matrix(tar_test, predictions))
# print('\naccuracy:', sklearn.metrics.accuracy_score(tar_test, predictions))
#
# # to display the relative importance of each predictive variable
# model = ExtraTreesClassifier()
# model.fit(pred_train, tar_train)
# print('importance of predictors:', model.feature_importances_)
#
# # run different numbers of trees to see the effect of the number on the accuracy of the prediction
# n = 10
# accuracy = [0]*n
#
# for i in range(n):
#     classifier = RandomForestClassifier(n_estimators=i+1)
#     classifier = classifier.fit(pred_train, tar_train)
#     predictions = classifier.predict(pred_test)
#     accuracy[i] = sklearn.metrics.accuracy_score(tar_test, predictions)
#
# # plt.plot(range(1, n+1), accuracy)
# # plt.xlabel("Number of trees")
# # plt.ylabel("Accuracy of prediction")
# # plt.title("Effect of the number of trees on the prediction accuracy")
# # plt.show()
#
# print(accuracy)


# #________________________________Lasso Regression__________________________________
#
# pre_preds = new_data[["LATITUDE_CIRCLE_IMAGE", "LONGITUDE_CIRCLE_IMAGE", "DIAM_CIRCLE_IMAGE", 'DEPTH_RIMFLOOR_TOPOG']]
# targets = new_data.NUMBER_LAYERS
#
# # standardize predictors to have mean=0 and sd=1
# predictors = pre_preds.copy()
# predictors["LATITUDE_CIRCLE_IMAGE"] = preprocessing.scale(predictors["LATITUDE_CIRCLE_IMAGE"].astype('float64'))
# predictors["LONGITUDE_CIRCLE_IMAGE"] = preprocessing.scale(predictors["LONGITUDE_CIRCLE_IMAGE"].astype('float64'))
# predictors["DIAM_CIRCLE_IMAGE"] = preprocessing.scale(predictors["DIAM_CIRCLE_IMAGE"].astype('float64'))
# predictors["DEPTH_RIMFLOOR_TOPOG"] = preprocessing.scale(predictors["DEPTH_RIMFLOOR_TOPOG"].astype('float64'))
# # print(predictors.head())
#
# # split into training and testing sets
# pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.3, random_state=123)
#
# # specify the lasso regression model
# model = LassoLarsCV(cv=10, precompute=False).fit(pred_train, tar_train)
#
# print('Predictors and their regression coefficients:')
# d = dict(zip(predictors.columns, model.coef_))
# for k in d:
#     print(k, ':', d[k])
#
# # plot coefficient progression
# m_log_alphas = -np.log10(model.alphas_)
# ax = plt.gca()
# plt.plot(m_log_alphas, model.coef_path_.T)
# # print(model.alpha_)
# plt.axvline(-np.log10(model.alpha_), linestyle="dashed", color='k', label='alpha CV')
# plt.ylabel("Regression coefficients")
# plt.xlabel("-log(alpha)")
# plt.title('Regression coefficients progression for Lasso paths')
# plt.show()
#
# # plot mean squared error for each fold
# m_log_alphascv = -np.log10(model.cv_alphas_)
# plt.plot(m_log_alphascv, model.cv_mse_path_, ':')
# plt.plot(m_log_alphascv, model.cv_mse_path_.mean(axis=-1), 'k', label='Average across the folds', linewidth=2)
# plt.legend()
# plt.xlabel('-log(alpha)')
# plt.ylabel('Mean squared error')
# plt.title('Mean squared error on each fold')
# plt.show()
#
# # Mean squared error from training and test data
# train_error = mean_squared_error(tar_train, model.predict(pred_train))
# test_error = mean_squared_error(tar_test, model.predict(pred_test))
# print('\nmean squared error for training data:', train_error)
# print('mean squared error for test data:', test_error)
#
# rsquared_train = model.score(pred_train, tar_train)
# rsquared_test = model.score(pred_test, tar_test)
# print('\nR-square for training data:', rsquared_train)
# print('R-square for test data:', rsquared_test)

# ______________________________K-Means Cluster Analysis_________________

# subset clustering variables
cluster = new_data[["LATITUDE_CIRCLE_IMAGE", "LONGITUDE_CIRCLE_IMAGE", "DIAM_CIRCLE_IMAGE", 'DEPTH_RIMFLOOR_TOPOG']]
# standardize predictors to have mean=0 and sd=1
clustervar = cluster.copy()
clustervar["LATITUDE_CIRCLE_IMAGE"] = preprocessing.scale(clustervar["LATITUDE_CIRCLE_IMAGE"].astype('float64'))
clustervar["LONGITUDE_CIRCLE_IMAGE"] = preprocessing.scale(clustervar["LONGITUDE_CIRCLE_IMAGE"].astype('float64'))
clustervar["DIAM_CIRCLE_IMAGE"] = preprocessing.scale(clustervar["DIAM_CIRCLE_IMAGE"].astype('float64'))
clustervar["DEPTH_RIMFLOOR_TOPOG"] = preprocessing.scale(clustervar["DEPTH_RIMFLOOR_TOPOG"].astype('float64'))
# print(predictors.head())

# split into training and testing sets
clus_train, clus_test = train_test_split(clustervar, test_size=.3, random_state=123)

# # _________________k-means cluster analysis for 1-9 clusters
# clusters = range(1,10)
# meandist = []
#
# for k in clusters:
#     print(k)
#     model = KMeans(n_clusters=k)
#     model.fit(clus_train)
#     clusassign = model.predict(clus_train)
#     meandist.append(sum(np.min(cdist(clus_train, model.cluster_centers_, 'euclidean'), axis = 1))/clus_train.shape[0])
#
# print(meandist)
#
# # plot average distance from observations to the cluster centroid to use the Elbow Method to identify number of clusters to choose
# plt.plot(clusters, meandist)
# plt.xlabel('Number of clusters')
# plt.ylabel('Average distance')
# plt.title('Selecting k with the Elbow Method')
# plt.show()

# _________Interpret 3 cluster solution
model3 = KMeans(n_clusters=3)
model3.fit(clus_train)
clusassign = model3.predict(clus_train)

# # plot clusters
# pca_2 = PCA(2)
# plot_columns = pca_2.fit_transform(clus_train)
# plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=model3.labels_)
# plt.xlabel('Canonical variable 1')
# plt.ylabel('Canonical variable 2')
# plt.title('Canonical variables for 3 clusters')
# plt.show()

# ____________________merge cluster assignment with clustering variables to examine cluster variable means by cluster
# create a unique identifier variable from the index for the cluster training data to merge with the cluster assignment variable
clus_train.reset_index(level=0, inplace=True)
# create a list that has the new index variable
cluslist = list(clus_train['index'])
# create a list of cluster assignments
labels = list(model3.labels_)
# combine index variable list with cluster assignment list into a dictionary
newlist = dict(zip(cluslist, labels))
# convert newlist dictionary to a dataframe
newclus = pd.DataFrame.from_dict(newlist, orient='index')
# rename the cluster assignment column
newclus.columns = ['cluster']
# create a unique identifier variable from the index for the cluster assignment dataframe to merge with cluster training data
newclus.reset_index(level=0, inplace=True)
# merge the cluster assignment dataframe with the cluster training variable dataframe by the index variable
merged_train = pd.merge(clus_train, newclus, on='index')
#print(merged_train.head(n=100))
# print(merged_train.cluster.value_counts())

# calculate clustering variable means by cluster
clustergrp = merged_train.groupby('cluster').mean()
print('Clustering variable means by cluster:')
print(clustergrp)

# _________validate clusters in training data by examining cluster differences in number of layers (validation variable) using ANOVA
# merge number of layers with clustering variables and cluster assignment data
nl = new_data['NUMBER_LAYERS']
# split number of layers data into train and test sets
nl_train, nl_test = train_test_split(nl, test_size=.3, random_state=123)
nl_train1 = pd.DataFrame(nl_train)
nl_train1.reset_index(level=0, inplace=True)
merged_train_all = pd.merge(nl_train1, merged_train, on = 'index')
sub1 = merged_train_all[['NUMBER_LAYERS', 'cluster']]

nlmod = smf.ols(formula='NUMBER_LAYERS ~ C(cluster)', data=sub1).fit()
print(nlmod.summary())

print('\nMeans for number of layers by cluster:')
print(sub1.groupby('cluster').mean())
print('\nStandard deviations for number of layers by cluster:')
print(sub1.groupby('cluster').std())

# perform Post hoc test (using Tukey's Honestly Significant Difference Test)
mc1 = multi.MultiComparison(sub1['NUMBER_LAYERS'], sub1['cluster'])
res1 = mc1.tukeyhsd()
print(res1.summary())
