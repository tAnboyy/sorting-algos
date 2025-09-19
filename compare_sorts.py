# Compare sorting algorithms: plot random, sorted, reverse sorted input timings for all algorithms
import os
import importlib.util
import matplotlib.pyplot as plt

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

# Each sort file should have a function: get_results() returning a dict like {'random': {'sizes': [...], 'times': [...]}, ...}
def get_results_from_file(file_path):
    spec = importlib.util.spec_from_file_location('sortmod', file_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, 'get_results'):
        return mod.get_results()
    return {}

def main():
    for sort_file, label in zip(SORT_FILES, SORT_LABELS):
        file_path = os.path.join(os.path.dirname(__file__), sort_file)
        results = get_results_from_file(file_path)
        for key in RESULTS:
            if key in results:
                RESULTS[key][label] = (results[key]['sizes'], results[key]['times'])

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    input_types = ['random', 'sorted', 'reverse_sorted']
    for idx, key in enumerate(input_types):
        ax = axes[idx]
        for label in SORT_LABELS:
            if label in RESULTS[key]:
                sizes, times = RESULTS[key][label]
                ax.plot(sizes, times, marker='o', label=label)
        ax.set_xlabel('Input Size')
        ax.set_ylabel('Avg. Execution Time (s)')
        ax.set_title(f'{key.capitalize()} Inputs')
        ax.grid(True)
        ax.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
