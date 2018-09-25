#!/usr/bin/python
# -*- coding:utf-8 -*-

from pyspark import SparkContext, SparkConf
from operator import add
conf = SparkConf()\
.setAppName("wordcount_demo")
sc = SparkContext(conf=conf)
lines = sc.textFile("/data/data.log")
words = lines.flatMap(lambda line: line.split(','))
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(add)
output = wordCounts.collect()
for (word, count) in output:
    print ("%s: %i\n" % (word, count))
sc.stop()