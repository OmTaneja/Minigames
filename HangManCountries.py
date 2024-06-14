import random

word_list = [
    "afghanistan", "albania", "algeria", "andorra", "angola", "antiguaandbarbuda", "argentina", "armenia", "australia", "austria",
    "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize", "benin", "bhutan", "bolivia",
    "bosniaandherzegovina", "botswana", "brazil", "brunei", "bulgaria", "burkinafaso", "burundi", "cambodia", "cameroon", "canada",
    "capeverde", "centralafricanrepublic", "chad", "chile", "china", "colombia", "comoros", "congo", "costarica", "croatia", "cuba",
    "cyprus", "czechrepublic", "denmark", "djibouti", "dominica", "dominicanrepublic", "ecuador", "egypt", "elsalvador", "equatorialguinea",
    "eritrea", "estonia", "eswatini", "ethiopia", "fiji", "finland", "france", "gabon", "gambia", "georgia", "germany", "ghana", "greece",
    "grenada", "guatemala", "guinea", "guineabissau", "guyana", "haiti", "honduras", "hungary", "iceland", "india", "indonesia", "iran",
    "iraq", "ireland", "israel", "italy", "jamaica", "japan", "jordan", "kazakhstan", "kenya", "kiribati", "northkorea", "southkorea",
    "kosovo", "kuwait", "kyrgyzstan", "laos", "latvia", "lebanon", "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg",
    "madagascar", "malawi", "malaysia", "maldives", "mali", "malta", "marshallislands", "mauritania", "mauritius", "mexico", "micronesia",
    "moldova", "monaco", "mongolia", "montenegro", "morocco", "mozambique", "myanmar", "namibia", "nauru", "nepal", "netherlands",
    "newzealand", "nicaragua", "niger", "nigeria", "northmacedonia", "norway", "oman", "pakistan", "palau", "palestine", "panama", "papuanewguinea",
    "paraguay", "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda", "saintkittsandnevis", "saintlucia",
    "saintvincentandthegrenadines", "samoa", "sanmarino", "saotomeandprincipe", "saudiarabia", "senegal", "serbia", "seychelles", "sierraleone",
    "singapore", "slovakia", "slovenia", "solomonislands", "somalia", "southafrica", "southsudan", "spain", "srilanka", "sudan", "suriname",
    "sweden", "switzerland", "syria", "taiwan", "tajikistan", "tanzania", "thailand", "timorleste", "togo", "tonga", "trinidadandtobago",
    "tunisia", "turkey", "turkmenistan", "tuvalu", "uganda", "ukraine", "uae", "uk", "usa", "uruguay", "uzbekistan", "vanuatu", "vaticancity",
    "venezuela", "vietnam", "yemen", "zambia", "zimbabwe"
]
word = random.choice(word_list)

underscores = '_' * len(word)
print(underscores)

list1 = []
for i in underscores:
    list1.append(i)


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

max_no_of_incorrect_guesses = len(HANGMANPICS)
incorrect_guesses_uptil_now = 0
lol = 0
str1 = ""

while max_no_of_incorrect_guesses > 0:
    guess = str.lower(input())


    def valid_string(guess):
        for i in range(65, 91):
            if guess == chr(i).lower():
                return True
            else:
                return False


    valid = valid_string(guess)
    if len(guess) != 1 and valid == False:
        #print("Error 404 ('_')")
        break

    while True:
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    list1[i] = guess
            print(str1.join(list1))
        else:
            max_no_of_incorrect_guesses -= 1
            print(HANGMANPICS[incorrect_guesses_uptil_now])
            incorrect_guesses_uptil_now +=1
            print(str1.join(list1))
        break
    lol += 1

print("PRESS ENTER TO CONTINUE....")
if max_no_of_incorrect_guesses == 0:
    print('GAME OVER....TRY AGAIN :(')
else:
    print("CONGRATULATIONS! YOU WON...  :)")
