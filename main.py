def count_words(text):
    # Split the text into words and return the number of words
    words = text.split()  # Split the text by whitespace into a list of words
    return len(words)  # Return the number of words in the list

def main():
    # Open the frankenstein.txt file in read mode
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()  # Read the file content into a string
        print("File contents loaded.")  # Confirm the file is loaded

    # Call the count_words function and store the result
    word_count = count_words(file_contents)
    
    # Print the word count
    print(f"The book contains {word_count} words!")

if __name__ == "__main__":
    main()  # Call the main function to execute the program
