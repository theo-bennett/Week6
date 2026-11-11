def minimum(lst):
    a = 0
    for x in range(1, len(lst)):
        if lst[x] < lst[a]:
            a = x
    return lst[a]
print(minimum([4, 2, 7, 3])) # The output should be 2


#the error was in the 2nd to last line. the Return statement was missing "lst" which is why it was giving a 1 not a 2