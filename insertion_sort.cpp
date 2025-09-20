// Insertion Sort, timing, and input reading for multiple input files (C++)
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <chrono>
#include <filesystem>
#include <algorithm>

void insertion_sort(std::vector<int>& arr) {
    for (size_t i = 1; i < arr.size(); ++i) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
    }
}

std::vector<int> read_input_file(const std::string& filepath) {
    std::ifstream file(filepath);
    std::vector<int> arr;
    std::string line;
    if (std::getline(file, line)) {
        // Handle Python list format: [1, 2, 3, ...]
        if (!line.empty() && line.front() == '[' && line.back() == ']') {
            line = line.substr(1, line.size() - 2); // remove [ and ]
            std::replace(line.begin(), line.end(), ',', ' ');
        }
        std::istringstream iss(line);
        int num;
        while (iss >> num) {
            arr.push_back(num);
        }
    }
    return arr;
}

int main() {
    std::cout << "Running Insertion Sort..." << std::endl;
    std::string input_dir = "inputs_DSA_project";
    std::vector<std::string> input_files;
    for (const auto& entry : std::filesystem::directory_iterator(input_dir)) {
        if (entry.path().extension() == ".txt") {
            input_files.push_back(entry.path().filename().string());
        }
    }
    // Sort files by size in filename
    std::sort(input_files.begin(), input_files.end(), [](const std::string& a, const std::string& b) {
        auto extract_size = [](const std::string& filename) {
            size_t pos = filename.find_last_of('_');
            if (pos != std::string::npos) {
                std::string num = filename.substr(pos + 1);
                if (num.ends_with(".txt")) num = num.substr(0, num.size() - 4);
                try { return std::stoi(num); } catch (...) { return 0; }
            }
            return 0;
        };
        return extract_size(a) < extract_size(b);
    });
    for (const auto& filename : input_files) {
        std::string filepath = input_dir + "/" + filename;
        std::vector<int> arr = read_input_file(filepath);
        size_t n = arr.size();
        if (n > 60000) {
            std::cout << "File: " << filename << " | Input size: " << n << " -- Skipped (input size > 60000)" << std::endl;
            continue;
        }
        int num_runs = (n > 10000) ? 3 : 5;
        double total_time = 0.0;
        for (int run = 0; run < num_runs; ++run) {
            std::vector<int> arr_copy = arr;
            auto start = std::chrono::high_resolution_clock::now();
            insertion_sort(arr_copy);
            auto end = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double> elapsed = end - start;
            total_time += elapsed.count();
        }
        double avg_time = total_time / num_runs;
        std::cout << "File: " << filename << " | Input size: " << n << ", Average time over " << num_runs << " runs: " << avg_time << " seconds" << std::endl;
    }
    std::cout << "******* Insertion Sort Finished *******" << std::endl;
    return 0;
}
