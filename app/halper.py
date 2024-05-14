class Halper:
    """
    A helper class providing string manipulation functions.
    """

    def capitalize_words(sentence):
        """
        Capitalize the first letter of each word in a sentence.

        Args:
            sentence (str): The input sentence.

        Returns:
            str: The sentence with capitalized words.
        """
        # Split the sentence into words
        words = sentence.split()
        
        # Capitalize the first letter of each word
        capitalized_words = [word.capitalize() for word in words]
        
        # Join the capitalized words back into a sentence
        capitalized_sentence = ' '.join(capitalized_words)
        
        return capitalized_sentence

    def capitalize_first_letter(text):
        """
        Capitalize the first letter of a given text.

        Args:
            text (str): The input text.

        Returns:
            str: The text with the first letter capitalized.
        """
        # Convert all letters to lowercase
        text = text.lower()
        # Capitalize the first letter of the first word
        text = text.capitalize()
        return text