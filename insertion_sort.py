import time

# we are using standard insertion sort implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

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
