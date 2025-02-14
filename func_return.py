#lists and functions

#lists can be passed as arguments to functions
def list_sum(lst):
  s=0
  for i in lst:
    s+=i
  return s

print("Sum of list: ",list_sum([5,4,3]))
#print("Sum of list: ",list_sum(5)) Results in TypeError: 'int' object is not iterable


#lists can be returned as a function result
def strange_list_fun(n):
  strange_list=[]
  for i in range(0,n):
    strange_list.insert(0,i)

  return strange_list

print(strange_list_fun(5))
