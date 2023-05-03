# Writing_Multiple_Lines_Text


# Python Method to Write Multiple Lines of Text to a File

This Python code demonstrates how to write multiple lines of text content into a file named `myfile.txt`.

## Usage
The code prompts the user to enter lines of text until the user enters "n" when asked whether there are more lines to input. Once the user finishes entering text, the code writes the input lines to the `myfile.txt` file. 

## Sample Output
```
Enter line: Beautiful is better than ugly.
Are there more lines y/n? y
Enter line: Explicit is better than implicit.
Are there more lines y/n? y
Enter line: Simple is better than complex. 
Are there more lines y/n? n
```

## Code Explanation

```python
def write():
    # open file named my_file.txt(write)
    my_file = open("my_file.txt", "w")
    # while loop with true
    while True:
        # Enter line
        line = input("Enter line: ")
        # Write line
        my_file.write(line.strip())
        # choose if there are more lines
        choice = input("Are there more line (Y/N): ")
        if choice == "N":
            break    

# === start === 
write()
```

- First, the code creates a new file named `my_file.txt` in write mode using the `open()` function.
- The `while` loop prompts the user to enter a line of text using the `input()` function and writes the line to the `my_file.txt` file using the `write()` method of the file object. 
- The `strip()` method is used to remove any leading or trailing white space from the input line.
- The `choice` variable stores the user's response to the question "Are there more lines y/n?". If the user enters 'n', the `break` statement is executed, and the `while` loop is exited.
- Finally, the `with` statement closes the file automatically.
