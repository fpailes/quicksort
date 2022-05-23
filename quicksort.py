from random import randrange, shuffle
def quicksort(list):
  # this portion of listay has been sorted
  if len(list) <= 1:
    return list

  # select random element to be pivousj
  pivot_idx = randrange(len(list))
  print(pivot_idx)
  pivot_element = list[pivot_idx]
  print("pivot Element: " + str(pivot_element))
  sub_list_left = []
  sub_list_right = []
# tracks all elements which should be to left (lesser than) pivot
  for i in range(0, len(list)):
    if list[i] < pivot_element:
        sub_list_left.append(list[i])
        print("left: " + str(sub_list_left))
    elif list[i] > pivot_element:
        sub_list_right.append(list[i])
        print("right: " + str(sub_list_right))


  sub_list_left.append(pivot_element)
  # Call quicksort on the "left" and "right" sub-lists
  return quicksort(sub_list_left) + quicksort(sub_list_right)


unsorted_list = [3,7,12,24,36,42]
shuffle(unsorted_list)
print(unsorted_list)
# use quicksort to sort the list, then print it out!
print(quicksort(unsorted_list))
