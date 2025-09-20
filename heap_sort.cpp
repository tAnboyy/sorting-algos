// Heap Sort, timing, and input generation (C++)
#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <algorithm>
#include <random>

void heap_sort(std::vector<int>& arr) {
    std::make_heap(arr.begin(), arr.end());
    std::sort_heap(arr.begin(), arr.end());
}

std::vector<int> generate_input(size_t size, const std::string& type) {
    std::vector<int> arr(size);
    if (type == "random") {
        std::mt19937 rng(42);
        std::uniform_int_distribution<int> dist(0, size * 10);
        for (size_t i = 0; i < size; ++i) arr[i] = dist(rng);
    } else if (type == "sorted") {
        for (size_t i = 0; i < size; ++i) arr[i] = i;
    } else if (type == "reverse_sorted") {
        for (size_t i = 0; i < size; ++i) arr[i] = size - i;
    }
    return arr;
}

int main() {
    std::cout << "Running Heap Sort..." << std::endl;
    std::vector<size_t> sizes = {1000,2000,3000,4000,5000,10000,20000,40000,50000,60000,80000,90000,100000};
    std::vector<std::string> types = {"random", "sorted", "reverse_sorted"};
    for (const auto& type : types) {
        for (auto size : sizes) {
            std::vector<int> arr = generate_input(size, type);
            int num_runs = (size > 10000) ? 3 : 5;
            double total_time = 0.0;
            for (int run = 0; run < num_runs; ++run) {
                std::vector<int> arr_copy = arr;
                auto start = std::chrono::high_resolution_clock::now();
                heap_sort(arr_copy);
                auto end = std::chrono::high_resolution_clock::now();
                std::chrono::duration<double> elapsed = end - start;
                total_time += elapsed.count();
            }
            double avg_time = total_time / num_runs;
            std::cout << "Type: " << type << " | Size: " << size << ", Avg time: " << avg_time << " seconds" << std::endl;
        }
    }
    std::cout << "******* Heap Sort Finished *******" << std::endl;
    return 0;
}
