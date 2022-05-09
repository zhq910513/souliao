#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 最好采用anaconda   资料参考如下
'https://baijiahao.baidu.com/s?id=1725016623454388410&wfr=spider&for=pc'
'https://blog.csdn.net/StephenFengz/article/details/52997387?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-2-52997387-blog-96299139.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-2-52997387-blog-96299139.pc_relevant_default&utm_relevant_index=5'
'https://blog.csdn.net/duohuanxi/article/details/107740930'

#  我的环境
# anaconda
# python3.8
# pydot==1.4.1
# sklearn==0.0
# six==1.16.0


from sklearn.datasets import load_iris
from sklearn import tree
from six import StringIO
import pydot


iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
print(graph)
