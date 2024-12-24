def main():
    # Open the frankenstein.txt file in read mode
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()  # Read the file content into a string
        print(file_contents)  # Print the file content to the console

if __name__ == "__main__":
    main()  # Call the main function to execute the program
