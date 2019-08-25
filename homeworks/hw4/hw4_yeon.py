### Insertion Sort : O(n^2)
# https://en.wikipedia.org/wiki/Insertion_sort
def InsertionSort(numbers):
	for i in range(1, len(numbers)): # Start from the second element
		value = numbers[i] # Save the element to be inserted
		for j in range(i): # Compare the elements with elements on its left to find the position to insert 
			if value < numbers[j]: 
				numbers.pop(i)
				numbers.insert(j, value)
				break # break the loop after the insertion
		print(numbers)
	return numbers

## Testing InsertionSort
test = [3, 7, 4, 9, 5, 2, 6, 8, 1]
InsertionSort(test)


### Merge Sort : O(nlogn)
# https://en.wikipedia.org/wiki/Merge_sort

def MergeSort(numbers):
	if len(numbers) == 1: 
		return numbers  # Stop the recursion(spliting the list) when sublists have only one element. 
	print("Dividing", numbers)
	mid = len(numbers)//2
	g1 = MergeSort(numbers[:mid])
	g2 = MergeSort(numbers[mid:])
	sorted_numbers = []
	print("Merging", g1, "and", g2)
	while len(g1) > 0 and len(g2) > 0:
		if g1[0] < g2[0]:
			sorted_numbers.append(g1[0])
			g1.pop(0)
		else:
			sorted_numbers.append(g2[0])
			g2.pop(0)
	if len(g1) == 0: 
		sorted_numbers += g2
	if len(g2) == 0: 
		sorted_numbers += g1
	return sorted_numbers

## Testing MergeSort
test = [3, 7, 4, 9, 5, 2, 6, 8, 1]
print(MergeSort(test))






