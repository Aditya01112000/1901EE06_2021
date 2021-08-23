def get_memory_score(l):
    # for storing final score
    score = 0
    # helper list
    n = []

    for i in range(len(l)):
        # if element is already present in list increment score
        if l[i] in n:
            score += 1
        # size of helper list=5 then remove first element and append list element into helper list
        elif len(n) == 5:
            n.remove(n[0])
            n.append(l[i])
        # add element to helper list
        else:
            n.append(l[i])
    return score


input_nums = [1,4,"a",3,5,"Star",7.5]
# temporary list for storing invalid character
list1 = []

# Traversing the array
for i in range(len(input_nums)):
    temp_string = str(input_nums[i])

    # using isdigit() function for checking integer
    if temp_string.isdigit():
        pass
    else:
        list1.append(input_nums[i])

# if temporary list size=0 then the given input is valid
if len(list1) != 0:
    print("Please enter a valid input list.")
    print("Invalid inputs detected :", list1)
else:
    print("Score:", get_memory_score(input_nums))