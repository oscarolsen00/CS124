#include <iostream>
#include <random>
#include <vector>
#include <cmath>
#include <map>
#include <tuple>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;


double euc_dist(vector<double>& a, vector<double>& b){
    double distance = 0;
    for (int i = 0; i < a.size(); i++) {
        distance += pow(a[i] - b[i], 2);
    }
    return sqrt(distance);
}

std::map<int, std::vector<double> > vertices_gen(int n, int dim) {
    std::map<int, std::vector<double> > vertices;
    std::srand(std::time(nullptr)); // Seed the random number generator

    for (int i = 0; i < n; i++) {
        std::vector<double> coordinates;
        for (int j = 1; j < dim + 1; j++) {
            double coord = (double)std::rand() / RAND_MAX; // Generate a random coordinate
            coordinates.push_back(coord); // Add the coordinate to the vector
        }
        vertices.insert(std::make_pair(i, coordinates)); // Add the vector to the map
    }

    return vertices;
}

vector<vector<double> > matrix(int n, map<int, vector<double> >& vertices, int dim){
    vector<vector<double> > graph(n, vector<double>(n, 0));
    if(dim == 1){
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(j > i){
                    graph[i][j] = ((double) std::rand() / (RAND_MAX));
                } else {
                    graph[i][j] = graph[j][i];
                }
            }
        }
    } else {
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(j > i){
                    graph[i][j] = euc_dist(vertices[i], vertices[j]);
                } else {
                    graph[i][j] = graph[j][i];
                }
            }
        }
    }
    return graph;
}

class MinHeap {  
public:
    vector<pair<double, int> > heap;
    int parent(int i){
        return i/ 2;
        // return ceil((double)i/ 2);
    }

    int left_child(int i){
        return 2*i + 1;
    }

    int right_child(int i){
        return 2*i + 2;
    }

    void swap(int i, int j){
        pair<double, int> temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    void insert(pair<double, int> k){
        heap.push_back(k);
        int i = heap.size()-1;
        while(i != 0 && heap[parent(i)].first > heap[i].first){
            swap(i, parent(i));
            i = parent(i);
        }
    }

    void heapify(int i){
        int l = left_child(i);
        int r = right_child(i);
        int smallest = i;
        if(l < heap.size() && heap[l].first < heap[i].first){
            smallest = l;
        }
        if(r < heap.size() && heap[r].first < heap[smallest].first){
            smallest = r;
        }
        if(smallest != i){
            swap(i, smallest);
            heapify(smallest);
        }
    }

    // void push(pair<double, int> k){
    //     insert(k);
    // }

    pair<double, int> pop(){
        pair<double, int> min_tup = heap[0];
        heap[0] = heap[heap.size()-1];
        heap.pop_back();
        heapify(0);
        return min_tup;
    }

    // bool empty(){
    //     return heap.empty();
    // }
};


double prim_mst_heap_adjacency(vector<vector<double> > adj_matrix) {
    int n = adj_matrix.size();
    vector<bool> visited(n, false);
    MinHeap heap;
    heap.insert(std::make_pair(0, 0)); // (dist, vertex)
    double mst_cost = 0;
    int len_mst = 0;

    while (!heap.heap.empty()) {
        // int weight, u;
        const auto weight_u = heap.pop();
        // weight, u = heap.pop();
        if (visited[weight_u.second]) {
            continue;
        }
        visited[weight_u.second] = true;
        mst_cost += weight_u.first;
        if (len_mst < n - 1) {
            len_mst += 1;
        } else {
            break;
        }
        for (int v = 0; v < n; v++) {
            if (!visited[v] && adj_matrix[weight_u.second][v] != 0) {
                heap.insert(std::make_pair(adj_matrix[weight_u.second][v], v));
            }
        }
    }

    return mst_cost;
}

double fun1(int dim, int vertices, int numtrials) {
    int x = 0;
    double sum = 0;
    while (x != numtrials) {
        auto test_vert = vertices_gen(vertices, dim);
        auto matrix_1 = matrix(vertices,test_vert, dim);
        sum += prim_mst_heap_adjacency(matrix_1);
        x += 1;
    }
    double average = sum/numtrials;

    return average;
}

int main() {
    
    // vector<double> Num_vertices{128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144}
    // vector<int> Num_vertices{ 128, 256 };
    // vector<int> Dimensions{ 1, 2, 3, 4 };
    int num_trials = 5;

    vector<int> Num_vertices;
  
    Num_vertices.push_back(128);
    Num_vertices.push_back(256);
    Num_vertices.push_back(512);
    Num_vertices.push_back(1024);
    // Num_vertices.push_back(2048);
    // Num_vertices.push_back(4096);
    // Num_vertices.push_back(8192);
    // Num_vertices.push_back(16384);
    // Num_vertices.push_back(32768);
    // Num_vertices.push_back(65536);
    // Num_vertices.push_back(131072);
    // Num_vertices.push_back(262144);

    vector<int> Dimensions;

    // Dimensions.push_back(1);
    // Dimensions.push_back(2);
    Dimensions.push_back(3);
    Dimensions.push_back(4);

    // Open the CSV file for writing
    ofstream csv_file("output.csv");
    
    // Loop over each row of the output data and write it to the CSV
    for (const auto& dims : Dimensions) {
        for (const auto& ns : Num_vertices) {
            double result = fun1(dims, ns, num_trials);
            csv_file << result << ",";
            csv_file << std::endl;
        }
        csv_file << "\n";
    }
    
    // Close the CSV file
    csv_file.close();
    

    return 0;
}


// int Dimensions = 2;
    // int Num_vertices = 512;
    // int num_trials = 5;
    // double result = fun1(Dimensions, Num_vertices, num_trials);
    // cout << "Average = " << static_cast<double>(result) << ", "
    //      << "Number of vertices = " << Num_vertices << ", "
    //      << "Number of trials = " << num_trials << ", "
    //      << "Dimensions = " << Dimensions << endl;