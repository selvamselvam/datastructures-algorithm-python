def linear_search(array, x):
    for i in range(len(array)):
        if array[i] == x:
            print("Find the value in {} position".format(int(i)+1))
            return
    print("not found")


array = [1, 2, 3, 7, 8]
linear_search(array, 7)
