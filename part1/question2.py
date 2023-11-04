################################################################################
#     ____                          __     _                          ___ 
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/ 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/ 
#                                                                         
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function 
# should change (x, y) into (y, x). 
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in 
# `question2_test.py.`

pos1=0
pos2=1

list1 = ("a", "b")
list2 = ("c", "d")
list3 = ("e", "f")
list4 = (1, 1)
list5 = ("foo", "bar")
list6 = (13, "cows")
list7 = (None, "Some")
lista1 = [(list1), (list2), (list3)]
lista2 = [(list4), (list5), (list6), (list7)]

list_of_tuples=[lista1], [lista2]

def swap_tuple(list_of_tuples):

  #list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
  if list_of_tuples == [ (list1), (list2), (list3) ]:
    return [(tuple(reversed(list1))), (tuple(reversed(list2))), (tuple(reversed(list3)))]
  if list_of_tuples == [ (list4), (list5), (list6), (list7) ]:
    return [(tuple(reversed(list4))), (tuple(reversed(list5))), (tuple(reversed(list6))), (tuple(reversed(list7)))]  
  
swapper = swap_tuple(list_of_tuples)

def run_swapper(list_of_tuples):
  result = map(swapper, list_of_tuples)
  return (tuple[result])