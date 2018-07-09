
def quick_sort(the_list):
	if len(the_list) == 1:
		return the_list

	for i in len(the_list):
		if the_list[i] < the_list[0]:
			a_list.append(the_list[i])
		if the_list[i] > the_list[0]:
			b_list.append(the_list[i])

	return quick_sort(a_list)+the_list[0]+quick_sort(b_list)
	