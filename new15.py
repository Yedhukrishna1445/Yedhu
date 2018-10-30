import random
count=0
while(count<=100):
	a=input("Enter r to roll a dice:")
	if(a=='r'):
		y=random.randint(1,6)
		print(y)
		count=count+y
		print(count)
	elif(count==100):
		print("you win")
	elif(count==11):
		count=2
		print("snake is byte come down")
	elif (count==8):
		count=37
		print("climbes a lader")
	elif (count==13):
		count=34
		print("climbes a lader")
	elif (count==25):
		count=4
		print("snake is byte come down")
	elif(count==38):
		count=9
		print("snake is byte come down")
	elif(count==40):
		count=68
		print("climbes a lader")
	elif(count==52):
		count=81
		print("climbes a lader")
	elif(count==65):
		count=46	
		print("snake is byte come down")
	elif(count==76):
		count=97
		print("climbes a lader")
	elif(count==93):
		count=64
		print("snake is byte come down")		
	else:
		break