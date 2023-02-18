# class to represent the graph dimensions
# nodes have an extra dimension
# weight using euclidian distance when dimension greater than 1 ortherwise weight is 

from random import uniform as rnd
import numpy as np
import math as mt

def euc_dist(a,b):
    val = mt.dist(a,b)
    return val

def vertices_gen(n : int, dim : int) -> dict:
    vertices = dict()
    if dim == 2:
        for i in range(n):
            vertices.update({ i : [rnd(0,1)]})
    if dim == 2:
        for i in range(n):
            vertices.update({ i : [rnd(0,1),rnd(0,1)]})
    if dim == 3:
        for i in range(n):
            vertices.update({ i : [rnd(0,1),rnd(0,1), rnd(0,1)]})
    if dim == 4:
        for i in range(n):
            vertices.update({ i : [rnd(0,1),rnd(0,1), rnd(0,1), rnd(0,1)]})
    return vertices

def matrix(n : int, vertices : dict, dim : int) -> list:
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
                    graph[i][j] = euc_dist(vertices.get(i), vertices.get(j))
                else: 
                    graph[i][j] = graph[j][i]

    return graph
            
                #  gerneate new edge copy over otherewise

test_vert = vertices_gen(3, 2)
print(matrix(3, test_vert, 2))


# class for a heap

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return i / 2

    def left_child(self, i):
        return 2 * i

    def right_child(self, i):
        return 2 * i + 1

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, k):
        self.heap.append(k)
        # len(self.heap) - 1
        i = self.heap[-1]
        while i != 0 and self.heap[self.parent(i)][0] > self.heap[i][0]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        smallest = i
        if l < len(self.heap) and self.heap[l][0] < self.heap[i][0]:
            smallest = l
        if r < len(self.heap) and self.heap[r][0] < self.heap[smallest][0]:
            smallest = r
        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def extract_min(self):
        min_tup = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0) 
        return min_tup

def prim_mst_heap_adjacency(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    heap = [(0, 0)] # (dist, vertex)
    mst_cost = 0
    mst = []

    while heap:
        weight, u = MinHeap.extract_min()
        if visited[u]:
            continue
        
        if len(mst) < n - 1:
            mst.append((u, weight))
        else:
            break
        for v in range(n):
            if not visited[v] and adj_matrix[u][v] != 0:
                MinHeap.insert(heap, (adj_matrix[u][v], v))
        
        visited[u] = True
        mst_cost += weight

    return mst, mst_cost


      




#  matrix - becusea complete so everyone conected
# randomly generate coordinates 
# weights = euclidian distance of these nodes
# list of node index to coordinates

# an MST function