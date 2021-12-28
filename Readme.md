# 基于多视图和图间随机游走核(Inter-graph Random Walk Kernel, IRWK)的Twitter网络社群相似度寻找方法
这是社会网络分析课程的期末作业项目。
## 介绍
本项目使用IRWK基于每个视图提供的信息以及视图之间的关系对网络进行建模，然后使用IRWK学习一个判别分类器来标记参与者。一个视图中只存在单一种类的连接关系，复杂网络如Twitter往往是由多种视图构成的，每一个参与者在不同的视图中存在不同的关系。本工作中需要寻找节点之间的相似性，如果一个图中的两个节点产生的随机游动集相似，则认为这两个节点是相似的，因此构建了随机游走核。IRWK为每个视图生成一个内核，它不仅结合了每个视图内的随机游走信息，也结合了从每个视图和其他视图遍历的随机游走信息，从而充分利用了复杂网络中的多视角信息。
## 文件描述

reply.txt\retweet.txt\mention.txt: 提供了三种tweeter网络的视角————回复、转发、艾特的视图，文件中提供了各个节点之间存在的边的关系，每一行记录了第一个点到第二个点的关系，分别32523、328132、150818个链接。

social1.txt\social2.txt: 提供了样本中各个节点相互关注的视角，文件中提供了各个节点之间存在的边的关系，每一行表示第一个节点关注第二个节点。

RW.py: 构建了IRWK方法。

main.py: 运行的主文件，在此文件中通过networkx构建了reply、retweet、mention、social四个图，使用IRWK来计算平均相似度。

## 使用的库
networkx: 使用Python语言构建复杂网络

community: 探测复杂网络中的社群

numpy

random

timeit
## 参考
本项目使用的基于多视图和图间随机游走核的方法参考自文章：

[1]N. Bui, T. Le and V. Honavar, "Labeling actors in multi-view social networks by integrating information from within and across multiple views," 2016 IEEE International Conference on Big Data (Big Data), 2016, pp. 616-625, doi: 10.1109/BigData.2016.7840654.

