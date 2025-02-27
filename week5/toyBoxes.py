'''
We are given N unopenend boxed with k number of figurines in each box. The boxes cannot be opened 
and hence, the order of the figurines cannot be changed
A box cannot be rotate (otherwise figurines face the wrong way)

Each figurine is specified by its height 
For example in a given box the height of the figurine from ledt to right 4, 5, and 7. 
Note that the number of figurines in each box may vary

We would like to organize all the toy boxes s.t they are arranged in non decreasing order  of figurine heights 
from left to right. Hence, write a program to determine if we can have such an arrangement or not. 

Top down design
some task will not require much code
other tasks will require more from us 
'''
# n boxes
# k figurines
# either increasing or equal

def box(n):
    sublst = []
    for i in range(n):
        fig = input().split()
        #fig.pop(0)
        for i in range(len(fig)):
            fig[i] = int(fig[i])
        sublst.append(fig[1:])
    return sublst

def allBoxesOk(kst_boxes):
    for box in kst_boxes:
        if box != sorted(box):
            return False
    return True

def boxIntervals(lst_boxes):
    intervals = []
    for box in lst_boxes:
        intervals.append([box[0], box[-1]])
    return intervals

def allIntervalsOk(lst_intervals):
    prev_max_height = lst_intervals[0][1]

    for box in range(1, len(lst_intervals)):
        curr_min_height = lst_intervals[box][0]
        if curr_min_height < prev_max_height:
            return False
        prev_max_height = lst_intervals[box][1]
    return True



n = int(input())
boxes = box(n)

if not allBoxesOk(boxes):
    print("No")
else:
    intervals = boxIntervals(boxes)
    intervals.sort()
    if allIntervalsOk(intervals):
        print("YES")
    else:
        print("NO")

