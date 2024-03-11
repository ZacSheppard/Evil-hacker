#fortnite>>>>>>>>

arr = [7, 4, 18, 19, 5, 348, 6, 1400, 666, 9, 42]

def LinearSearch(arr):
    found = False
    i = 0
    search_term = int(input())
    while found == False and i < len(arr):
        if arr[i] == search_term:
            found = True
        i += 1



