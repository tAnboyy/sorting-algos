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
		# If the file looks like a Python list, use eval safely
		if content.startswith('[') and content.endswith(']'):
			import ast
			return ast.literal_eval(content)
		# Otherwise, fallback to splitting by whitespace
		return [int(x) for x in content.split()]

def main():
	input_dir = 'inputs_DSA_project'
	def extract_size(filename):
		# Handles random_in_1000.txt, sorted_in_1000.txt, reverse_sorted_in_1000.txt, etc.
		parts = filename.split('_')
		for part in reversed(parts):
			if part.isdigit():
				return int(part)
			if part.endswith('.txt') and part[:-4].isdigit():
				return int(part[:-4])
		return 0
	input_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.txt')],
						key=extract_size)
	sizes = []
	avg_times = []
	for filename in input_files:
		filepath = os.path.join(input_dir, filename)
		arr = read_input_file(filepath)
		n = len(arr)
		times = []
		num_runs = 3 if n > 10000 else 5
		for _ in range(num_runs):
			arr_copy = arr.copy()
			start = time.perf_counter()
			insertion_sort(arr_copy)
			end = time.perf_counter()
			times.append(end - start)
		avg_time = sum(times) / len(times)
		sizes.append(n)
		avg_times.append(avg_time)
		print(f"File: {filename} | Input size: {n}, Average time over {num_runs} runs: {avg_time:.6f} seconds")

	# Plotting
	plt.figure(figsize=(10,6))
	plt.plot(sizes, avg_times, marker='o')
	plt.xlabel('Input Size')
	plt.ylabel('Average Execution Time (seconds)')
	plt.title('Insertion Sort: Input Size vs Average Execution Time')
	plt.grid(True)
	plt.tight_layout()
	plt.show()

if __name__ == "__main__":
	main()
