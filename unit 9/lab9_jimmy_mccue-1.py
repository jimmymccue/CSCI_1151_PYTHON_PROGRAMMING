'''
    Jimmy McCue 
    This program allows a user to choose a file to read and then gives a word count for
    each word in the file.
    06/24/2025
'''

from word_counter import WordCounter 

def main():
    """
    Main function that handles user interaction:
    - Asks for a file name
    - Processes the file to count word frequency
    - Prompts the user to continue or exit
    """
    while True:
        filename = input("Enter the name of the text file to analyze: ")
        counter = WordCounter(filename)
        counter.read_file()

        if not counter.text:
            continue  # skip to next loop if file not found

        counter.clean_text()
        counts = counter.count_words()
        counter.display_counts(counts)

        again = input("Would you like to check another file? (y/n): ")
        if again.lower() != 'y':
            break


if __name__ == "__main__":
    main()