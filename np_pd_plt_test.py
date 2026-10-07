import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print(np.__version__)
print(pd.__version__)
print(matplotlib.__version__)

#numpy
import numpy as np

# Math on every number
scores = np.array([70, 85, 90, 65, 100])
print("Plus 5 bonus:", scores + 5)

# Average and highest
print("Average:", np.mean(scores))
print("Highest:", np.max(scores))

# A 2D array (rows and columns)
table = np.array([[1, 2, 3], [4, 5, 6]])
print("Table:")
print(table)
print("Shape:", table.shape)

#Pandas
import pandas as pd

#  Create a table 
students = pd.DataFrame({
    "Name": ["Hassan", "Mohamed", "John", "Alice"],
    "Age": [20, 22, 19, 21],
    "Score": [85, 90, 70, 95]
})
print(students)

#Pick one column and find its average
print("Average score:", students["Score"].mean())

#Filter rows (scores above 80)
print(students[students["Score"] > 80])


#Matplotlib
import matplotlib.pyplot as plt

#Line chart
plt.plot([1, 2, 3, 4], [10, 20, 25, 40])
plt.title("Line Chart")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()

#Bar chart
names = ["Hassan", "Mohamed", "John", "Alice"]
scores = [85, 90, 70, 95]
plt.bar(names, scores)
plt.title("Bar Chart")
plt.ylabel("Score")
plt.show()

#Scatter plot
plt.scatter([1, 2, 3, 4, 5], [5, 7, 4, 8, 6])
plt.title("Scatter Plot")
plt.show()


