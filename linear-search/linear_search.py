def linear_search(lst, to_find):
  a=-1
  for x in range(0,len(lst)+1):
    if to_find == lst[x]:
      a=x
      break
    else:
      continue
  return a
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
