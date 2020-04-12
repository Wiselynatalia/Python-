#python_version == '3.7.4'
import matplotlib.pyplot as plt
import numpy as np 
#draw histogram
random_numbers = np.random.normal(0,1,1000)
plt.figure()
plt.ylabel("Probability density")
plt.xlabel("Random numbers")
plt.hist(random_numbers)
plt.savefig(fname= "histogram.png")
#draw piechart
plt.figure()
labels = "New Asia College", "United College", "Chung Chi College"
size = [3400,3272,3147]
colors = ["gold","lightblue","lightcoral"]
plt.pie(size, labels = labels, colors = colors, autopct="%1.1f%%")
plt.savefig(fname="pie.png")
#draw barchart
plt.figure()
objects = "New Asia", "United","Chung Chi","Shaw","C.W.Chu", "S.H.Ho","Wu Yee Sun","Lee Woo Sing","Morningside"
size = [3400,3272,3147,3441,300,600,1200,1389,300]
plt.ylabel("Number of Students")
plt.xlabel("Colleges")
plt.bar(objects, size)
plt.xticks(objects, rotation=45)
plt.savefig(fname="bar.png", bbox_inches = 'tight')
#Scatter plot and line chart
plt.figure()
plt.ylabel("y-axis")
plt.xlabel("x-axis")
x_list = np.linspace(0,1,100)
y_list= x_list + np.random.rand(100)
plt.scatter(x_list,y_list,alpha=0.5)
y = x_list
plt.plot(x_list,y)
plt.grid()
plt.savefig(fname="scatter_line.png")