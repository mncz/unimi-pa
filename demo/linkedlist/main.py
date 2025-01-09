from linkedlist import LinkedList

def main():
    # l1 = LinkedList([1,2,3])
    # l2 = LinkedList(100)
    l3 = LinkedList()
    
    l3.append([3, 12, 23, 42, 99, 42])
    l3.remove(42)
    l3[0] = 8
    del l3[1]
    l3.insert(-1, 100)
    print(l3)
    print(repr(l3))

if __name__ == '__main__':
    main()