# This file compares sorting algorithms and plots random, sorted, reverse sorted input timings for all algorithms

import os
import importlib.util
import matplotlib.pyplot as plt
import pandas as pd
import random

SORT_FILES = [
    'insertion_sort.py',
    'merge_sort.py',
    'heap_sort.py',
    'quick_sort.py',
    'modified_quick_sort.py',
]

SORT_LABELS = [
    'Insertion Sort',
    'Merge Sort',
    'Heap Sort',
    'Quick Sort',
    'Modified Quick Sort',
]

COLOR_MAP = {
    'random': 'red',
    'sorted': 'blue',
    'reverse_sorted': 'green',
}

RESULTS = {
    'random': {},
    'sorted': {},
    'reverse_sorted': {},
}


# each sort file has a function: get_results(inputs_dict) returning a dict
def get_results_from_file(file_path, inputs_dict):
    spec = importlib.util.spec_from_file_location('sortmod', file_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, 'get_results'):
        return mod.get_results(inputs_dict)
    return {}

def main():

    # input sizes as per requirement
    sizes = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 50000, 60000, 80000, 90000, 100000]

    # generating dynamic inputs for each type and size
    dynamic_inputs = {'random': {}, 'sorted': {}, 'reverse_sorted': {}}
    for size in sizes:
        arr = [random.randint(0, 10**6) for _ in range(size)]
        dynamic_inputs['random'][size] = arr.copy()
        arr_sorted = sorted(arr)
        dynamic_inputs['sorted'][size] = arr_sorted.copy()
        dynamic_inputs['reverse_sorted'][size] = arr_sorted[::-1]

    # For each sorting algorithm, calling get_results(inputs_dict)
    for sort_file, label in zip(SORT_FILES, SORT_LABELS):
        file_path = os.path.join(os.path.dirname(__file__), sort_file)
        results = get_results_from_file(file_path, dynamic_inputs)
        for key in RESULTS:
            if key in results:
                RESULTS[key][label] = (results[key]['sizes'], results[key]['times'])


    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    input_types = ['random', 'sorted', 'reverse_sorted']
    table_data = []
    for idx, key in enumerate(input_types):
        ax = axes[idx]
        for label in SORT_LABELS:
            if label in RESULTS[key]:
                sizes, times = RESULTS[key][label]
                ax.plot(sizes, times, marker='o', label=label)
                #collecting data for table
                for size, t in zip(sizes, times):
                    table_data.append({
                        'Input Type': key.capitalize(),
                        'Sorting Algorithm': label,
                        'Input Size': size,
                        'Execution Time (s)': t
                    })
        ax.set_xlabel('Input Size')
        ax.set_ylabel('Avg. Execution Time (s)')
        ax.set_title(f'{key.capitalize()} Inputs')
        ax.grid(True)
        ax.legend()
    plt.tight_layout()
    plt.show()

    # Creating and plotting a simple table using pandas and matplotlib
    df = pd.DataFrame(table_data)
    df = df.sort_values(['Sorting Algorithm', 'Input Type', 'Input Size'])
    # displaying only the relevant columns in a simple table
    display_df = df[['Sorting Algorithm', 'Input Type', 'Input Size', 'Execution Time (s)']]
    fig, ax = plt.subplots(figsize=(12, min(1 + 0.3 * len(display_df), 20)))
    ax.axis('off')
    table = ax.table(
        cellText=display_df.values,
        colLabels=display_df.columns,
        loc='center',
        cellLoc='center',
        colLoc='center',
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width(col=list(range(len(display_df.columns))))
    plt.title('Execution Times for Sorting Algorithms')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
