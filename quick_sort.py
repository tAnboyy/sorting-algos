# In-place Quick Sort (pivot: random item), timing, and plotting for multiple input files
import time
import random

def quick_sort(arr, low, high):
    while low < high:
        pi = partition(arr, low, high)
        # Tail call elimination: sort smaller part first
        if pi - low < high - pi:
            quick_sort(arr, low, pi - 1)
            low = pi + 1
        else:
            quick_sort(arr, pi + 1, high)
            high = pi - 1

def partition(arr, low, high):
    # Select a random pivot and swap with high
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main(inputs_dict = None):
    print("Running Quick Sort...")
    if inputs_dict is None:
        print("No input provided.")
        return
    else:
        # Dynamic input handling
        results = {
            'random': {'sizes': [], 'times': []},
            'sorted': {'sizes': [], 'times': []},
            'reverse_sorted': {'sizes': [], 'times': []}
        }
        for key in ['random', 'sorted', 'reverse_sorted']:
            for n, arr in inputs_dict.get(key, {}).items():
                times = []
                num_runs = 3 if n > 10000 else 5
                for _ in range(num_runs):
                    arr_copy = arr.copy()
                    start = time.perf_counter()
                    quick_sort(arr_copy, 0, len(arr_copy) - 1)
                    end = time.perf_counter()
                    times.append(end - start)
                avg_time = sum(times) / len(times)
                results[key]['sizes'].append(n)
                results[key]['times'].append(avg_time)
                print(f"{key.capitalize()} Input size: {n}, Average time over {num_runs} runs: {avg_time:.6f} seconds")
        print("******* Quick Sort Finished *******")
        return results

def get_results(inputs_dict = None):
    return main(inputs_dict)

if __name__ == "__main__":
    main()
