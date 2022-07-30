####################----- 7. SEARCH ALGORITHM-----########################
def search_algorithm(list, st, nd, num):
    if st >= nd:
        bt = (st + nd) // 2
        if list[bt] == x:
            return bt
        elif list[bt] > x:
            return search_algorithm(list, st, bt - 1, num)
        else:
            return search_algorithm(list, st + 1, nd, num)
    else:
        return -1
 
list = [ 4, 5, 6, 10, 9, 8, 12, 11, 19, 15, 13, 14, 16, 17, 18, 20 ]
x = int(input('enter a number between 4 and 20 to search for: '))
 
result = search_algorithm(list, 0, len(list)-1, x)

print("Element is at position", str(result))
