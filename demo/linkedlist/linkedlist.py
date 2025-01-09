class Node:
    """Classe che rappresenta un nodo in una lista collegata."""

    def __init__(self, value):
        """
        Inizializza un nodo con un valore e un puntatore al nodo successivo.

        Args:
            value: Il valore del nodo.
        """
        self.value = value
        self.next = None
    
    def __str__(self):
        """Restituisce una rappresentazione stringa del nodo."""
        return f'Node({self.value})'
    
    def __repr__(self):
        """Restituisce una rappresentazione dettagliata del nodo."""
        return f'Node(value={self.value}, next={self.next})'


class LinkedList:
    """Classe che rappresenta una lista collegata."""

    def __init__(self, elem=None):
        """
        Inizializza una lista collegata.

        Args:
            elem: Un singolo elemento o una lista di elementi per 
            inizializzare la lista collegata.
        """
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
        """Restituisce la dimensione della lista collegata."""
        return self.size
    
    def __getitem__(self, index):
        """
        Restituisce il valore del nodo all'indice specificato.

        Args:
            index: L'indice del nodo.

        Returns:
            Il valore del nodo all'indice specificato.
        """
        index = self.size + index if index < 0 else index
        current = self.head
        
        self.__in_range(index)

        for _ in range(index):
            current = current.next
        
        return current.value
    
    def __setitem__(self, index, value):
        """
        Imposta il valore del nodo all'indice specificato.

        Args:
            index: L'indice del nodo.
            value: Il nuovo valore del nodo.
        """
        index = self.size + index if index < 0 else index
        current = self.head
        
        self.__in_range(index)

        for _ in range(index):
            current = current.next
        
        current.value = value

    def __delitem__(self, index):
        """
        Elimina il nodo all'indice specificato.

        Args:
            index: L'indice del nodo da eliminare.
        """
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
        """
        Verifica se un valore è presente nella lista collegata.

        Args:
            value: Il valore da cercare.

        Returns:
            True se il valore è presente, False altrimenti.
        """
        if self.head is None:
            return False
        
        current = self.head

        for _ in range(self.size):
            if current.value == value:
                return True
            
            current = current.next
        
        return False
    
    def __str__(self):
        """Restituisce una rappresentazione stringa della lista collegata."""
        r = ''
        current = self.head

        for i in range(self.size):
            r += f'{current.value}'

            if i < self.size - 1:
                r += ' -> '
            
            current = current.next

        return f'LinkedList({r})'
    
    def __repr__(self):
        """Restituisce una rappresentazione dettagliata della lista collegata."""
        return f'LinkedList(head={self.head}, size={self.size})'
    
    def append(self, value):
        """
        Aggiunge un valore alla fine della lista collegata.

        Args:
            value: Il valore da aggiungere.
        """
        if self.head:
            current = self.head

            while current.next is not None:
                current = current.next
            
            current.next = Node(value)
            self.size += 1
        else:
            self.__init__(value)

    def insert(self, index, value):
        """
        Inserisce un valore all'indice specificato.

        Args:
            index: L'indice in cui inserire il valore.
            value: Il valore da inserire.
        """
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
        """
        Rimuove il primo nodo con il valore specificato.

        Args:
            value: Il valore del nodo da rimuovere.
        """
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
    
    def pop(self):
        self.__delitem__(-1)

    def __in_range(self, index):
        """
        Verifica se l'indice è nel range valido.

        Args:
            index: L'indice da verificare.

        Raises:
            IndexError: Se l'indice è fuori dal range.
        """
        if index < 0 or index > self.size:
            raise IndexError('Indice fuori dal range!')