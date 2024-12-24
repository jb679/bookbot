from collections import Counter

# Function to count the number of words in the text
def count_words(text):
    words = text.split()  # Split the text by whitespace into a list of words
    return len(words)  # Return the number of words in the list

# Function to count the frequency of each character in the text
def count_characters(text):
    text_lower = text.lower()  # Convert all characters to lowercase
    character_counts = Counter(text_lower)  # Count each character using Counter
    return character_counts

# Function to generate a report from word and character data
def generate_report(word_count, character_count):
    report = []

    # Add word count to report
    report.append(f"Word Count: {word_count}")
    
    # Add character frequency data to report
    report.append("\nCharacter Frequency (Case Insensitive):")
    for char, count in sorted(character_count.items()):
        # Only show alphabetic characters and space (optional)
        if char.isalpha() or char == ' ':
            report.append(f"{char}: {count}")

    # Join the report lines into a single string with line breaks
    return "\n".join(report)

# Main function to execute the program
def main():
    # Open the frankenstein.txt file in read mode
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()  # Read the file content into a string
        print("File contents loaded.")  # Confirm the file is loaded

    # Call the count_words function and store the result
    word_count = count_words(file_contents)

    # Call the count_characters function and store the result
    character_count = count_characters(file_contents)

    # Generate the report
    report = generate_report(word_count, character_count)

    # Print the report to the console
    print("\n--- Frankenstein Book Report ---")
    print(report)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
