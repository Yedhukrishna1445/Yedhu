import random
while True:
	a=input("Enter r to roll a dice:")
	if(a=='r'):
		i=random.randint(1,6)
		print(i)
	else:
		break
