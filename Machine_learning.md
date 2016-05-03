Project for Machine Learning for Data Analysis on Coursera

### Decision Trees

This is the classification tree (`N = 100`) for the number of layers in a crater (categorical target variable: more than/equal to 2 or less than 2)

![alt tag](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/dt.png)

Decision tree analysis was performed to test nonlinear relationships among a series of explanatory variables and a binary, categorical response variable. All possible cut points (for quantitative variables) are tested. For the present analysis, the entropy “goodness of split” criterion was used to grow the tree and a cost complexity algorithm was used for pruning the full tree into a final subtree.

The following explanatory variables were included as possible contributors to a classification tree model evaluating the number of layers in a crater (my response variable): the diameter, latitude, and longitude of a crater. 60% of the sample were used for the training, and 40% - for testing. The accuracy of the resulted tree is `0.78`. The confusion matrix is:
 
 `[30  5]`

 `[ 4  2]`

The longitude was the first variable to separate the sample into two subgroups, followed by the latitude and the diameter. However, it is important to notice that these variable were used recurrently later in the sub-branches of the tree. It might indicate that the selected variables are not suitable for proper tree formation, or that the tree analysis is not suitable for these data, or that this particular target variable is not suitable for prediction. Anyway, this work was useful in educational purposes.
 
This is the main code of the program (in Python):
![alt tag](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/Screenshot_of_code.png)

### Random Forests

Random forest analysis was performed to evaluate the importance of the crater's diameter and depth (quantitative explanatory variables) in predicting the number of layers in a crater (binary target variable: more than/equal to 2 layers or less than 2 layers). 60% of the sample were used for the training, and 40% - for testing. Initially, the random forest model was created with `25` trees. Here are the results of the training:

![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/output_week2.png)

We can see that the diameter of a crater has very high relative importance score, and, therefore, more important in predicting the number of layers than the depth of the crater. I find this result surprising.

Then, we trained the random forest with different numbers of trees (1-10) to see the effect of the number on the accuracy of the prediction. The following plot indicates that the subsequent growing of number of trees adds little to the overall accuracy of the forest; moreover, the forest with just 2 trees has the highest accuracy: `0.9855`.
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/n_trees_vs_accuracy.png)

There is the [code](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/machine_learning.py) of the program (in Python).

### Lasso Regression

A lasso regression analysis was conducted to identify a subset of predictor variables that are best in predicting a quantitative response variable measuring the number of layers in a crater. The predictor variables (crater's longitude, latitude, depth, and diameter) are quantitative and standardized to have a mean of zero and a standard deviation of one.

Data were randomly split into a training set (70% of the observations) and a test set (30%). The least angle regression algorithm with k=10 fold cross validation was used to estimate the lasso regression model in the training set, and the model was validated using the test set. The change in the cross validation mean squared error at each step was used to identify the best subset of predictor variables.

![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/Lasso_mse.png)
![](https://raw.githubusercontent.com/ekolik/-Python-Distribution_of_craters_on_Mars/master/machine_learning/Lasso_coefs.png)

All 4 predictor variables were retained in the selected model. The results of the training indicate the crater's depth as the predictor variable most strongly and positively associated with the number of layers. Other variables have very small coefficients and, therefore, might be considered not very influential. Mean squared error and R-squared values prove the model being robust for testing on new examples. The predictors account for 21% of the variance in the target variable.

![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/output_week3.png)

There is the [code](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/machine_learning.py) of the program (in Python).

### K-Means Cluster Analysis

A K-means cluster analysis was conducted to identify underlying subgroups of craters based on their characteristics (quantitative clustering variables): latitude, longitude, diameter, and depth. All the variables were standardized to have a mean of 0 and a standard deviation of 1.

Data were randomly split into a training set (70%) and a test set (30% of the observations). A series of k-means cluster analyses were conducted on the training set specifying k=1-9 clusters, using Euclidean distance. The average distance from observations to the cluster centroids was plotted for each of the nine cluster solutions in an elbow curve to provide guidance for choosing the number of clusters to interpret.
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/K-means_elbow.png)

The elbow curve was inconclusive, suggesting that the 4, 6, and 8-cluster solutions might be interpreted. However, before choosing the solution, canonical discriminant analyses were performed for each solution.

Canonical discriminant analysis reduces the 4 clustering variables down to 2 canonical variables that account for most of the variance in the clustering variables. After plotting the canonical variables for each 1-9 cluster solution, the 3-cluster solution was chosen as the one that splits the data in the best way. The plot for 3-cluster solution indicates that the observations in the *green* and *blue* clusters are densely packed with relatively low within cluster variances and don't overlap with the other clusters. The observations in the *red* cluster have greater spread suggesting higher within cluster variance.
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/K-means_3clus.png)

The means of the clustering variables show that, the cluster 1, as the most distinctive, contains crates located mostly in near zero coordinates and have big diameter and big depth. Cluster 2 containes craters located mostly in the north-eastern quadrant of Mars and have diameter and depth close to 0. Cluster 3 contains craters located mostly in the south-western quadrant of Mars and have diameter and depth close to 0, too. 

In order to externally validate the clusters, an Analysis of Variance (ANOVA) was conducted to test for significant differences between the clusters on the number of layers in a crater. Results indicated significant differences between the clusters on the number of layers (`F(2, 269037) = 1.886e+04, p = 0`). The Tukey post hoc comparisons also showed significant differences between all clusters on the number of layers. Craters in cluster 1 have the largest number of layers (`mean = 0.498607, std = 0.788978`), which implies that combination of near zero coordinates, big diameter, and big depth is associated with large number of layers in a crater.

There is the [code](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/machine_learning.py) of the program (in Python) and its [output](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/output_week4.txt).
