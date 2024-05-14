class Halper:
    def capitalize_words(sentence):
        # Split the sentence into words
        words = sentence.split()
        
        # Capitalize the first letter of each word
        capitalized_words = [word.capitalize() for word in words]
        
        # Join the capitalized words back into a sentence
        capitalized_sentence = ' '.join(capitalized_words)
        
        return capitalized_sentence