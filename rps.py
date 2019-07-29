import random

def main():
	play_game()

def get_rounds(): 
	games = int(raw_input("How many rounds would you like to play?\n"))	
	print("")
	return games

def play():
	allowed = [1,2,3]
	valid = False
	
	while valid == False:
		print("Press the corresponding number to make your selection:")
		print("[1] ROCK")
		print("[2] PAPER")
		print("[3] SCISSORS")	 
		
		selection = str(raw_input())
		if selection == "1":
			print("You played ROCK")
			valid = True 
		elif selection == "2": 
			print("You played PAPER")
			valid = True
		elif selection == "3":
			print("You played SCISSORS")
			valid = True 
		else:	
			print("Input invalid: Try again")

	return int(selection)

def cpu_play():
	choice = random.randrange(1,4)
	if choice == 1: 
		print("CPU played ROCK")
	elif choice == 2:
		print("CPU played PAPER")
	else:
		print("CPU played SCISSORS")

	return choice

def play_game():
	p_score = 0
	c_score = 0
	for i in range(get_rounds()): 
		print("ROUND " + str(i+1))
		player = 0
		cpu = 0
		while player == cpu:
			player = play()
			cpu = cpu_play()
			print("")
			if player == cpu:
				print("Tie game; repeat the round\n")
		if (player == 1 and cpu == 3) or (player == 2 and cpu == 1) or (player == 3 and cpu == 2):
			print("Player Victory (+1 point)\n")	
			p_score += 1
		else:
			print("CPU Victory (+1 point)\n")
			c_score += 1
		print_score(p_score, c_score)
	
	if p_score == c_score:
		print("TIE GAME")
	elif p_score > c_score:
		print("PLAYER WIN")
	else:
		print("CPU WIN")
				
def print_score(p, c):
	print("Player: " + str(p))
	print("CPU: " + str(c) + "\n")	

if __name__ == '__main__':
	main()
