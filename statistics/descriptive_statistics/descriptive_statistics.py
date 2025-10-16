# Population
#-----> Collection of all items of interest 
# Notation: N
# Example: All students in a school

# Sample 
#-----> Subset of the population
# Notation: n
# Example: 50 students selected from the school


#  Types  of data 

# There are two types of data
# Categorical Data
# Numerical Data

# Categorical Data
#-----> Data that can be divided into groups or categories
# 1. Car brands : Audi, BMW, Toyota
# 2. Colors : Red, Blue, Green
# 3. Answers to yes/no questions


# Numerical Data
#-----> Numerical data represents numbers.
# it is divided into two types 
# 1. Discrete Data
#-------> Discrete data can be usually counted in a finite matter
# Example: Number of students in a class, Number of cars in a parking lot

# 2. Continuous Data
#-------> Continuous data is infinte and impossible to count 

# Example: Height of students, Weight of students, Temperature
# Discrete : children  you want to have, SAT Score
# Continous : height, weight



# Levels of Measurement
# There are four levels of measurement
# 1. Qualitative
# Nominal------> This cannot be put in order
# Example : car brands, colors, four seasons(spring, summer, fall, winter)
# Ordinal ------> This can be put in order
# Example : movie ratings (poor, fair, good, excellent), education level (high school, bachelor's, master's)

# 2. Quantitative 
# Interval-------> This can be put in order and the difference between two values is meaningful
# Example : Temperature in Celsius or Fahrenheit, IQ scores
# Ratio-------> This can be put in order, the difference is meaningful, and there is a true zero point
# Example : Height, weight, duration

# What do you mean by true zero point?
# A true zero point means that the value of zero indicates the absence of the quantity being measured.
# For example, in the case of height, a height of zero means there is no height at all.
# In contrast, in the case of temperature measured in Celsius or Fahrenheit, a temperature of zero does not mean there is no temperature; it is simply a point on the scale.
# Therefore, height and weight are measured on a ratio scale because they have a true zero point, while temperature is measured on an interval scale because it does not have a true zero point.



# Mean, Median, Mode
# The mean is the the most widely used measure of central tendency.
# It is the simple average of  the  dataset.

# The formula for mean is 
# Mean = (Sum of all values) / (Number of values)
# Example : Find the mean of the following dataset
data = [10, 20, 30, 40, 50]
mean = sum(data)/ len(data)
print("Mean:", mean)

# using numpy
from turtle import color
import numpy as np 

mean_np = np.mean(data)
print("Mean using numpy:", mean_np)



# Median 
# The median is the middle value of a dataset when it is ordered from asending to descending.
# It is not as popular as the mean, but is often used when the  academia and data science.
#  In an ordered dataset, the median is the number at position
# (n + 1) / 2 if n is odd
# (n / 2) and (n / 2) + 1 if n is even
# Example : Find the median of the following dataset

median =  (len(data)+1 )/2
print("Median position:", median)
print("Median value:", data[int(median)-1])

# using numpy
median_np = np.median(data)
print("Median using numpy:", median_np)

# Mode
# The Mode is the value that occurs most frequently in a dataset.
# A dataset may have one mode, more than one mode, or no mode at all.
# Example : Find the mode of the following dataset

data_mode = [1, 2, 2, 3, 4, 4, 4, 5]
# using scipy
from scipy import stats
mode = stats.mode(data_mode)
print("Mode:", mode.mode, "Count:", mode.count)


# Graphs and tables that represent categorical variables.

# Frequency distribution tables

#                   Frequency
# Audi                  5
# BMW                  10   
# Toyota               15
# Honda                20
# Ford                 25
# Total                75


# Bar Graphs 
# Bar charts are  also called clustered column charts.

# Example : Using matplotlib to create a bar graph
import matplotlib.pyplot as plt
car_brands = ['Adui','BMW','Toyota', 'Honda', 'Ford']
frequencies = [5,10,14,20,25]
plt.bar(car_brands,frequencies)
plt.xlabel('Car Brands')
plt.ylabel('Frequency')
plt.title("Car Brands Frequency")
plt.show()

# Pie Charts 
# Pie charts are circular charts divided into sectors, each representing a proportion of the whole.
# Pie charts are created in the following way
# Example : Using matplotlib to create a pie chart
plt.pie(frequencies, labels= car_brands,colors=['red','blue','green','yellow', 'orange'],autopct='%1.1f%%') # autopct is used to show the percentage
plt.title('Car Brands Frequency')
plt.show()

#  Pareto diagrams
# Pareto diagrams are bar charts that display the frequency of categories in descending order, along with a cumulative percentage line.
# Example : Using matplotlib to create a Pareto diagram
sorted_freuencies = sorted(frequencies, reverse= True)
cumulative_frequencies = np.cumsum(sorted_freuencies)
plt.bar(car_brands,sorted_freuencies,color='blue')
plt.plot(car_brands, cumulative_frequencies, color = 'orange', marker='o')
plt.xlabel('Car Brands')
plt.ylabel('Frequency')
plt.title("Pareto diagrams")
plt.show()

# Histograms
# Histograms are graphical representations of the distribution of numerical data.
# They are created by dividing the data into intervals (bins) and counting the number of data points that fall within each interval.
# Example : Using matplotlib to create a histogram
data_hist = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
plt.hist(data_hist, bins=5, color = 'blue', edgecolor = 'black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()


# Scatter Plots
# Scatter plots are used to display the relationship between two numerical variables.
# Example : Using matplotlib to create a scatter plot
x = [1,2,3,4,5]
y = [2,3,5,7,11]
plt.scatter(x,y,color='orange')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()


# skewness 
# Skewness is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean.
# Skewness can be positive, negative, or undefined.
# Positive skewness indicates that the tail on the right side of the distribution is longer or fatter than the left side.
# Negative skewness indicates that the tail on the left side is longer or fatter than the
# right side.
# A skewness value of zero indicates that the tails on both sides of the mean balance out.
# Example : Calculate the skewness of a dataset using scipy
data_skew = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
skewness = stats.skew(data_skew)
print("Skewness:", skewness)