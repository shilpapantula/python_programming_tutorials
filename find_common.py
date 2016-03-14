A=[1,1,5,5,5,6,6,6,0,0,0,9,12,12,16,12,1,5,6,0,9,16]
B=[1,3,5,3,6,6,5,1,19,11,5,6,1,1,2]

# Find common objects from both the lists
def find_common(input1, input2):
    common = {}
    list_elem = {}
    for i in input1:
        if i not in list_elem:
            list_elem[i] = 1
        else:
            list_elem[i] += 1
        
    for i in input2:
        if i in list_elem:
            common[i] = common.get(i, 0) + 1
            
    return common.keys()

print find_common(A, B)
