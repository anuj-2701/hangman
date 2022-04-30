
import random
from hangman_art import stages,logo

print(logo)
end_of_game = False

from hangman_words import word_list
chosen_word = random.choice(word_list)

lives=6

hidden_word_list = []
for letter in chosen_word:
    hidden_word_list += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in hidden_word_list:
        print(f"you have already guessed {guess}")

    k=0
    for letter in chosen_word:
        if letter == guess:
            hidden_word_list[k] = guess
        k+=1 

    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in the word. you lose a life")
        lives-=1
        if lives==0:
           end_of_game = True
  
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(hidden_word_list)}")

    if "_" not in hidden_word_list:
        end_of_game = True
        print("You win.")


    print(stages[lives])
    if lives==0:
      print("you lose")
      print(f"the word was {chosen_word}")