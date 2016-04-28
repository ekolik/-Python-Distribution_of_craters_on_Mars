Project for the Regression Modeling in Practice course on Coursera

### Introduction to Regression
*Sample*

The data is taken from the Mars Craters Study ([Mars Crater codebook (.pdf)](https://d396qusza40orc.cloudfront.net/phoenixassets/data-management-visualization/Mars%20Crater%20Codebook.pdf), [Mars Crater data file (.csv)](https://d396qusza40orc.cloudfront.net/phoenixassets/data-management-visualization/marscrater_pds.csv)), which is created by Stuart Robbins and presents a new global database for Mars that contains 378,540 craters statistically complete for diameters ≥ 1km. This dataset provides the following information about the craters: the latitude and longitude of a crater, its depth and diameter, number of layers in a crater, the presence of ejecta and morphology if its layers. 

*Procedure*

The data was collected by a multi-stage process of identification and analysis conducted by Stuart Robbins in 2009. According to his [paper](http://about.sjrdesign.net/research_mars.html#crater_database_mars), his work involved examining the global daytime thermal infrared [mosaic of Mars](http://www.mars.asu.edu/data/thm_dir/), which was collected during [THEMIS mission](http://www.nasa.gov/mission_pages/themis/mission/index.html), and marking every resolved crater in this mosaic. *The researcher allowed ~500m spacing between point resolution and looked for ≥ 5 points along a crater rim which limits the diameter to ~700-800 meters. He estimates the statistical completeness to be at ~1.0 km.* *

\* *It looks confusing, but it's the most comprehensible explanation I was able to find. :)*

*Measures*

Here are the measures of the data collected:
* Latitude and longitude of a crater are in decimal degrees North and East respectively. These coordinates represent the derived center of a non-linear least squares circle that was fit to the vertices identifying the crater rim. In other words, the coordinates indicate the estimated center of a crater.
* Diameter of a crater is in km. It is equal to the diameter of a non-linear least squares circle fit to the vertices identifying the crater rim.
* Depth of a crater is in km. It is equal to the average elevation of each of the manually determined 5 points along (or inside) the crater rim.
* Number of layers is in the 0-to-5 range. It is equal to the maximum number of cohesive layers in any reliably identified azimuthal direction.
* Crater ejecta is described by categorical codes. The codes indicate if the ejecta is hummocky with short lobes, smooth with short lobes, hummocky with splash, or smooth with splash. The ejecta shape might be: pin-cushion, pedestal, sandbar, bumblebee, butterfly, pseudo-butterfly, or rectangular.

As one part of my work, I evaluate the distribution of craters by calculating and comparing the square acreages of craters separately on each of the 4 quadrants of Mars: north-western, north-eastern, south-western, and south-eastern. To find the square acreage of craters on one quadrant, I first calculate and then sum up the square acreages of all craters with centers within this quadrant.

### Basics of Linear Regression

As the first step in testing the association between the crater's depth (quantitative explanatory variable) and its number of layers (quantitative response variable), the scatter-plot was created:
![alt tag](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/depth-vs-numberlayers.png)

The plot reveals positive association between the variables: the deeper a crater, the more layers it has.

Before testing a linear regression model, the explanatory variable (depth of a crater) was centered by subtracting its mean (equal to `~ 0.076`) from each observed value of depth. The mean of the variable after centering is equal to `~ -2.557e-14`, which is very close to `0`. This is the output of the linear regression model that was created:

![alt tag](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/output_week2.png)

The output tells us that the model was constructed using `384343` observations, the R-squared number is `0.191` (in other words, 19% of the variability in the number of layers in a crater is described by variation in the crater's depth), F = `9.089e+04` with p = `0.00` (which mean that the variables are significantly associated). The regression coefficients of the model are: intercept = `0.0648` and slope = `0.6019`, which means that we can relate our variables by the formula: <br /> `number of layers = 0.0648 + 0.6019*depth`.

There is the [code](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/regression_modeling.py) of the program (in Python).

### Multiple Regression

There is the [code](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/regression_modeling.py) of the program (in Python) and its [output](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/output_week3.txt).

We have already addressed the association between the crater's diameter (quantitative explanatory variable) and its depth (quantitative response variable) in the Data Analysis section while studying [Pearson Correlation] (https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/Data_analysis.md#pearson-correlation). There we have noticed that the relationship between the variables is positive, but not linear. Therefore, now we address this question using polynomial (second order) regression. Firstly, we run the second order fit line for the data:
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/polynom.png)

This line is again not very accurate in describing the data, but let's see the results of the polynomial regression analysis in comparison to the linear regression analysis. (Before performing the analysis we center both of the variables by subtracting their means.) There are the [results](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/output_week3.txt) of the analysis. The results of the linear regression indicate a significant, positive association between the variables with `34.4%` of the variability in the crater's depth described by variation in its diameter. The results of the polynomial regression indicate a significant, positive, concave-shaped association between the variables with `42.6%` of the variability in the crater's depth described by variation in its diameter. In other words, the concave pattern observed in scatter plot is statistically significant, and there is an increase in the R-squared value.

We continue examining the relationship between the variables by adding another explanatory variable: number of layers in a crater. After running [multivariate regression](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/output_week3.txt), we observe that the diameter (initial explanatory variable, coefficient = `0.0182`) remains significantly (p-value = `0`) associated with the depth (response variable, intercept = `0.0774`) after controlling for the number of layers (second explanatory variable, coefficient = `0.2486`), and the number of layers is positively significantly (p-value = `0`) associated with the depth after controlling for the diameter. In other words, the number of layers is not confounder in this relationship. Moreover, this multivariate regression brings us additional increase in R-squared value: now `54%` of the variability in the crater's depth is described by variation in its diameter and the number of layers.

Before making any conclusions, we examine the diagnostic plots:
* The Q-Q plot shows that the residuals follow the fit line only in the middle, but highly deviate at the lower and higher quantiles. This indicated that the residuals do not follow normal distribution, and the association that we built is not proper. There must be other explanatory variables that should be considered in the model for its improvement.
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/qq.png)

* The plot of residuals again shows that that the model is a poor fit to the data because much more than 5% of the observations have standardized residuals with an absolute value bigger than 2. It means that the important explanatory variables were not used for the model fit.
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/resid_plot.png)

* Other diagnostic plots also show that the residuals are small neither for the number of layers nor for the diameter variables. The model predicts poorly for most of the cases, but it is especially bad for the observations with small number of layers and for the observations with big diameters. The partial regression plots show that the residuals follow a linear patter neither for the number of layers nor for the diameter. This means the weak association with the response variable of one explanatory variable after controlling for the other.
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/num_layers_diagnos.png)
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/diam_diagnos.png)

* The leverage plot (used only a subset of the data for plotting) shows that a big number of the observations are outliers (they have residuals greater than 2 or less than -2.), and even though they have small leverage values, they do have an undue influence on the estimation of the regression model. There are also quite a few cases with higher than average leverage; in particular, there is one observation (marked `1`) that is both an outlier and have a high leverage, and it is very dramatic in its undue influence on the estimation. 
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/regression_modeling/leverage.png)

Therefore, there is a very important lesson learned here: do not rely solely on the results of the regression models, but examine very carefully the diagnostic plots. These plots provide very essential information about the quality of the model and thus may undermine the correctness of the model. In our case, we conclude that the model we've built here is not a proper model for the data. 

The exploration of this topic is continued in the [Machine Learning](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/Machine_learning.md) section.
