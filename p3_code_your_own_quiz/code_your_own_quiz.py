import time
from sys import exit

easy_text = "President Donald Trump unloaded on the news media __1__ for using __2__ sources just hours after members of \nhis own __3__ insisted on briefing __4__ only on condition their names be __5__."

medium_text = "Barcelona coach Luis __1__ will leave the __2__ La Liga champions at the end of the __3__ when his __4__ expires, he said on __5__."

hard_text = "__1__ (14-9-11 last season for a franchise-record __2__ points) kicks off Saturday at Real Salt Lake and, unlike past seasons when __3__ Field was being renovated, will play just __4__ games on the road before opening at home __5__ 31 against Sporting Kansas City. "

easy_answer = ['Friday', 'anonymous', 'staff', 'reporters', 'concealed']

medium_answer = ['Enrique', 'Spanish', 'season', 'contract', 'Wednesday']

hard_answer = ['Toronto', '53', 'BMO', 'three', 'March']

parts_of_speech1  = ["__1__", "__2__", "__3__", "__4__", "__5__"]



def Gamesetup():  
	'''
	   Behavior: This function is to select game level and to setup number of guess.
	   Input: Takes no inputs.
	   Output: Text, Answer and number of guess.

	'''
	print "Welcome to the fill in blank quiz!\nPlease let me know how many guesses you need per game?\n"
	guess_remaining = int(raw_input()) # Number of guess

	while True:

		print "Please select a level(easy, medium, hard)!"
		print

		game_level = raw_input("")

		if game_level == "easy":
			text = easy_text
			answer = easy_answer
			print "Loading the %s level... Good luck!" % game_level
			time.sleep(1.5)
			CheckAnswerForAll(text, answer, guess_remaining)

		elif game_level == "medium":
			text = medium_text
			answer = medium_answer
			print "Loading the %s level... Good luck!" % game_level
			time.sleep(1.5)
			CheckAnswerForAll(text, answer, guess_remaining)

		elif game_level == "hard":
			text = hard_text
			answer = hard_answer
			print "Loading the %s level... Good luck!" % game_level
			time.sleep(1.5)
			CheckAnswerForAll(text, answer, guess_remaining)

		else:
			print "Sorry. I didn't catch you. Please select from easy, medium and hard!"
			



def CheckAnswer(index, text, answer, guess_remaining): 
    ''' 
       Behavior: Check answer for each blank until anwser is right or guess_remaining is zero.
       Input: Text, Answer, Guess_remaining, index of anwser list and parts of speech list
       Output: index of answer list and parts of speech list
    '''
    max_attempt = 1
    index_increment = 1
    print "What is the your answer for __%d__?" % (index + index_increment)
    user_input = raw_input("")


    while True:
				
		if user_input == answer[index]: # if the input is correct
			
			time.sleep(1)			
			print "\nGood Job!\nHere is the correct answer so far...\n"
			print text.replace(parts_of_speech1[index], answer[index]) # print text with correct answers
			return guess_remaining			

			
		elif guess_remaining > max_attempt:   # if the input is wrong
			guess_remaining = guess_remaining - max_attempt # number of guesses substact 1, and loop again

			print "Wrong. Please Try again. You have %d guesses left." % guess_remaining

			user_input = raw_input("")

		else:  
			print "You lose!"
			exit(0)


def CheckAnswerForAll(text, answer, guess_remaining,):
        
    ''' 
        Behavior: Call CheckAnswer function 5 times and print Good Job!
        Input: Text, Answer, guess_remaining
        Output: exit the game   
    '''
    index = 0
    print "Here is the text. Have fun!"
    print text
	
    for pos in range(5):  

	guess_remaining = CheckAnswer(index, text, answer, guess_remaining)
	text = text.replace(parts_of_speech1[index], answer[index])
	index = index + 1

		

    print "Good Job! You got all right answers."
    exit(0)

Gamesetup()


			


