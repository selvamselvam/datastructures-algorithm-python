def find_missing(a1,a2):


    a1= sorted(a1)
    a2 = sorted(a2)

    l = len(a1) > len(a2) ? len(a1) : len(a2)

    print(a1)
    print(a2)

a1=[1,2,3,4,5,6,7]
a2=[3,7,2,1,4,6]

find_missing(a1,a2)