Project for the Data Analysis Tools course on Coursera

### Hypothesis Testing and ANOVA

There are the [code](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/data_analysis.py) and its [output](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/data_analysis_output1week.txt) that are created at this point. 

When examining the correlation between the diameters of craters and their location (in one of 4 quadrants), an Analysis of Variance (ANOVA) revealed that these variables are significantly associated, `F(3, 384339) = 251.1, p = 8.27e-163`. Post hoc comparisons of mean diameters of craters by pairs of Mars' quadrants, in which the craters are located, revealed that all 4 quadrants contain craters with significantly different diameters. In particular, craters in the south-eastern quadrant have significantly larger diameters than craters in all other quadrants. Conversely, craters in the north-western quadrant have significantly smaller diameters than craters in all other quadrants. Or, in general, craters in the southern hemisphere have significantly larger diameters than craters in the northern.

### Chi-Square Test of Independence

There are the [code](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/data_analysis.py) and its [output](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/data_analysis_output2week.txt) that are created at this point. 

When examining the association between the number of layers in a crater (categorical response: more than/equal to 2 or less than 2) and the crater's location (categorical explanatory variable: one of 4 quadrants of Mars), a chi-square test of independence revealed that these variables are significantly associated: `χ2 = 704.47, p = 2.25e-152, df = 3`. Post hoc comparisons of the number of layers in craters by pairs of quadrants, in which the craters are located, revealed that the north-western quadrant contains the highest percent of crates with number of layers 2 or more, followed by the north-eastern quadrant. Both of these quadrants are statistically different from all other quadrants and from each other in the considered terms. The south-eastern and south-western quadrants contain fewer craters with number of layers 2 or more and are statistically similar in these terms. To visualize the results, the graph that shows the percent of craters with 2 or more layers per each quadrant of Mars was created and can be viewed [here](https://raw.githubusercontent.com/ekolik/-Python-Distribution_of_craters_on_Mars/master/data_analysis/twopluslayers.png).

### Pearson Correlation

When examining the association between the crater's diameter (quantitative explanatory variable) and its depth (quantitative response variable), a Pearson correlation coefficient was calculated: `r = 0.59, p-value = 0.0`. In other words, the coefficient shows that there is a positive linear relationship between these variables. In addition, it can be assumed that 34% of the variability in the crater's depth is described by variation in the crater's diameter (using `RSquared or Coefficient of Determination: 0.59² = 0.34`).

However, the scatter-plot of these variables shows that this relationship is hardly linear:
![alt tag](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/diam_vs_depth.png)

That is why it is important to look at both a scatterplot and a correlation coefficient before making a final conclusion. In this case, the relationship between the variables is somewhat positive, but not linear.

There is the main code of the program (in Python):
![alt tag](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/code_screenshot_week3.png)

### Exploring Statistical Interactions

Here, we check if the association between the crater's diameter (quantitative explanatory variable) and its depth (quantitative response variable) is linear for craters with the same number of layers. In other words, we divide the data into 6 groups by number of layers in craters: 0, 1, 2, 3, 4, and 5 layers, and then calculate a Pearson correlation coefficient (diameter vs depth) for each group.

There is the main code of the program (in Python):
![alt tag](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/code_screenshot_week4.png)

There is the output of the program:

![alt tag](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/code_output_week4.png)

The results of the calculations mean that there is a positive linear relationship between the variables for each group. This might indicate that the number of layers doesn't influence the relationship between the diameter and depth of a crater. However, the look at the scatter-plots for each of the groups (shown below) reveals the following:
* there is no distinctive linear relationship between the diameter and depth for craters with no layers; 
* the relationship progressively becomes more distinctive (positive and linear) for craters with 1, 2, and 3 layers;
* the relationship is strongly positive and linear for craters with 4 layers;
* there is not enough samples with 5 layers to make conclusions about the relationship.

![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/diam_vs_depth-0layers.png)
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/diam_vs_depth-1layer.png)
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/diam_vs_depth-2layers.png)
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/diam_vs_depth-3layers.png)
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/diam_vs_depth-4layers.png)
![](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/diam_vs_depth-5layers.png)

Therefore, the number of layers **does** influence the relationship between the diameter and depth of a crater: the more layers are in a crater, the more pronounced the linear relationship is.

