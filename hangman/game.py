from .exceptions import *

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):
    import random 
    if list_of_words == []:
        raise InvalidListOfWordsException()
    random_word = random.choice(list_of_words)
    
    return random_word


def _mask_word(word):
    masked_word = ""
    for letter in word: 
        masked_word += "*"
    if word == "":
        raise InvalidWordException()
    return masked_word
        


        
def _uncover_word(answer_word, masked_word, character):
    
    answer_word = list(answer_word)
        #  ['p','y','t','h','o','n']
    masked_word = list(masked_word)
        #  ['*','*','*','*','*','*'] 
    for value, item in enumerate(answer_word):
        if character.lower() == item.lower():
                masked_word[value] = character.lower()
    masked_word = "".join(masked_word)
#find index where character is in answer word, 
#replace the asterick with the same index with that character
    if not answer_word or not masked_word or not character:
        raise InvalidWordException()
    if len(character) > 1:
        raise InvalidGuessedLetterException
    if len(answer_word) != len(masked_word):
        raise InvalidWordException
    return masked_word
                
 
#find the index(indeces) of the character in the answer word and at the
#same index of the masked_word put in that letter


def guess_letter(game, letter):
    
    letter = letter.lower()
    previous_masked = game['masked_word']
    new_masked = _uncover_word(game['answer_word'], previous_masked, letter)
    
    if previous_masked == new_masked:
        #this is a miss
        game['remaining_misses'] -= 1
    else: 
        game['masked_word'] = new_masked
    game['previous_guesses'].append(letter)
    
    if is_game_won(game):
        raise GameWonException()
    
    if is_game_lost(game):
        raise GameLostException()
        
    
def is_game_won(game):
    return game['answer_word'].lower() == game['masked_word']
    
    
def is_game_lost(game):
    return game['remaining_misses'] <= 0
  
        
    #check if letter is in answer word 
    #append guess to previous guesses
    #update our masked work


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
