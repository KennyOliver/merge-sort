def mergeLists(list1, list2):
  '''Merge the two sorted lists to form a single sorted list'''
  list1Pointer = 0
  list2Pointer = 0
 
  list1Length = len(list1)
  list2Length = len(list2)
 
  mergedList = []
 
  #Repeatedly add values from the lists until the end of one is reached
  while list1Pointer < list1Length and list2Pointer < list2Length:
    if list1[list1Pointer] < list2[list2Pointer]:
      mergedList.append(list1[list1Pointer])
      list1Pointer = list1Pointer + 1
    else:
      mergedList.append(list2[list2Pointer])
      list2Pointer = list2Pointer + 1

  #If there are items left in list 1 - add them all to the merged list
  if list1Pointer < list1Length:
    for index in range(list1Pointer, list1Length):
      mergedList.append(list1[index])

  #If there are items left in list 2 - add them all to the merged list
  if list2Pointer < list2Length:
    for index in range(list2Pointer, list2Length):
      mergedList.append(list2[index])

  #Return the merged list
  return mergedList
 
 
#Main Program
merged = mergeLists([2, 3, 6, 8], [1, 3, 8, 10])
print(merged)