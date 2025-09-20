import time

# Recursive merge sort implementation - sorts the array in place
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        # splitting the array into two halves
        L = arr[:mid]
        R = arr[mid:]
        # Recursively sorting both halves
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        # Merging the sorted halves back into arr
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Copying any remaining elements from L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        # Copying any remaining elements from R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def main(inputs_dict):
    print("Running Merge Sort...")
    results = {
        'random': {'sizes': [], 'times': []},
        'sorted': {'sizes': [], 'times': []},
        'reverse_sorted': {'sizes': [], 'times': []}
    }
    # here we are benchmarking merge sort for each input type and size
    for key in ['random', 'sorted', 'reverse_sorted']:
        for n, arr in inputs_dict.get(key, {}).items():
            times = []
            num_runs = 3 if n > 10000 else 5
            for _ in range(num_runs):
                arr_copy = arr.copy()
                start = time.perf_counter()
                merge_sort(arr_copy)
                end = time.perf_counter()
                times.append(end - start)
            avg_time = sum(times) / len(times)
            results[key]['sizes'].append(n)
            results[key]['times'].append(avg_time)
            print(f"{key.capitalize()} Input size: {n}, Average time over {num_runs} runs: {avg_time:.6f} seconds")
    print("******* Merge Sort Finished *******")
    return results

def get_results(inputs_dict):
    return main(inputs_dict)

