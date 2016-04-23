import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import sklearn


new_data = pd.read_csv('marscrater_pds.csv', low_memory=False)


# recode layer numbers into 2 groups: {0,1}, {2,3,4,5}. this would be the response variable
recode = {0: 0, 1: 0, 2:1, 3:1, 4:1, 5:1}
new_data['NUMBER_LAYERS'] = new_data['NUMBER_LAYERS'].map(recode)

# round up the explanatory variables and subset the data
new_data["DIAM_INT"] = new_data["DIAM_CIRCLE_IMAGE"].round()
new_data["LATITUDE_CIRCLE_IMAGE"] = new_data["LATITUDE_CIRCLE_IMAGE"].round()
new_data["LONGITUDE_CIRCLE_IMAGE"] = new_data["LONGITUDE_CIRCLE_IMAGE"].round()
new_data = new_data.ix[:100]

# split into training and testing sets
predictors = new_data[["DIAM_INT", 'LATITUDE_CIRCLE_IMAGE', "LONGITUDE_CIRCLE_IMAGE"]]
targets = new_data.NUMBER_LAYERS

pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.4)
pred_train.shape
pred_test.shape
tar_train.shape
tar_test.shape

# build model on training data
classifier = DecisionTreeClassifier()
classifier = classifier.fit(pred_train, tar_train)

predictions = classifier.predict(pred_test)

# print the confusion matrix and accuracy of the model
print(sklearn.metrics.confusion_matrix(tar_test, predictions))
print(sklearn.metrics.accuracy_score(tar_test, predictions))

# export the tree for viewing
export_graphviz(classifier, out_file="decision_tree.dot")

# to view the decision tree create a .pdf file from the created .dot file
# by typing in the terminal from this directory: dot -Tpdf decision_tree -o decision_tree.pdf




