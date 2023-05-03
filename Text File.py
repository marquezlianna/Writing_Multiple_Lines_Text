# Marquez, Lianna L.
# Assignment4_Problem3

# Write a method in python to write multiple line of text contents into a text file myfile.txt.
# See sample output:
        #Enter line: Beautiful is better than ugly.
        #Are there more lines y/n? y
        #Enter line: Explicit is better than implicit.
        #Are there more lines y/n? y
        #Enter line: Simple is better than complex. 
        #Are there more lines y/n? y

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

