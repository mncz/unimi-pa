class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f'Node({self.value})'
    
    def __repr__(self):
        return f'Node(value={self.value}, next={self.next})'

class LinkedList:
    def __init__(self, elem=None):
        if elem:
            if not isinstance(elem, list):
                self.head = Node(elem)
                self.size = 1
            elif isinstance(elem, list):
                self.head = Node(elem[0])
                self.size = 1
                current = self.head

                for i in range(1, len(elem)):
                    node = Node(elem[i])
                    current.next = node
                    current = node
                    self.size += 1
            else:
                raise Exception('Impossibile inizializzare un LinkedList!')
        else:
            self.head = None
            self.size = 0
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        index = self.size + index if index < 0 else index
        current = self.head
        
        self.__in_range(index)

        for _ in range(index):
            current = current.next
        
        return current.value
    
    def __setitem__(self, index, value):
        index = self.size + index if index < 0 else index
        current = self.head
        
        self.__in_range(index)

        for _ in range(index):
            current = current.next
        
        current.value = value

    def __delitem__(self, index):
        index = self.size + index if index < 0 else index
        current = self.head

        self.__in_range(index)

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head

            for _ in range(index - 1):
                current = current.next

            current.next = current.next.next
        
        self.size -= 1
    
    def __contains__(self, value):
        if self.head is None:
            return False
        
        current = self.head

        for _ in range(self.size):
            if current.value == value:
                return True
            
            current = current.next
        
        return False
    
    def __str__(self):
        r = ''
        current = self.head

        for i in range(self.size):
            r += f'{current.value}'

            if i < self.size - 1:
                r += ' -> '
            
            current = current.next

        return f'LinkedList({r})'
    
    def __repr__(self):
        return f'LinkedList(head={self.head}, size={self.size})'
    
    def append(self, value):
        if self.head:
            current = self.head

            while current.next is not None:
                current = current.next
            
            current.next = Node(value)
            self.size += 1
        else:
            self.__init__(value)

    def insert(self, index, value):
        index = self.size + index + 1 if index < 0 else index

        self.__in_range(index)

        if index == 0:
            n = self.head
            self.head = Node(value)
            self.head.next = n
        else:
            current = self.head

            for _ in range(index - 1):
                current = current.next
            
            n = current.next
            current.next = Node(value)
            current.next.next = n

        self.size += 1
    
    def remove(self, value):
        if self.head:
            current = self.head.next
            prev = self.head

            while current is not None:
                if current.value == value:
                    prev.next = current.next
                    current = prev.next
                    self.size -= 1
                else:
                    prev = current
                    current = current.next

    def __in_range(self, index):
        if index < 0 or index > self.size:
            raise IndexError('Indice fuori dal range!')
