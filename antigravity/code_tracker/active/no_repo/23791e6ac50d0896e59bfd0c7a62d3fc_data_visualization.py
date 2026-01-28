Îimport pandas as pd
import matplotlib.pyplot as plt
data = {
    'Student': ['A', 'B', 'C', 'D', 'E'],
    'Maths': [78, 88, 92, 65, 80],
    'Science': [85, 79, 91, 70, 88],
    'English': [74, 93, 80, 72, 84],
    'tamil' : [71, 67, 85, 71, 86]
}

df = pd.DataFrame(data)
print(df)

avg_marks = df[['Maths', 'Science', 'English', 'tamil']].mean()

plt.bar(avg_marks.index, avg_marks.values)
plt.title('Average Marks per Subject')
plt.xlabel('Subject')
plt.ylabel('Average Marks')
plt.show()

plt.plot(df['Student'], df['Maths'], marker='o')
plt.title('Maths Marks of Students')
plt.xlabel('Student')
plt.ylabel('Marks')
plt.show()

plt.imshow(df[['Maths', 'Science', 'English', 'tamil']])
plt.colorbar(label='Marks')
plt.xticks([0,1,2,3], ['Maths', 'Science', 'English','tamil'])
plt.yticks([0,1,2,3,4], df['Student'])
plt.title('Student Marks Heatmap')
plt.show()

plt.boxplot([df['Maths'], df['Science'], df['English'], df['tamil']])
plt.xticks([1,2,3,4], ['Maths', 'Science', 'English', 'tamil'])
plt.title('Marks Distribution')
plt.ylabel('Marks')
plt.show()Î2 file:///d:/data_visualization.py