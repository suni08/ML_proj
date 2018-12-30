# Probability distributions using python
Prime Objective: To implement Probability distributions using python.
Obtained output of the program:
UBitName = Bhumika Khatwani Sunita Pattanayak
personNumber = 50247656 50249134
mu1 = 3.214
var1 = 0.448
sigma1 = 0.669
mu2 = 53.386
var2 = 12.588
sigma2 = 3.548
mu3 = 469178.816
var3 = 13900134681.701
sigma3 = 117898.832
mu4 = 29711.959
var4 = 30727538.733
sigma4 = 5543.243
COVARIANCE MATRIX:
[[0.457 1.106 3879.782 1058.480]
[1.106 12.850 70279.376 2805.789]
[3879.782 70279.376 14189720820.903 -163685641.258]
[1058.480 2805.789 -163685641.258 31367695.790]]
CORRELATION COEFFICIENT MATRIX:
[[1.000 0.456 0.048 0.279]
[0.456 1.000 0.165 0.140]
[0.048 0.165 1.000 -0.245]
[0.279 0.140 -0.245 1.000]]
Column Admin Base Pay and column Tuition are least correlated
Column Research Overhead and column CS Score are most correlated
Loglikelihood (normal pdf): -1315.099
Loglikelihood (formula implementation): -1304.729
Conclusion:
1. We have computed the values of mean, variance and standard
deviation for each column namely, CS Score, Research Overhead,
Admin Base Pay, Tuition

The dataset has 49 row inputs. In the project, we have considered
the data sets as random variables having a probability
distribution.
mu1, mu2, mu3 and mu4 represent the mean for each column.
Finding mean of the datasets, allows us to have a rough idea on
the expected value for each column.
sigma1, sigma2, sigma3 and sigma4 represent standard deviation
for each column. Standard deviation gives us an insight on the
extent to which the random variables are dispersed for a set of
data values.
var1, var2, var3 and var4 represent the variance for each column.
Variance is nothing but the expected squared deviation of a
random variable from its mean.
2. We have computed the Covariance matrix which is a 4X4 matrix.
Covariance is a measure of the extent to which corresponding
elements from two sets of ordered data move in the same
direction. Through the matrix, we can actually calculate how 2
variables change with respect to each other.
We have next, computed correlation coefficient matrix which is
also a 4X4 matrix. Correlation coefficient measures the strength
and direction of a linear relationship between two variables.
Through the matrix, we investigate the dependency between
multiple variables at the same time.
We have plotted the correlation matrix graph:
3. Probability distribution function: As we know PDF is the
probability of the random variable falling within a particular range
of values. Here, we plot a graph between the data set and the
normal pdf to check the same.
Then, we calculate the log likelihood which gives us an idea about
the probability of value of the random variables equaling that
sample. Main difference between the probability and likelihood is
that probability is used before availability of data to describe
possible future outcomes given a fixed value for the parameter
and likelihood is used after data id available to describe a function
of a parameter for a given outcome.
For the 4 columns, we have plotted the normal pdf graphs as
follows:

For multivariate pdf, we have implemented the formula given in
the project description. It gives us the likelihood of random
variables (from the given data set) by considering more than one
variable.
Thus, we can see how various probability distribution in statistics
helps us determine various behavior and likelihood of data sets.
We can even use histograms, scatter plots and many other single
as well as multi dimensional graphs to analyze data and their
behaviors.
