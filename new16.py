import random
a={1:'rock',2:'paper',3:'scissor'}
while True:
	p=input("your choice rock/paper/scissor")
	c=input("computer choice rock/paper/scissor")
	r=random.randint(1,3)
	print("your chooce=p","computer chooce=c")
	if(p==c):
		print("draw")
	elif(p=rock and c=paper):
		print("computer won")
	elif(p==rock and c==scissor):
		print("plyer won")
	elif(p==paper and c==rock):
		print("plyer won")
	elif(p==paper and c==scissor):
		print("computer won")
	elif(p==scissor and c==rock):
		print("computer won")
	elif(p==scissor and c==paper):
		print("plyer won")
	else:
		break