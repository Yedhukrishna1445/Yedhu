from random import randint
#create a list play option
p=["rock","paper","scissor"]

#assign a random play to the computer
computer=p[randint(0,2)]

#set player to False
player=False

while player ==False:
#set player to true
	player=input("rock,paper,scissor")
	if player==computer:
		print("Tie")
	elif player=="rock":
		if computer=="paper":
			print("you lose",computer,"try again",player)
		else:
			print("you win",player,"ureaka",computer)	
	elif player=="paper":
		if computer=="scissor":
			print("you lose",computer,"try again",player)
		else:
			print("you win",player,"ureaka",computer)
	elif player=="scissor":
		if computer=="rock":
				print("you lose",computer,"try again",player)
		else:
			print("you win",player,"ureaka",computer)
	else:
		break	
	#player was set to True, but we want it to be False so the loop continues
	player=False
	computer=p[randint(0,2)]				