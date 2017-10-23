# Kaggle-Titanic-Competition

Composition of the work :

1 - EDA : Exploratory Data Analysis

-Correlation Matrix: Based in the Pearson correlation coefficient (PCC), so it is only computed over continuos variables. The PCC is a bivariate linear correlation. It is a simple check point in order to detect a linear correlation between features that could interfer in the classifier. With correlated features it is posible to drop one of the variables because it doesn't give us more knowledge.

The PCC also asumes normality in the data so in this case it is performed a Spearman rank correlation. 

Spearman Correlation has some advantages in this case:
- it doesn't make any assumption about the distribution
- while the categorical variables are ordinal with can include them in the coefficient
- it check monotonic relationships (wheter are linear or not)

2 - Data Preprocessing, based in the EDA

3 - Classifier and Results, a SVM classifier is utilized and the results and conclusions are presented

4 - Ensembling diferents classifiers

