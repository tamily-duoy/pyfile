# -*- coding: utf-8 -*-

import math
import collections
import random
import copy
import pylab

try:
    import psyco
    psyco.full()
except ImportError:
    pass

FLOAT_MAX = 1e100

class Point:
    __slots__ = ["x", "y", "group", "uij"]
    def __init__(self, cent_clust, x = 0, y = 0, group = 0):
        self.x, self.y, self.group = x, y, group
        self.uij = [0.0 for _ in range(cent_clust)]

def Points(point_num, r, cent_clust):
    points = [Point(cent_clust) for _ in range(2 * point_num)]
    count = 0
    for point in points:
        count += 1
        R = random.random() * r
        angle = random.random() * 2 * math.pi
        point.x = R * math.cos(angle)
        point.y = R * math.sin(angle)
        if count == point_num - 1:
            break
    for index in range(point_num, 2 * point_num):
        points[index].x = 2 * r * random.random() - r
        points[index].y = 2 * r * random.random() - r
    return points



def Distance(pointA, pointB):
    return (pointA.x - pointB.x) **2 + (pointA.y - pointB.y) **2

def getNearestCenter(point, cent_clust):
    minIndex = point.group
    min_Distance = FLOAT_MAX
    for index, center in enumerate(cent_clust):
        distance = Distance(point, center)
        if (distance < min_Distance):
            min_Distance = distance
            minIndex = index
    return (minIndex, min_Distance)

def kmean(points, cent_clust):
    cent_clust[0] = copy.copy(random.choice(points))
    distanceGroup = [0.0 for _ in range(len(points))]
    sum = 0.0
    for index in range(1, len(cent_clust)):
        for i, point in enumerate(points):
            distanceGroup[i] = getNearestCenter(point, cent_clust[:index])[1]
            sum += distanceGroup[i]
        sum *= random.random()
        for i, distance in enumerate(distanceGroup):
            sum -= distance
            if sum < 0:
                cent_clust[index] = copy.copy(points[i])
                break
    return

def fuzzy_kmean(points, cent_num, weight):
    cent_clust = [Point(cent_num) for _ in range(cent_num)]
    kmean(points, cent_clust)
    cent_trace = [[Cent] for Cent in cent_clust]
    tolerableError, curError = 1.0, FLOAT_MAX
    while curError >= tolerableError:
        for point in points:
            getSingleuij(point, cent_clust, weight)
        cent_clust = [Point(cent_num) for _ in range(cent_num)]
        for centerIndex, center in enumerate(cent_clust):
            upperSumX, upperSumY, lowerSum = 0.0, 0.0, 0.0
            for point in points:
                uijWeight = pow(point.uij[centerIndex], weight)
                upperSumX += point.x * uijWeight
                upperSumY += point.y * uijWeight
                lowerSum += uijWeight
            center.x = upperSumX / lowerSum
            center.y = upperSumY / lowerSum
        # update cluster center trace
        curError = 0.0
        for index, trace_i in enumerate(cent_trace):
            trace_i.append(cent_clust[index])
            curError += Distance(trace_i[-1], trace_i[-2])
            cent_clust[index] = copy.copy(cent_clust[index])
    for point in points:
        max_Index, max_uij = 0, 0.0
        for index, singleuij in enumerate(point.uij):
            if singleuij > max_uij:
                max_uij = singleuij
                max_Index = index
        point.group = max_Index
    return cent_clust, cent_trace

def getSingleuij(point, cent_clust, weight):
    Distance2 = [Distance(point, cent_clust[index]) for index in range(len(cent_clust))]
    for centerIndex, singleuij in enumerate(point.uij):
        sum = 0.0
        isCoincide = [False, 0]
        for index, distance in enumerate(Distance2):
            if distance == 0:
                isCoincide[0] = True
                isCoincide[1] = index
                break
            sum += pow(float(Distance2[centerIndex] / distance), 1.0 / (weight - 1.0))
        if isCoincide[0]:
            if isCoincide[1] == centerIndex:
                point.uij[centerIndex] = 1.0
            else:
                point.uij[centerIndex] = 0.0
        else:
            point.uij[centerIndex] = 1.0 / sum

def show(points, cent_trace):
    colorStore = ['or', 'og', 'ob', 'oc', 'om', 'oy', 'ok']
    pylab.figure(figsize=(9, 9), dpi = 80)
    for point in points:
        color = ''
        if point.group >= len(colorStore):
            color = colorStore[-1]
        else:
            color = colorStore[point.group]
        pylab.plot(point.x, point.y, color)
    for trace_i in cent_trace:
        pylab.plot([center.x for center in trace_i], [center.y for center in trace_i], 'k')
    pylab.show()

def main():
    cent_clust = 5
    point_num = 2000
    r = 10
    weight = 2
    points = Points(point_num, r, cent_clust)
    _, cent_trace = fuzzy_kmean(points, cent_clust, weight)
    show(points, cent_trace)

main()