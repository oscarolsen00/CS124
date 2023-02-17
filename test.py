# class to represent the graph dimensions

# nodes have an extra dimension
# weight using euclidian distance when dimension greater than 1 ortherwise weight is 

from random import uniform as rnd
import numpy as np
import math as mt

def euc_dist(a,b):
    val = mt.dist(a,b)
    return val

node = 1

def vertices_gen(n, dim):
    vertices = dict()
    if dim == 2:
        for i in range(n):
            vertices.update({ i : (rnd(0,1))})
    if dim == 2:
        for i in range(n):
            vertices.update({ i : (rnd(0,1),rnd(0,1))})
    if dim == 3:
        for i in range(n):
            vertices.update({ i : (rnd(0,1),rnd(0,1), rnd(0,1))})
    if dim == 4:
        for i in range(n):
            vertices.update({ i : (rnd(0,1),rnd(0,1), rnd(0,1), rnd(0,1))})
    return vertices


def matrix(n, vertices):
    graph = []
    if dim == 1:
        for i in range(0,n):
            graph.append(list(np.zeros(n)))
            for j in range(n):
                if j > i:
                    graph[i][j] = rnd(0,1)
                else: 
                    graph[i][j] = graph[j][i]
    else:
        for i in range(0,n ):
            graph.append(list(np.zeros(n)))
            for j in range(n):
                if j > i:
                    graph[i][j] = euc_dist()
                else: 
                    graph[i][j] = graph[j][i]

    return graph
            
                #  gerneate new edge copy over otherewise
print(matrix(3))

#  matrix - becusea complete so everyone conected
# randomly generate coordinates 
# weights = euclidian distance of these nodes
# list of node index to coordinates

# an MST function