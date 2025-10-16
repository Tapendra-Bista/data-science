from turtle import color
import numpy as np
import matplotlib.pyplot as mt
from scipy import stats

# mean
data = [1,3,5,6,8,4,3,5,6,3]
mean = np.mean(data)
print('Mean is:', mean)

# median 
median = np.median(data)
print('Median is:', median)

# mode
mode = stats.mode(data)
print('Mode is:', mode.mode, 'Count is:', mode.count)

# skewness
skewness = stats.skew(data)
print('Skewness is:', skewness)

# bar graph
names  = ['A','B','C','D']
values = [1,4,2,5]
mt.bar(names,values,color='purple')
mt.title("Bar Graph Example")
mt.xlabel('Names')
mt.ylabel('Values')
mt.show()

# pie  chart
mt.pie(values, labels = names, autopct='%1.1f%%', startangle=120)
mt.title('Pie Chart Example')
mt.show()

# histogram
mt.hist(data, bins=2, color='green', edgecolor='black')
mt.title('Histogram Example')
mt.xlabel('Value')
mt.ylabel('Frequency')
mt.show()

# pareto chart
data = [4,2,5,8,6,3,4,5,6,7,8,9,5,4,3,2,1]
data.sort(reverse=True)         
frequency = np.array(data)
cumulative_frequency = np.cumsum(frequency)
cumulative_percentage = 100 * cumulative_frequency / cumulative_frequency[-1]

fig, ax1 = mt.subplots()
ax2 = ax1.twinx()
ax1.bar(range(len(frequency)), frequency, color='C0')
ax2.plot(range(len(cumulative_percentage)), cumulative_percentage, color='C1', marker='D', ms=7)
ax1.set_xlabel('Data Points')

ax1.set_ylabel('Frequency', color='C0')
ax2.set_ylabel('Cumulative Percentage', color='C1')
ax2.axhline(80, color='r', linestyle='--')
mt.title('Pareto Chart Example')
mt.show()

# scatter plot
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,3,5,7,11,13,17,19,23,29]
mt.scatter(x, y, color='orange')
mt.title('Scatter Plot Example')
mt.xlabel('X-axis')
mt.ylabel('Y-axis')
mt.show()

# box plot
data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
mt.boxplot(data, vert=True, patch_artist=True, boxprops=dict(facecolor='lightblue'))
mt.title('Box Plot Example')

mt.ylabel('Values')
mt.show()   


# line graph
x = np.linspace(0, 10, 100)
y = np.sin(x)

mt.plot(x, y, color='magenta')
mt.title('Line Graph Example')
mt.xlabel('X-axis')
mt.ylabel('Y-axis')
mt.grid()
mt.show()




