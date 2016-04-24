Project for Machine Learning for Data Analysis on Coursera

### Decision Trees

This is the classification tree (`N = 100`) for the number of layers in a crater (categorical target variable: more than/equal to 2 or less than 2)

![alt tag](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/dt.png)

Decision tree analysis was performed to test nonlinear relationships among a series of explanatory variables and a binary, categorical response variable. All possible cut points (for quantitative variables) are tested. For the present analyses, the entropy “goodness of split” criterion was used to grow the tree and a cost complexity algorithm was used for pruning the full tree into a final subtree.

The following explanatory variables were included as possible contributors to a classification tree model evaluating the number of layers in a crater (my response variable): the diameter, latitude, and longitude of a crater. 60% of the sample were used for the training, and 40% - for testing. The accuracy of the resulted tree is `0.78`. The confusion matrix is:
 
 `[30  5]`

 `[ 4  2]`

The longitude was the first variable to separate the sample into two subgroups, followed by the latitude and the diameter. However, it is important to notice that these variable were used recurrently later in the sub-branches of the tree. It might indicate that the selected variables are not suitable for proper tree formation, or that the tree analysis is not suitable for these data, or that this particular target variable is not suitable for prediction. Anyway, this work was useful in educational purposes.
 
This is the main code of the program (in Python):
![alt tag](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/machine_learning/Screenshot_of_code.png)