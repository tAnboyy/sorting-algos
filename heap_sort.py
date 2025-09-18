# Heap Sort (vector-based, insert one item at a time), timing, and plotting for multiple input files
import os
import time
import matplotlib.pyplot as plt
import heapq

def heap_sort(arr):
    heap = []
    # Insert one item at a time into the heap
    for item in arr:
        heapq.heappush(heap, item)
    # Extract items from the heap to get sorted order
    for i in range(len(arr)):
        arr[i] = heapq.heappop(heap)

def read_input_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read().strip()
        if content.startswith('[') and content.endswith(']'):
            import ast
            return ast.literal_eval(content)
        return [int(x) for x in content.split()]

def main():
    input_dir = 'inputs_DSA_project'
    def extract_size(filename):
        parts = filename.split('_')
        for part in reversed(parts):
            if part.isdigit():
                return int(part)
            if part.endswith('.txt') and part[:-4].isdigit():
                return int(part[:-4])
        return 0
    input_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.txt')],
                        key=extract_size)
    # Store results by type
    results = {
        'random': {'sizes': [], 'times': []},
        'sorted': {'sizes': [], 'times': []},
        'reverse_sorted': {'sizes': [], 'times': []}
    }
    for filename in input_files:
        filepath = os.path.join(input_dir, filename)
        arr = read_input_file(filepath)
        n = len(arr)
        times = []
        num_runs = 3 if n > 10000 else 5
        for _ in range(num_runs):
            arr_copy = arr.copy()
            start = time.perf_counter()
            heap_sort(arr_copy)
            end = time.perf_counter()
            times.append(end - start)
        avg_time = sum(times) / len(times)
        # Determine type by filename
        if filename.startswith('random'):
            key = 'random'
        elif filename.startswith('sorted'):
            key = 'sorted'
        elif filename.startswith('reverse_sorted'):
            key = 'reverse_sorted'
        else:
            key = 'random'  # fallback
        results[key]['sizes'].append(n)
        results[key]['times'].append(avg_time)
        print(f"File: {filename} | Input size: {n}, Average time over {num_runs} runs: {avg_time:.6f} seconds")

    # Plotting
    plt.figure(figsize=(10,6))
    if results['random']['sizes']:
        plt.plot(results['random']['sizes'], results['random']['times'], marker='o', color='red', label='Random')
    if results['sorted']['sizes']:
        plt.plot(results['sorted']['sizes'], results['sorted']['times'], marker='o', color='blue', label='Sorted')
    if results['reverse_sorted']['sizes']:
        plt.plot(results['reverse_sorted']['sizes'], results['reverse_sorted']['times'], marker='o', color='green', label='Reverse Sorted')
    plt.xlabel('Input Size')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Heap Sort: Input Size vs Average Execution Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
