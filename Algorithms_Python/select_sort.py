

#select sort

def find_smallest(myarray):
	s_index = 0
	smallest = myarray[0]

	for index in range(1,len(myarray)):
		if myarray[index] < smallest:
			smallest = myarray[index]
			s_index = index

	return s_index


def select_sort(newarray):
	sorted_array = []
	for index in range(len(newarray)):
		smallest = find_smallest(newarray)
		sorted_array.append(newarray.pop(smallest))

	return sorted_array



print (select_sort([34,4,67,89,23,4,0,123,55,789,32,435,111,222,3,65,44,3]))




