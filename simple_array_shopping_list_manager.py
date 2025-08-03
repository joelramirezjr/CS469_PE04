class SimpleArrayShoppingListManagerClass:
    
    def __init__(self):
        #Create an empty list for shopping items
        self.items = []
    
    def insert_item(self, item):
        #Add an item to the start of the list
        self.items.insert(0, item)
    
    def print_items(self):
            # Print items with single quoutes and seperate with comma
            print("[", end=" ")
            for item in self.items:
                print("'" + item + "',", end=" ")
            print("]")
    
    def delete_item(self, item):
        # This will remove the first matching item from the list
        if item in self.items:
            self.items.remove(item)
    
    def get_last_item(self):
        #Return the last item in the list
        return self.items[-1] if self.items else None
    
    def quicksort(self, left=0, right=None):
        #Sort the list using quicksort algorithm
        if right is None:
            right = len(self.items) - 1
        
        if left < right:
            pivot = self.partition(left, right)
            self.quicksort(left, pivot - 1)
            self.quicksort(pivot + 1, right)
    
    def partition(self, left, right):
        #Place pivot at correct position and arrange smaller/larger elements
        pivot = left
        index = pivot + 1
        i = index
        while i <= right:
            if self.items[i] < self.items[pivot]:
                self.swap(i, index)
                index += 1
            i += 1
        self.swap(pivot, index - 1)
        return index - 1
    
    def swap(self, i, j):
        #Swap two elements in the list
        self.items[i], self.items[j] = self.items[j], self.items[i]
    
    def quick_sort(self):
        #Sort the entire list using quicksort
        if self.items:
            self.quicksort()
    