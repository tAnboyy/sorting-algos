import time

def insertion_sort(arr):
    def binary_search(sub_arr, val, start, end):
        while start < end:
            mid = (start + end) // 2
            if sub_arr[mid] < val:
                start = mid + 1
            else:
                end = mid
        return start

    for i in range(1, len(arr)):
        key = arr[i]
        # Find the insertion point using binary search
        insert_pos = binary_search(arr, key, 0, i)
        # Shift elements to the right to make space
        for j in range(i, insert_pos, -1):
            arr[j] = arr[j - 1]
        arr[insert_pos] = key

def main(inputs_dict):
    print("Running Insertion Sort...")
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
                insertion_sort(arr_copy)
                end = time.perf_counter()
                times.append(end - start)
            avg_time = sum(times) / len(times)
            results[key]['sizes'].append(n)
            results[key]['times'].append(avg_time)
            print(f"{key.capitalize()} Input size: {n}, Average time over {num_runs} runs: {avg_time:.6f} seconds")
    print("******* Insertion Sort Finished *******")
    return results


def get_results(inputs_dict):
    return main(inputs_dict)
