import matplotlib.pyplot as plt


# Data for the student distribution
labels = ['CBA', 'CS', 'BDA', 'Diploma (BDA)', 'Diploma (CBA)']
sizes = [35, 45, 25, 20, 10]


# Plotting the pie chart
plt.figure(figsize=(10, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)


# Adding a title
plt.title('Student Distribution in 4th Semester - Institute of Computer Technology, Ganpat University')


# Display the plot
plt.show()
