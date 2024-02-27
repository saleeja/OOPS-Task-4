"""Create a class for creating and writing data to a text file. The class must have __enter__ and __exit__ 
defined.
__enter__ must use the built in `open` to open the file and set the file pointer to self.
__exit__ must close the file pointer on exit.
If the user entered text contains the word 'bug' then __exit__ must delete the file on exiting.
Or if any exception has occurred, then also __exit__ must delete the file.(remember to close file 
before deleting)
Use a `with` block to execute the logic"""


import os

class FileWriter:
    def __init__(self, filename, mode="w"): # Initialize FileWriter instance with a filename, mode, file object, and text_written attribute
        self.filename = filename
        self.file = None
        self.mode = mode
        self.text_written = None  # Initialize the attribute to store the written text

    def __enter__(self):  # Implement the context manager's __enter__ method to open the file
        self.file = open(self.filename, self.mode)
        return self # Return the FileWriter instance for use in the 'with' statement

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            try:
                # Check if the entered text contains the word 'bug'
                contain_bug = 'bug' in self.text_written
            finally:
                self.file.close()

                # Check if an exception occurred or if the entered text contains the word 'bug'
                if exc_type is not None or contain_bug:
                    print("An exception occurred or the entered text contains the word 'bug'.\nDeleting the file................")
                    os.remove(self.filename)
                    print("File deleted.")
                else:
                    print("Text has been written successfully.")

    def write(self, data):
        if self.file:
            self.file.write(str(data))
            self.text_written = data  # Store the written text

    def writelines(self, lines):
        if self.file:
            self.file.writelines(lines)
            self.text_written = ''.join(lines)  # Store the written text

try:
    with FileWriter("Example.txt") as writer:
        text_to_write = input("Enter the text to write to the file: ")
        writer.write(text_to_write)
except Exception as e:
    print(f"An exception occurred: {e}")


# output
"""
Enter the text to write to the file: hello world!
Text has been written successfully."""

#if entered bug word
"""
Enter the text to write to the file: bug
An exception occurred or the entered text contains the word 'bug'.
Deleting the file................
File deleted."""
