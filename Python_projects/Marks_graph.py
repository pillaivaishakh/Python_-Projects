import matplotlib.pyplot as plt
import numpy as np

E1 = [20, 18, 30, 22, 15]
E2 = [19, 22, 33, 30, 19]

# Calculate the difference between marks in E1 and E2
diff = np.array(E2) - np.array(E1)

# Set the x-axis labels
labels = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5']

# Create a bar chart to show the difference in marks
plt.bar(labels, diff)

# Add title and axis labels
plt.title('Difference in Marks between E1 and E2')
plt.xlabel('Subjects')
plt.ylabel('Marks')

# Show the bar chart
plt.show()
