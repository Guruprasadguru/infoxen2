
l2= [1, [2, 3, [4, 5, 6], [7,[ 8, 9, [10, 11], 12] ]]]
output=[]
def flatedlist(l2):
    for i in l2:
        if type(i)==list:
            flatedlist(i)
        else:
            output.append(i)

flatedlist(l2)
print(output)