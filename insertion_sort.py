# Insertion Sort, timing, and plotting for multiple input files
import os
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key

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
	input_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.txt')], key=extract_size)
	results = {
		'random': {'sizes': [], 'times': []},
		'sorted': {'sizes': [], 'times': []},
		'reverse_sorted': {'sizes': [], 'times': []}
	}
	for filename in input_files:
		filepath = os.path.join(input_dir, filename)
		arr = read_input_file(filepath)
		n = len(arr)
		if n > 20000:
			print(f"File: {filename} | Input size: {n} -- Skipped (too large for insertion sort)")
			continue
		times = []
		num_runs = 3 if n > 10000 else 5
		for _ in range(num_runs):
			arr_copy = arr.copy()
			start = time.perf_counter()
			insertion_sort(arr_copy)
			end = time.perf_counter()
			times.append(end - start)
		avg_time = sum(times) / len(times)
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
	return results

def get_results():
	return main()

if __name__ == "__main__":
	main()