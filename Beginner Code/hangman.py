import random

word_list = ['aardvark', 'baboon', 'camel']
total_word_count = int(len(word_list))

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ""

for i in range(int(len(chosen_word))):
    placeholder += "_"

print(placeholder)

game_over = False

while not game_over:
    guessed_letter = input('guess a letter\n')

    display = ""

    for idx in range(int(len(chosen_word))):
        if guessed_letter == chosen_word[idx]:
            display += guessed_letter
        else:
            display += "_"
        
    print(display)
