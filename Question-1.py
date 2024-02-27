"""Create a class called Add , it must have __call__ defined. Create an object of that class.
When the object is directly called with a list of integers - like - obj([1,2,3,4,5]) It must return the sum 
of elements in the list.
Eg:
add = Add()
total = add([1,2,3,4,5,6])"""

class Add:
    def __init__(self):
        self.history = []  # Initialize the Add class with an empty history list to store calculations.

    def __call__(self, numbers): # The __call__ method allows instances of the class to be called as a function
        # Check if the input is a list of integers
        if not isinstance(numbers, list):
            raise TypeError("Input must be a list of integers")
        
        if not all(isinstance(num, int) for num in numbers):
            raise TypeError("List must contain only integers")

        result = sum(numbers) # Calculate the sum of list
        self.history.append({"input": numbers, "result": result})
        return result

    def get_history(self):
        return self.history

# Create an object of the Add class
add_object = Add()

# Call the object with a list of integers
result1 = add_object([1, 2, 3, 4, 5])

result2 = add_object([10, 20, 30, 40])

history = add_object.get_history()

print(f"Sum of the elements in the first list: {result1}")
print(f"Sum of the elements in the second list: {result2}")
print("History of calculations:")
for entry in history:
    print(f"Input: {entry['input']}, Result: {entry['result']}")


