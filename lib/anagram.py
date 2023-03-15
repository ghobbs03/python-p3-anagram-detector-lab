# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word
    
    def match(self, words):
        anagram = self.word
        unique_anagram_letters = set([*anagram])
        matched_words = []

        letter_counts = dict()
        for letter in unique_anagram_letters:
            letter_counts[letter] = anagram.count(letter)

    
        for word in words:
            matched_letters = dict()
            unique_word_letters = set([*word])
            for letter in unique_word_letters:
                count = word.count(letter)
                if (letter in letter_counts and letter_counts[letter] == count):
                    matched_letters[letter] = count
            
            if (len(matched_letters) == len(letter_counts)):
                matched_words.append(word)

        return matched_words

      
        

       
