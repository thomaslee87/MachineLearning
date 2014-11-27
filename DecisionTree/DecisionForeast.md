

参考文档：[Decision Foreast](http://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm#workings)

----

#### 1.名词解释

variable importance、oob error estimate、Gini importance、Proximities。中文对应的分别为：变量重要性、OOB误差估计、基尼重要性、相似性矩阵。

+ oob error estimate

每棵决策树构造时，都使用原始样本的bootstrap抽样作为训练集，原始数据中约1/3在构造单棵树时没有被用到，这部分数据被称为oob（out-of-bag袋外数据)

构造好每棵数时，对袋外数据每个样本预测得到一个分类，这样对每个样本，都会在约1/3的树中作为测试集。

构建完成后，对每个样本都用投票机制决定被分到哪个类，被分错的样本的比例就是oob error estimate 

*在很多测试中被证明是无偏的* 期望等于真实值

+ variable importance

构建随机森林中的每棵数时，记下oob中每个样本被分类正确的个数 n1

随机改变oob中所有样本某个特征m的取值，然后再进行预测得到被正确分类的个数 n2

n2 - n1，然后对森林中所有的数做平均，就得到了这个特征m的**原始重要性 raw importance**

对单个样本来说，考虑所有它在oob中的树，未改变特征m时被分类正确的比例 减去 改变了特征m后被分类正确的比例，得到的是这个样本的**local importance score for variable m**


+ Gini importance

每次对节点关于特征m做分裂时，两个派生节点的基尼不纯度（gini impurity)小于父节点，对森林中单个特征计算的所有gini decrease做加和，得到一个快速的变量重要性

+ Proximities

Proximities是随机森林中最重要的工具之一，N * N 矩阵的形式。一棵树构造好之后，将所有的样本（training + oob） put down the tree。如果样本k和样本n走到同一个terminal node，则矩阵相应位置 +1，最后矩阵除以数的个数来做归一化。


----

#### 2.针对bootstrap抽样给出你的理解，可以从原理和基本步骤角度来展开

Bootstrap又称自展法，是用小样本估计总体值的一种非参数方法

已经证明，在初始样本足够大的情况下，bootstrap抽样能够无偏得接近总体的分布。

通过从原始数据（大小n）做n次有放回随机抽样，得到n个数据，抽取的样本数目与原始样本数目一样 

一个bootstrap样本集中包含了大约原始样本集的1-0.368=0.632，另外0.368的样本没有包括

----

#### 3.	请查阅资料给大家讲明白“蓄水池抽样”的背景、问题、实现原理

[蓄水池抽样](http://blog.csdn.net/huagong_adu/article/details/7619665)

选择N中的前k个数加入“蓄水池”中，然后从第k+1个数开始，以k/k+i(i=1,2,3...)的概率选择这个数，然后在蓄水池中随机选择一个数，并将其替换，N个元素遍历完毕后，蓄水池中的k个数就是随机选择的。

----

#### 4. 讲一下随机森林实现的原理



----

#### Features of Random Forests

It is unexcelled in accuracy among current algorithms.

It runs efficiently on large data bases.

It can handle thousands of input variables without variable deletion.

It gives estimates of what variables are important in the classification.

It generates an internal unbiased estimate of the generalization error as the forest building progresses.

It has an effective method for estimating missing data and maintains accuracy when a large proportion of the data are missing.

It has methods for balancing error in class population unbalanced data sets.

Generated forests can be saved for future use on other data.

Prototypes are computed that give information about the relation between the variables and the classification.

It computes proximities between pairs of cases that can be used in clustering, locating outliers, or (by scaling) give interesting views of the data.

The capabilities of the above can be extended to unlabeled data, leading to unsupervised clustering, data views and outlier detection.

It offers an experimental method for detecting variable interactions.








