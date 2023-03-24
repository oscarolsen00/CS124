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

def adjacency_list(n : int, vertices : dict, dim : int):
    graph = []
    if dim == 1:
        for vertex in vertices:
            graph[vertex] = [v for v in vertices if v != vertex]
        
        for i in range(0,n):
            graph[vertexi].append()
    else:

        graph[vertexi].append()

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




# class for a heap

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return int(i / 2)

    def left_child(self, i):
        return 2 * i

    def right_child(self, i):
        return 2 * i + 1

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        # i = self.heap[-1]
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
    heap = MinHeap()
    heap.insert((0, 0)) # (dist, vertex)
    mst_cost = 0
    len_mst = 0

    while heap:
        weight, u = MinHeap.extract_min(heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += weight
        if len_mst < n - 1:
            len_mst += 1
            
        else:
            break
        for v in range(n):
            if not visited[v] and adj_matrix[u][v] != 0:
                MinHeap.insert(heap, (adj_matrix[u][v], v))

    return mst_cost

def main(dim,vertices,numtrials):
    x = 0
    sum = 0
    while x != numtrials:
        test_vert = vertices_gen(vertices, dim)
        matrix_1 = matrix(vertices, test_vert, dim)
        sum += prim_mst_heap_adjacency(matrix_1)
        x += 1
    average = sum/numtrials

    return average

Dimensions = 2
Num_vertices1 = 32768
Num_vertices2 = 65536
Num_vertices3 = 131072
Num_vertices4 = 262144
num_trials = 5

# print("Average 32768=", main(Dimensions,Num_vertices1,num_trials),',', "Number of vertices = ",
#          Num_vertices1,',', "Number of trials = ", num_trials,',', "Dimensions = ", Dimensions)
# print("Average 65536=", main(Dimensions,Num_vertices2,num_trials),',', "Number of vertices = ",
#          Num_vertices2,',', "Number of trials = ", num_trials,',', "Dimensions = ", Dimensions)
# print("Average 131072=", main(Dimensions,Num_vertices3,num_trials),',', "Number of vertices = ",
#          Num_vertices3,',', "Number of trials = ", num_trials,',', "Dimensions = ", Dimensions)  
print("Average 262144=", main(Dimensions,Num_vertices4,num_trials),',', "Number of vertices = ",
         Num_vertices4,',', "Number of trials = ", num_trials,',', "Dimensions = ", Dimensions)          

print("hello")
