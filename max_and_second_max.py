# Find max and second max from the input lists given
A=[1,1,5,5,5,6,6,6,0,0,0,9,12,12,16,12,1,5,6,0,9,16]
B=[1,3,5,3,6,6,5,1,19,11,5,6,1,1,2]
 
 
#Maximum and Second Maximum
 
 
def second_max(input):
    max = None
    sec_max = None
   
    for i in input:
        if i > max:
            max = i
        elif i <= max and i > sec_max:
            sec_max = i
    return max, sec_max
 
print second_max(B)
