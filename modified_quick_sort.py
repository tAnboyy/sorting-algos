# Modified Quick Sort (median-of-three pivot, insertion sort for small subarrays)
import time

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    a, b, c = arr[low], arr[mid], arr[high]
    if a > b:
        if a < c:
            median = low
        elif b > c:
            median = mid
        else:
            median = high
    else:
        if a > c:
            median = low
        elif b < c:
            median = mid
        else:
            median = high
    return median

def modified_quick_sort(arr, low, high):
    while low < high:
        if high - low + 1 <= 20:
            insertion_sort(arr, low, high)
            break
        else:
            pivot_index = median_of_three(arr, low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            pi = partition(arr, low, high)
            # Tail call optimization ie- sorting smaller part first
            if pi - low < high - pi:
                modified_quick_sort(arr, low, pi - 1)
                low = pi + 1
            else:
                modified_quick_sort(arr, pi + 1, high)
                high = pi - 1

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main(inputs_dict):
    print("Running Modified Quick Sort...")
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
                modified_quick_sort(arr_copy, 0, len(arr_copy) - 1)
                end = time.perf_counter()
                times.append(end - start)
            avg_time = sum(times) / len(times)
            results[key]['sizes'].append(n)
            results[key]['times'].append(avg_time)
            print(f"{key.capitalize()} Input size: {n}, Average time over {num_runs} runs: {avg_time:.6f} seconds")
    print("******* Modified Quick Sort Finished *******")
    return results

def get_results(inputs_dict):
    return main(inputs_dict)

if __name__ == "__main__":
    main()
