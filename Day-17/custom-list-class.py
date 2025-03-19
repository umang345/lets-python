'''
Custom Dynamic Array

In this exercise, you will implement a custom dynamic array class, similar to Python’s built-in list. Your task is to create a class CustomList that supports dynamic resizing and several list operations.

Class Definition

Class Name: CustomList

Attributes:

capacity: The current capacity of the internal array.

size: The number of elements currently stored in the array.

array: The internal storage for the list elements.

Methods:

__init__(self): Initializes an empty CustomList with an initial capacity of 1.

append(self, item): Adds an item to the end of the list. If the list is full, it should resize the internal storage to accommodate more elements.

__len__(self): Returns the number of elements in the list.

__str__(self): Returns a string representation of the list, formatted like a Python list.

pop(self): Removes and returns the last item in the list. If the list is empty, it should return an appropriate error message.

__getitem__(self, index): Retrieves the item at the specified index. If the index is out of bounds, it should return an error message.

clear(self): Clears all items from the list.

insert(self, position, element): Inserts an element at the specified position. If the list is full, it should resize the internal storage.

remove(self, element): Removes the first occurrence of the specified element from the list. If the element is not found, it should return an error message.
'''

import ctypes

class CustomList:
    def __init__(self):
        initialCapacity = 1
        self.capacity = initialCapacity
        self.size = 0
        self.array = self.__create_array(self.capacity)

    def __create_array(self, capacity):
        # Create a new referential array with the given capacity
        return (capacity * ctypes.py_object)()

    def __resize(self, new_capacity):
        new_array = self.__create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array # Replace the old array
        self.capacity = new_capacity

    def append(self, item):
        if self.size == self.capacity:
            self.__resize(2*self.capacity)
            
        self.array[self.size] = item 
        self.size+=1 
        print(self.array)

    def __len__(self):
        return self.size 

    def __str__(self):
        
        nums = [str(self.array[index]) for index in range(self.size)]
        
        output = ", ".join(nums)
        return f"[{output}]"
        
        
    def pop(self):
        
        if self.size==0:
            return "Empty List, IndexError: pop from empty list"
            
        popped = self.array[self.size-1]
        self.size-=1 
        return popped

    def __getitem__(self, index):
        
        if index>=0 and index < self.size :
            return self.array[index]
            
        return 'Index Error: Invalid index'

    def clear(self):
        self.size = 0

    def insert(self, position, element):
        if self.size == self.capacity:
            self.__resize(2*self.capacity)
            
        if not (position>=0 and position<=self.size):
            return 'Index Error: Invalid position'
            
        for index in range(self.size, position, -1):
            self.array[index] = self.array[index-1]
            
        self.array[position] = element
        self.size+=1

    def remove(self, element):
        indexFound = -1 
        for index in range(0, self.size):
            if self.array[index] == element:
                indexFound = index 
                break 
            
        if indexFound!=-1:
            for index in range(index, self.size-1):
                self.array[index] = self.array[index+1]
            self.size-=1
        else:
            return "Element not found"
        

# Example Usage
myList = CustomList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
print(myList)  # Expected Output: [1, 2, 3, 4]
myList.insert(1, 100)
print(myList)  # Expected Output: [1, 100, 2, 3, 4]
