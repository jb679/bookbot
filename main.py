from collections import Counter

# Function to count the number of words in the text
def count_words(text):
    # Split the text into words and return the number of words
    words = text.split()  # Split the text by whitespace into a list of words
    return len(words)  # Return the number of words in the list

# Function to count the frequency of each character in the text
def count_characters(text):
    # Convert the text to lowercase and count the occurrences of each character
    text_lower = text.lower()  # Convert all characters to lowercase
    character_counts = Counter(text_lower)  # Count each character using Counter
    return character_counts

# Main function to execute the program
def main():
    # Open the frankenstein.txt file in read mode
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()  # Read the file content into a string
        print("File contents loaded.")  # Confirm the file is loaded

    # Call the count_words function and store the result
    word_count = count_words(file_contents)
    print(f"The book contains {word_count} words!")  # Print the word count

    # Call the count_characters function and store the result
    character_count = count_characters(file_contents)

    # Print the character count
    print("\nCharacter counts:")
    for char, count in character_count.items():
        # Print each character and its count
        print(f"{char}: {count}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
