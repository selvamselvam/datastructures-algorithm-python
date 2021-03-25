class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

def reverse(head):

    currentnode=head;
    privious = None
    nextnode = None

    while currentnode:

        nextnode = currentnode.nextnode

        currentnode.nextnode = privious

        privious=currentnode
        currentnode=nextnode

    return privious

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d


print( a.nextnode.value)
print (b.nextnode.value)
print (c.nextnode.value)



reverse(a)


print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)