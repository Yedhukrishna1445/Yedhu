import random
while True:
	a=input("Enter r to roll a dice:")
	if(a=='r'):
		y=random.randint(1,6)
		print(y)
	else:
		break

