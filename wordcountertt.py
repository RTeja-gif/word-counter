import re

def count_words(text):
    """
    Count the number of words in the given text.

    Args:
        text (str): The input text to be processed.

    Returns:
        int: The number of words in the text.
    """
    # Remove punctuation and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()

    # Split the text into words
    words = cleaned_text.split()

    # Return the count of words
    return len(words)

def get_user_input():
    """
    Prompt the user to enter a sentence or paragraph.

    Returns:
        str: The user input text.
    """
    while True:
        user_input = input("Enter a sentence or paragraph (or 'q' to quit): ")

        # Check if the user wants to quit
        if user_input.lower() == 'q':
            print("Goodbye!")
            return None

        # Proceed if the input is not empty
        if user_input.strip():
            return user_input

        # Handle empty input
        print("Error: Input cannot be empty. Please try again.")

def main():
    """
    The main function that runs the word counting program.
    """
    print("Welcome to the Word Counter!")

    while True:
        # Get user input
        user_input = get_user_input()

        # Exit the program if the user chooses to quit
        if user_input is None:
            break

        # Count the words
        word_count = count_words(user_input)

        # Display the word count
        print(f"The number of words in your input is: {word_count}")
        print()  # Print a blank line for readability

if __name__ == "__main__":
    main()