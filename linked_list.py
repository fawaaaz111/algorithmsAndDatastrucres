class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class linkedList:
    """
    singly linked list
    """
    def __init__(self):
        self.head = None


    def is_empty(self):
        """
        check if linkedlist is empty or not
        """
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    

    def add(self, data):
        """
        Adds new node containing data at the head of the linkedlist
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    
    def insert(self, data, index):
        """
        Insert a new node at certain index position
        Insetion takes O(n) time, however finding the node at
        insertion point takes O(n) time

        Takes overall O(n) time
        """
        if index == 0:
            self.add(data)
        else:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            preNode = current
            nextNOde = current.next_node

            preNode.next_node = new
            new.next_node = nextNOde

    
    def search(self, key):
        """
        Search for the first node containting data equal to key
        Return the node or 'None' if not found

        Takes O(n) time
        """

        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
            
        return None
    
    def delete(self, index):
        """
        Delete a node at specific index if index is valid
        Returns the deleted node

        Takes O(n) time
        """
        position = index
        current = self.head


        if position >= self.size():
            return 'not available'
        
        elif position == 0:
            nextNode = current.next_node
            current.next_node = None
            self.head = nextNode

        else:
            while position > 1:
                current = current.next_node
                position -= 1

            nextNode = current.next_node.next_node
            temp = current.next_node
            current.next_node = None
            current.next_node = nextNode

        return temp

    def remove(self, key):
        """
        Removes data that containing data matches the key
        Returns the node or None if the key doesn't exist

        Takes O(n) time
        """
        current =  self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def __repr__(self):
        """
        Returns a string representation of a linkedlist
        Takes O(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node

        return '->'.join(nodes)
    