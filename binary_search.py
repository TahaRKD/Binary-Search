import random
import time
def binarySearch(list,target,low=None,high=None):
    if low==None:
         low=0
    if high==None:
        high=len(list)-1
    #as we are incrementing high-1 and low+1
    #we will reach a point where low>high, in that case target is not there in the list
    if low>high:
        return -1   

    midpoint=(low+high)//2
    if list[midpoint]==target:
        return midpoint 
    elif  target<list[midpoint]:
        new_high=midpoint-1
        return binarySearch(list,target,low,new_high)
    elif  target>list[midpoint]:
            new_low=midpoint+1
            return binarySearch(list,target,new_low,high)
length=10000
sorted_list=set()
while len(sorted_list)<length:
     sorted_list.add(random.randint(-3*length,3*length))
sorted_list=sorted(sorted_list)
target_list=[random.randint(-3*length,3*length) for _ in range(length)]

start=time.time()
for target in target_list:
     binarySearch(sorted_list,target)
end=time.time()
print(f"it took {end-start} second to search {length} items in sorted list")