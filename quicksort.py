from random import randrange, shuffle
def quicksort(list):
  # this portion of listay has been sorted
  if len(list) <= 1:
    return list

  # select random element to be pivousj
  pivot_idx = randrange(len(list)-1)
  print(pivot_idx)
  pivot_element = list[pivot_idx]

  # swap random element with last element in sublistay
  #list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  #less_than_pointer = start
  sub_list_left = []
  sub_list_right = []
  for i in range(0, len(list)-1):
    # we found an element out of place
    if list[i] < pivot_element:
        sub_list_left.append(list[i])
    elif list[i] >= pivot_element:
        sub_list_right.append(list[i])
      #less_than_pointer += 1
  # Call quicksort on the "left" and "right" sub-lists
  return quicksort(sub_list_left), quicksort(sub_list_right)


unsorted_list = [3,7,12,24,36,42]
shuffle(unsorted_list)
print(unsorted_list)
# use quicksort to sort the list, then print it out!
print(quicksort(unsorted_list))
