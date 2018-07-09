
def quick_sort(the_list):
	if len(the_list) < 2:
		return the_list

	else:
		mid_value = the_list[0]
		less = [item for item in the_list[1:] if item < mid_value]
		great = [item for item in the_list[1:] if item >= mid_value]
		return quick_sort(less) + [mid_value] + quick_sort(great)



print (quick_sort([34,1,65,77,1,3,54,8,0,3,45,8,99,22]))