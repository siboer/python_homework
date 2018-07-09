

#select sort

def find_smallest(myarray):
	s_index = 0
	smallest = myarray[0]

	for index in range(0,len(myarray)):
		if myarray[index] < smallest:
			smallest = myarray[index]
			s_index = index

	return index


def select_sort(newarray):
	sorted_list = []
	for index in range(0,len(newarray)):
		sorted_list.append(newarray.pop(find_smallest(newarray)))

	return sorted_list






