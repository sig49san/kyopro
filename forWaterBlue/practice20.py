import bisect

N = int(input())
Alist = sorted(list(map(int, input().split())))
Blist = sorted(list(map(int, input().split())))
Clist = sorted(list(map(int, input().split())))
'''
def binary_search1(num_list, target):
    ans_counter = 0
    if target <= num_list[0]:
        return 0
    
    if num_list[-1] < target:
        return(len(num_list))
    
    for i in range(10000000):

        middle = num_list[len(num_list) // 2]
        left = num_list[:len(num_list) // 2]
        right = num_list[len(num_list) // 2:]

        if target >= left[-1] and right[0] > target:
            ans_counter += len(left)
            return ans_counter

        elif target < left[-1]:
            num_list = left
    
        elif right[0] <= target:
            ans_counter += len(left)
            num_list = right

def binary_search2(num_list, target):
    ans_counter = 0
    if target <= num_list[0]:
        return 0
    
    if num_list[-1] < target:
        return(len(num_list))
    
    for i in range(10000000):

        middle = num_list[len(num_list) // 2]
        left = num_list[:len(num_list) // 2]
        right = num_list[len(num_list) // 2:]

        if target > left[-1] and right[0] >= target:
            ans_counter += len(left)
            return ans_counter

        elif target <= left[-1]:
            num_list = left
    
        elif right[0] < target:
            ans_counter += len(left)
            num_list = right
'''
ans = 0

for B in Blist:
    Aindex = bisect.bisect_left(Alist, B)
    Cindex = bisect.bisect_right(CList, B)

    print(B, Aindex, Cindex)

'''
for B in Blist:
    a_point = binary_search2(Alist, B)
    c_point = binary_search1(Clist, B)
    print(B,a_point, c_point, Clist.count(B))

    ans = ans + a_point * (N - c_point)

print(ans)
#for C in Clist:
'''    


