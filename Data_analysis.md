Project for the Data Analysis Tools course on Coursera

### Hypothesis Testing and ANOVA

There are the [code](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/data_analysis.py) and its [output](https://github.com/ekolik/-Python-Distribution_of_craters_on_Mars/blob/master/data_analysis/data_analysis_output1week.txt) that are created at this point. 

When examining the correlation between the diameters of craters and their location (in one of 4 quadrants), an Analysis of Variance (ANOVA) revealed that these variables are significantly associated, `F(3, 384339) = 251.1, p = 8.27e-163`. Post hoc comparisons of mean diameters of craters by pairs of Mars' quadrants, in which the craters are located, revealed that all 4 quadrants contain craters with significantly different diameters. In particular, craters in the south-eastern quadrant have significantly larger diameters than craters in all other quadrants. Conversely, craters in the north-western quadrant have significantly smaller diameters than craters in all other quadrants. Or, in general, craters in the southern hemisphere have significantly larger diameters than craters in the northern.
