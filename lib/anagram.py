class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted (self.word)
    
    def match(self, character_list):
        return[
            character for character in character_list
            if character.lower() != self.word and sorted(character.lower()) == self.sorted_word
        ]

















