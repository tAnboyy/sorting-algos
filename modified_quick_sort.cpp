// Modified Quick Sort (median-of-three, insertion for small subarrays), timing, and input generation (C++)
#include <iostream>
#include <vector>
#include <string>
#include <chrono>
#include <algorithm>
#include <random>

void insertion_sort(std::vector<int>& arr, int left, int right) {
    for (int i = left + 1; i <= right; ++i) {
        int key = arr[i];
        int j = i - 1;
        while (j >= left && arr[j] > key) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
    }
}

int median_of_three(std::vector<int>& arr, int low, int high) {
    int mid = (low + high) / 2;
    if (arr[low] > arr[mid]) std::swap(arr[low], arr[mid]);
    if (arr[low] > arr[high]) std::swap(arr[low], arr[high]);
    if (arr[mid] > arr[high]) std::swap(arr[mid], arr[high]);
    return mid;
}

int partition(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; ++j) {
        if (arr[j] <= pivot) {
            ++i;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

void modified_quick_sort(std::vector<int>& arr, int low, int high) {
    while (low < high) {
        if (high - low + 1 <= 20) {
            insertion_sort(arr, low, high);
            break;
        } else {
            int m = median_of_three(arr, low, high);
            std::swap(arr[m], arr[high]);
            int pi = partition(arr, low, high);
            if (pi - low < high - pi) {
                modified_quick_sort(arr, low, pi - 1);
                low = pi + 1;
            } else {
                modified_quick_sort(arr, pi + 1, high);
                high = pi - 1;
            }
        }
    }
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
    std::cout << "Running Modified Quick Sort..." << std::endl;
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
                modified_quick_sort(arr_copy, 0, arr_copy.size() - 1);
                auto end = std::chrono::high_resolution_clock::now();
                std::chrono::duration<double> elapsed = end - start;
                total_time += elapsed.count();
            }
            double avg_time = total_time / num_runs;
            std::cout << "Type: " << type << " | Size: " << size << ", Avg time: " << avg_time << " seconds" << std::endl;
        }
    }
    std::cout << "******* Modified Quick Sort Finished *******" << std::endl;
    return 0;
}
