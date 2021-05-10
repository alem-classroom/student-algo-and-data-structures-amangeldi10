def linear_search(lst, to_find):
  a=-1
  if to_find in lst:
    a=lst.index(to_find)
  return a
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
