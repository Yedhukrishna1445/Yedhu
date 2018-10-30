import matplotlib.pyplot as plt

#x-cordinates of left sides of bars
left=[1,2,3,4,5]

#hights of bars
hight=[10,24,36,40,5]

#Labels for bars
tick_label=['one','two','three','four','five']

#Plotting a bar chart
plt.bar(left,height,tick_label=tick_label,
		width=0.8,color=['blue','red'])

#naming the x-axis
plt.xlbel('x-axis')

#naming the y-axis
plt.ylabel('y-axis')

#naming the graph
plt.title('my bar graph')

plt.show()  		  