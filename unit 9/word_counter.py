from collections import Counter
import string

class WordCounter:
    """
    A class to read a text file, clean its contents, and count the occurrences of each word.
    """

    def __init__(self, filename):
        """
        Initialize the WordCounter with a given filename.

        :param filename: Name of the text file to be processed.
        """
        self.filename = filename
        self.text = ""

    def read_file(self):
        """
        Reads the contents of the file and stores it in the 'text' attribute.
        Prints an error if the file is not found.
        """
        try:
            with open(self.filename, 'r') as file:
                self.text = file.read()
            if not self.text.strip():  # checks if text is empty or only whitespace
                print("File contains no text.")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            self.text = ""

    def clean_text(self):
        """
        Cleans the text by removing punctuation and converting all characters to lowercase.
        """
        self.text = self.text.translate(str.maketrans('', '', string.punctuation)).lower()

    def count_words(self):
        """
        Splits the cleaned text into words and counts their occurrences.

        :return: A Counter object with words as keys and their counts as values.
        """
        words = self.text.split()
        return Counter(words)

    def display_counts(self, counts):
        """
        Displays the word counts sorted alphabetically.

        :param counts: A Counter object containing word-frequency pairs.
        """
        for word, count in sorted(counts.items()):
            print(f"{word:<15}{count}")