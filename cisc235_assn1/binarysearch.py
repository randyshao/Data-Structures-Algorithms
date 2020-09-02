#Name: Randy Shao
#Student Number: 20100992

#This function creates a binary search algorithm and returns the number of function calls
def bin_search(num_list, first, last, target, count):

    if first > last:
        return count
    else:
        mid = (first + last) // 2
        if num_list[mid] == target:
            return count
        elif num_list[mid] > target:
            count += 1
            return bin_search(num_list, first, mid - 1, target, count)
        else:
            count += 1
            return bin_search(num_list, mid + 1, last, target, count)

#This function creates a trinary search algorithm and returns the number of function calls
def trin_search(num_list, first, last, target, count):

    if first > last:
        return count
    else:
        one_third = first + (last-first) // 3
        two_thirds = first + 2 * (last-first) // 3

    if num_list[one_third] == target:
        return count
    elif num_list[one_third] > target:
        count += 1
        return trin_search(num_list, first, one_third-1, target, count)
    elif num_list[two_thirds] == target:
        return count
    elif num_list[two_thirds] > target:
        count += 1
        return trin_search(num_list, one_third+1, two_thirds-1, target, count)
    else:
        count += 1
        return trin_search(num_list, two_thirds+1, last, target, count)

#This function creates a list of values based on the given size and returns a sorted list
def list_maker(size):

    list_sorted = []
    for i in range(size):
        list_sorted.append(i)
    return list_sorted

#This function creates a list of even values based on the given size and returns a sorted list
def even_list_maker(size):

    list_sorted = []
    for i in range(size):
        list_sorted.append(i * 2)
    return list_sorted

#This function returns the average number of function calls for binary search
def avg_bin_search(size):

    list_final = list_maker(size)
    count = 0
    for i in range(size):
        count += bin_search(list_final, 0, list_final[-1], i, 1)
    avg_call = count / size
    return avg_call

#This function returns the average number of function calls for trinary search
def avg_trin_search(size):

    list_final = list_maker(size)
    count = 0
    for i in range(size):
        count += trin_search(list_final, 0, list_final[-1], i, 1)
    avg_call = count / size
    return avg_call

#This function returns the average number of function calls for binary search for missing values
def odd_bin_search(size):
    list_final = even_list_maker(size)
    count = 0
    for i in range(size):
        count += bin_search(list_final, 0, list_final[-1], i, 1)
    avg_call = count / size
    return avg_call

#This function returns the average number of function calls for trinary search for missing values
def odd_trin_search(size):

    list_final = even_list_maker(size)
    count = 0
    for i in range(size):
        count += trin_search(list_final, 0, list_final[-1], i, 1)
    avg_call = count / size
    return avg_call

def main():

    num_list = [1000, 2000, 4000, 8000, 16000]
    for i in range(len(num_list)):
        avg_bin_call = avg_bin_search(num_list[i])
        avg_trin_call = avg_trin_search(num_list[i])
        odd_bin_call = odd_bin_search(num_list[i])
        odd_trin_call = odd_trin_search(num_list[i])
        print("Experiment 1 - Average number of calls for binary search with", num_list[i], "integers:", avg_bin_call)
        print("Experiment 1 - Average number of calls for trinary search with", num_list[i], "integers:", avg_trin_call)
        print("Experiment 2 - Average number of calls for binary search with", num_list[i], "integers (missing value):", odd_bin_call)
        print("Experiment 2 - Average number of calls for trinary search with", num_list[i], "integers (missing value):", odd_trin_call)

main()