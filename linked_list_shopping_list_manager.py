class LinkedListShoppingListManagerClass:
    
    class Node:
        #use Node to hold an item and link to the next node'
        def __init__(self, data):
            self.data = data
            self.next = None
    
    def __init__(self): #creates empty linked list
        self.head = None
    
    def insert_item(self, item):
        #Add an item to the start of the linked list
        new_node = self.Node(item)
        new_node.next = self.head
        self.head = new_node
    
    def print_items(self):
        #Print all items in the linked list
        print("[", end=" ")
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print("]")
    
    def delete_item(self, item):
        #this will remove the first matching item from the linked list
        current = self.head
        previous = None
        while current and current.data != item:
            previous = current
            current = current.next
        if current:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
    
    def get_last_item(self):
        #Return the last item in the linked list
        if not self.head:
            return None
        current = self.head
        while current.next:
            current = current.next
        return current.data
    
    def quick_sort_helper(self, head):
        #Sort the linked list by splitting it AROUND a pivot
        # note! f list is empty or has one item, it's already sorted
        if not head or not head.next:
            return head
            
        # Use first node as pivot
        pivot = head
        pivot_data = pivot.data
        
        # Create lists for items smaller and larger than pivot
        smaller = None
        larger = None
        smaller_tail = None
        larger_tail = None
        
        # Split list into smaller and larger parts
        current = head.next
        while current:
            next_node = current.next
            current.next = None
            if current.data < pivot_data:
                if not smaller:
                    smaller = current
                    smaller_tail = current
                else:
                    smaller_tail.next = current
                    smaller_tail = current
            else:
                if not larger:
                    larger = current
                    larger_tail = current
                else:
                    larger_tail.next = current
                    larger_tail = current
            current = next_node
        
        # Sort the smaller and larger parts
        sorted_smaller = self.quick_sort_helper(smaller)
        sorted_larger = self.quick_sort_helper(larger)
        
        # Connect sorted smaller, pivot, and sorted larger
        if sorted_smaller:
            current = sorted_smaller
            while current.next:
                current = current.next
            current.next = pivot
        else:
            sorted_smaller = pivot
            
        pivot.next = sorted_larger
        
        return sorted_smaller
    
    def quick_sort(self):
        self.head = self.quick_sort_helper(self.head)
    
    def selection_sort(self):
        if not self.head:
            return
            
        current = self.head
        while current:
            min_node = current
            runner = current.next
            while runner:
                if runner.data < min_node.data:
                    min_node = runner
                runner = runner.next
            if min_node != current:
                current.data, min_node.data = min_node.data, current.data
            current = current.next