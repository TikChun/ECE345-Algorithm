import math
def countsort(array):
  a = 1
  max=array[0]
  while (a < len(array)):
    if(array[a]>max):
      max = array[a]
    a = a + 1
  freq_list = []*max
  a = 0
  while (a < len(array) ):
    freq_list[array[a]] +=1
    a += 1
  result = []
  a = 0
  while(a<len(freq_list)):
    duplicate = freq_list[a]
    if(duplicate != 0):
      count = 0
      while(count!= 0):
        result.append(a)
        count = count - 1
    a = a + 1
  return result


def int_digit(number,target_digit):
  total_length = len(str(number))
  if(target_digit >= total_length):
    print("Can't be done, you are asking for more digits than it truely has")
    return -1
  elif(target_digit < 0):
    print("Can't be done, you are asking for negative digits")
    return -1
  else:
    result = str(number)
    digit = len(result) - 1 - target_digit
    return int(result[digit])


def radix_sort(array):
  #assume all int in array are of same length
  total_length = len(str(array[0]))
  current_digit = 0
  current_temp=[]
  next_temp=[]
  while(current_digit<total_length):
    current_num = 0
    a=0
    current_temp=[]
    while(a<10):
      current_temp.append([])
      a=a+1
    while(current_num < len(array)):
      digit = int_digit(array[current_num],current_digit)
      current_temp[digit].append(array[current_num])
      current_num += 1
    for small_list in current_temp:
      for elements in small_list:
        next_temp.append(elements)
    array = next_temp
    next_temp=[]
    current_digit += 1

  return array

def list_swap(array,a,b):
  array[a],array[b]=array[b],array[a]



def quick_sort(array):
  length = len(array)
  pivot = 0
  pivot_num = array[pivot]
  left_turn = False
  right_turn = True
  if(length ==1):
    return array
  elif(length == 2):
    if(array[0]>array[1]):
      array[0],array[1]=array[1],array[0]
      return array
    else:
      return array
  else:
    larger = 1
    lesser = length-1
    while(lesser != larger):
      while(right_turn):
        if(array[lesser]<pivot_num):
          list_swap(array,lesser,pivot)
          pivot = lesser
          right_turn = False
          left_turn = True
        else:
          lesser = lesser - 1
          if(lesser == larger):
            right_turn = False
      while(left_turn):
        if(array[larger]>pivot_num):
          list_swap(array,larger,pivot)
          pivot = larger
          left_turn = False
          right_turn = True
        else:
          larger = larger+1
          if(lesser==larger):
            left_turn = False
    #round accomplished
    array1 = array[:lesser]
    array2 = array[larger:]
    result=quick_sort(array1)
    temp = quick_sort(array2)
    result.extend(temp)
    return result

def merge_sort(array):
  if(len(array)>=2):
    middle = len(array)//2
    array1 = array[:middle]
    array2 = array[middle:]
    return merge(merge_sort(array1),merge_sort(array2))
  else:
    return array

def merge(array_left,array_right):
  length_left=len(array_left)
  length_right=len(array_right)
  result = []
  left=0
  right=0
  while(left!=length_left and right!=length_right):
    if(array_left[left]<=array_right[right]):
      result.append(array_left[left])
      left = left+1
    elif(array_right[right]<=array_left[left]):
      result.append(array_right[right])
      right = right+1
  if(left==length_left and right!=length_right):
    result.extend(array_right[right:])
  elif(left!=length_left and right==length_right):
    result.extend(array_left[left:])
  return result


def randomized_selection(array,min_num):
  length = len(array)
  pivot = 0
  pivot_num = array[pivot]
  left_turn = False
  right_turn = True
  if(min_num > length):
    print("impossible")
  elif(length ==1):
    return array[0]
  elif(length == 2):
    if(array[0]>array[1]):
      array[0],array[1]=array[1],array[0]
      return array[min_num-1]
    else:
      return array[min_num-1]
  else:
    larger = 1
    lesser = length-1
    while(lesser != larger):
      while(right_turn):
        if(array[lesser]<pivot_num):
          list_swap(array,lesser,pivot)
          pivot = lesser
          right_turn = False
          left_turn = True
        else:
          lesser = lesser - 1
          if(lesser == larger):
            right_turn = False
      while(left_turn):
        if(array[larger]>pivot_num):
          list_swap(array,larger,pivot)
          pivot = larger
          left_turn = False
          right_turn = True
        else:
          larger = larger+1
          if(lesser==larger):
            left_turn = False
    #round accomplished
    array1 = array[:lesser]
    array2 = array[larger:]
    if(min_num<=len(array1)):
      #print(array1)
      #print(array2)
      #print(min_num)
      #print("case1")
      return randomized_selection(array1,min_num)
    else:
      #print("case3")
      return randomized_selection(array2,min_num-len(array1))
